#!/usr/bin/env python

from argparse import ArgumentParser
from collections import defaultdict
import os
import functools
import colorsys

import svg_tools


# Parent class which processes all SVG images in a folder
class Traverser:
    def __init__(self, path):
        assert path
        self._path = os.path.expanduser(path)
    
    def run(self):
        for path, dirs, files in os.walk(self._path, onerror=self._assert):
            for d in dirs:
                try:
                    self._process_dir(path, d)
                except Exception as e:
                    print(f"Exception {e} while processing dir {path + '/' + d + '/'}")
                    raise
            for f in files:
                try:
                    if os.path.splitext(f)[1].lower() == ".svg":
                        self._process_file(path, f)
                except Exception as e:
                    print(f"Exception {e} while processing file {path + '/' + f}")
                    raise
    
    def done(self):
        pass
    
    def _process_dir(self, path, directory):
        pass
    
    def _process_file(self, path, filename):
        assert path.startswith(self._path)
        rel_path = path[len(self._path):]
        with open(os.path.join(path, filename)) as file:
            self._process_content(file.read(), rel_path + "/" + filename)
    
    def _process_content(self, content, filename):
        pass

    @staticmethod
    def _assert(_):
        assert False


class ListTraverser(Traverser):
    def __init__(self, path):
        super().__init__(path)
        self._colors = defaultdict(int)
    
    def _process_content(self, content, filename):
        result = svg_tools.list_colors(content)
        assert len(result)
        for c in result:
            self._colors[c] += 1
    
    def done(self):
        print("COLOR:\t\tINSTANCES")
        for color, num_usages in sorted(self._colors.items(), key=lambda item: item[1], reverse=True):
            print(f"{color}:\t\t{num_usages}")
            

class ListOneTraverser(Traverser):
    def __init__(self, path, file):
        super().__init__(path)
        self._file = file
        
    def _process_file(self, path, filename):
        if filename == self._file:
            with open(os.path.join(path, filename)) as file:
                self._process_content(file.read(), filename)
    
    def _process_content(self, content, filename):
        result = svg_tools.list_colors(content)
        assert len(result)
        print(f"COLORS IN {filename}:")
        print(sorted(result))


class FindTraverser(Traverser):
    def __init__(self, path, color):
        super().__init__(path)
        self._color = color
        self._regexp = svg_tools.make_regexp(color)
        self._files = []
    
    def _process_content(self, content, filename):
        if svg_tools.contains_regexp(content, self._regexp):
            self._files.append(filename)
    
    def done(self):
        print(f"{len(self._files)} FILES WITH COLOR {self._color}:")
        for f in self._files:
            print(f)


class NoFindTraverser(FindTraverser):
    def _process_content(self, content, filename):
        if not svg_tools.contains_regexp(content, self._regexp):
            self._files.append(filename)
    
    def done(self):
        print(f"{len(self._files)} FILES WITHOUT COLOR {self._color}:")
        for f in self._files:
            print(f)


class FindImagesTraverser(Traverser):
    def __init__(self, path):
        super().__init__(path)
        self._files = []
    
    def _process_content(self, content, filename):
        if svg_tools.contains_image(content):
            self._files.append(filename)
    
    def done(self):
        print(f"{len(self._files)} FILES WITH EMBEDDED IMAGES:")
        for f in self._files:
            print(f)


class RemapTraverser(Traverser):
    def __init__(self, input_path, output_path, config_file, infix):
        super().__init__(input_path)
        self._color_map, self._default_actions = self._read_config(os.path.expanduser(config_file))
        self._output_path = os.path.expanduser(output_path)
        os.mkdir(self._output_path)
        self._infix = infix
        self._overflows = set()
    
    def _process_dir(self, path, directory):
        assert path.startswith(self._path)
        new_path = self._output_path + "/" + path[len(self._path):] + "/" + directory
        os.mkdir(new_path)
    
    def _process_content(self, content, filename):
        assert filename.endswith(".svg")
        if self._infix:
            filename = filename[:-3] + self._infix + ".svg"
        processed = svg_tools.replace(content, self._color_map, self._default_actions)
        with open(self._output_path + "/" + filename, "x") as file:
            file.write(processed)

    def _read_config(self, config_file):
        color_map = {}
        default_actions = []
        with open(config_file) as file:
            for l in file.readlines():
                l = l.split("#")[0] # strip comments
                words = l.split()
                if not words:       # empty line
                    continue
                assert len(words) == 2
                if words[0] == "*": # operations for colors not listed in the config
                    default_actions.append(functools.partial(self._multiply_rgb, multiplier=float(words[1])))
                elif words[0] == "~":
                    default_actions.append(functools.partial(self._invert_lightness, pivot=float(words[1])))
                elif words[0] == "/":
                    default_actions.append(functools.partial(self._saturate, divisor=float(words[1])))
                else:               # mapping one color onto another
                    assert words[0] not in color_map
                    color_map[words[0]] = words[1]
        return svg_tools.prepare_color_map(color_map), default_actions

    def done(self):
        if self._overflows:
            print("COLOR MULTIPLICATION OVERFLOWS:")
            for c in sorted(self._overflows):
                print(c)
    
    # Operations
    def _multiply_rgb(self, color, multiplier):
        result = ""
        assert len(color) == 6
        for i in range(3):
            value = int(color[2*i: 2*(i+1)], 16)
            value *= multiplier
            if value > 255:
                self._overflows.add(color)
                value = 255
            result += f"{int(value):02x}"
        return result
    
    @staticmethod
    def _invert_lightness(color, pivot):
        # Parse the hex input
        assert len(color) == 6
        rgb = [int(color[2*i: 2*(i+1)], 16) / 255.0 for i in range(3)]
        # Transfor the color: invert Lightness around the pivot value
        h, l, s = colorsys.rgb_to_hls(*rgb)
        if l > pivot:
            l = pivot * ((1 - l) / (1 - pivot))
        else:
            l = 1 - ((l / pivot) * (1 - pivot))
        rgb = colorsys.hls_to_rgb(h, l, s)
        # Print the color back to hex
        result = ""
        for i in range(3):
            result += f"{int(rgb[i] * 255.0):02x}"
        return result
    
    def _saturate(self, color, divisor):
        # Parse the hex input
        assert len(color) == 6
        rgb = [int(color[2*i: 2*(i+1)], 16) / 255.0 for i in range(3)]
        # Transfor the color: invert Lightness around the pivot value
        h, l, s = colorsys.rgb_to_hls(*rgb)
        s = 1 - ((1 - s) / divisor)
        if s < 0:
            self._overflows.add(color)
            s = 0
        rgb = colorsys.hls_to_rgb(h, l, s)
        # Print the color back to hex
        result = ""
        for i in range(3):
            result += f"{int(rgb[i] * 255.0):02x}"
        return result


def main():
    description = "Change colors in SVG files."
    usage = """
svgcolor.py <input_folder> --{list|find-images}
svgcolor.py <input_folder> --explore <file_name>
svgcolor.py <input_folder> --[no-]find <color_code>
svgcolor.py <input_folder> <output_folder> --remap <color_map> [--infix <string>]"""
    
    # Set up the CLI arguments
    parser = ArgumentParser(description=description, usage=usage)
    
    parser.add_argument("input", help="folder with SVG images")
    parser.add_argument("output", help="folder for processed SVG images", default=None, nargs="?")
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-l", "--list", action="store_true", help="list all the colors used in the images")
    group.add_argument("-o", "--list-one", action="store", help="see which colors a given SVG file uses")
    group.add_argument("-f", "--find", action="store", help="find which SVG files use a given color")
    group.add_argument("-n", "--no-find", action="store", help="find which SVG files don't use a given color")
    group.add_argument("-i", "--find-images", action="store_true", help="find SVG files with embedded raster images")
    group.add_argument("-r", "--remap", action="store", help="transform the input images with this color map file")
    
    parser.add_argument("-x", "--infix", action="store", help="extra file extension for remapped colors")
    
    args = parser.parse_args()
    assert args.input
    if args.remap:
        if not args.output:
            parser.print_usage()
            print("Output folder is required for --replace")
            exit()
        traverser = RemapTraverser(args.input, args.output, args.remap, args.infix)
    else:
        if args.output:
            parser.print_usage()
            print("Output folder is supported only with --replace")
            exit()
        if args.infix:
            parser.print_usage()
            print("Infix is supported only with --replace")
            exit()
        if args.list:
            traverser = ListTraverser(args.input)
        elif args.list_one:
            traverser = ListOneTraverser(args.input, args.list_one)
        elif args.find:
            traverser = FindTraverser(args.input, args.find)
        elif args.no_find:
            traverser = NoFindTraverser(args.input, args.no_find)
        elif args.find_images:
            traverser = FindImagesTraverser(args.input)
        else:
            assert False
    
    print()
    print(f"Processing SVG images in {args.input} ...")
    traverser.run()
    traverser.done()
    print()
    
    
if __name__ == "__main__":
    main()