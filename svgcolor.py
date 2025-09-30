#!/usr/bin/env python

from argparse import ArgumentParser
from collections import defaultdict
import os

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
        with open(os.path.join(path, filename)) as file:
            self._process_content(file.read(), filename)
    
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

"""
class ReplaceTraverser(Traverser):
    def __init__(self, path, color):
        super().__init__(path)
        self._color = color
        self._files = []
    
    def _process_content(self, content, filename):
        if svg_tools.contains_color(content, self._color):
            self._files.append(filename)
    
    def done(self):
        print(f"{len(self._files)} FILES WITH COLOR {self._color}:")
        for f in self._files:
            print(f)
"""

def main():
    description = "Change colors in SVG files."
    usage = """
svgcolor.py <input_folder> --list
svgcolor.py <input_folder> --explore <file_name>
svgcolor.py <input_folder> --find <color_code>
svgcolor.py <input_folder> --no-find <color_code>
svgcolor.py <input_folder> <output_folder> --replace <color_map>"""
    
    # Set up the CLI arguments
    parser = ArgumentParser(description=description, usage=usage)
    
    parser.add_argument("input", help="folder with SVG images")
    parser.add_argument("output", help="folder for processed SVG images", default=None, nargs="?")
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-l", "--list", action="store_true", help="list all the colors used in the images")
    group.add_argument("-o", "--list-one", action="store", help="see which colors a given SVG file uses")
    group.add_argument("-f", "--find", action="store", help="find which SVG files use a given color")
    group.add_argument("-n", "--no-find", action="store", help="find which SVG files don't use a given color")
    group.add_argument("-r", "--replace", action="store", help="transform the input images with this color map file")
    
    args = parser.parse_args()
    assert args.input
    if args.replace:
        if not args.output:
            parser.print_usage()
            print("Output folder is required for --replace")
            exit()
    else:
        if args.output:
            parser.print_usage()
            print("Output folder is supported only with --replace")
            exit()
        if args.list:
            traverser = ListTraverser(args.input)
        elif args.list_one:
            traverser = ListOneTraverser(args.input, args.list_one)
        elif args.find:
            traverser = FindTraverser(args.input, args.find)
        elif args.no_find:
            traverser = NoFindTraverser(args.input, args.no_find)
        else:
            assert False
    
    print()
    print(f"Processing SVG images in {args.input} ...")
    traverser.run()
    traverser.done()
    print()
    
    
if __name__ == "__main__":
    main()