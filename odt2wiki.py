#!/usr/bin/env python

"Convert ODT to markdown splitting the output into chapters."

from argparse import ArgumentParser
from zipfile import ZipFile
import os.path
import functools
import importlib

import odt_tools
import odt_parser
import document
import github_writer, hugo_writer
import image_matcher


TEXT_XML_FILE_NAME = "content.xml"
STYLES_XML_FILE_NAME = "styles.xml"


def _print_dict_tree(key, tree, level):
    print((" " * 4 * level) + key)
    for (k, v) in sorted(tree.items()):
        _print_dict_tree(k, v, level + 1)
        
def _print_visitor(section):
    print("  " * section.header.outline_level + section.header.to_string())

def _print_doc_tree(doc):
    doc.root().traverse(_print_visitor)


# Troubleshooting methods

def list_files(archive):
    for f in archive.namelist():
        print(f)

def list_attrs(content):
    visitor = odt_tools.UniqueTagsVisitor()
    visitor.traverse(content)
    tags = visitor.results()
    max_len = max(len(t) for t in tags)
    for (t, v) in sorted(tags.items()):
        print(f"{t + ':':{max_len + 2}}{', '.join(v)}")
        
def tags_tree(content):
    visitor = odt_tools.TagsTreeVisitor()
    visitor.traverse(content)
    tags = visitor.results()
    for (k, v) in sorted(tags.items()):
        _print_dict_tree(k, v, 0)

def extract_text(content, dest_path):
    visitor = odt_tools.TextVisitor()
    visitor.traverse(content)
    with open(dest_path, "x") as output:
        output.write(visitor.results())
        

# Main methods        

def _create_document(content, styles, dest_path, split_level, strategy, customization, landing_name):
    # Parse the input file
    visitor = odt_parser.FullVisitor()
    visitor.preload_styles(styles)
    visitor.traverse(content)
    # Process the content
    doc = document.Document(dest_path, split_level, strategy, customization)
    visitor.fill_document(doc)
    doc.finalize()
    # Add the landing page
    doc.push_root(document.Section.create(landing_name))
    doc.create_folders()
    # Create the table of contents
    index = document.TocMaker(strategy).make(doc.root())
    doc.root().content.append(index)
    # The index may be reused
    return doc, index

def _process_images(doc, archive, dest_path, images_folder, remote_image_path):
    external_images = {}
    internal_images = {}
    if images_folder:
        if not image_matcher.has_image_matcher:
            print("FATAL: Matching images requires Pillow to be installed\n")
            exit(1)
        full_local_path = os.path.expanduser(images_folder)
        matched, unmatched = image_matcher.match_images(archive, full_local_path)
        if remote_image_path is not None:
            external_images = {k: v.replace(full_local_path, remote_image_path) for k, v in matched.items()}
        else:
            external_images = matched
        if unmatched:
            internal_images = image_matcher.extract_images(archive, dest_path, unmatched)
    else:
        internal_images = image_matcher.extract_all_images(archive, dest_path)
    doc.link_images(external_images, internal_images)


def convert_to_github_markdown( archive,
                                content, 
                                styles, 
                                dest_path, 
                                collapse_level, 
                                split_level, 
                                images_folder, 
                                remote_image_path,
                                customization):
    # Set up
    strategy = github_writer.github_strategy
    doc, index = _create_document(content, styles, dest_path, split_level, strategy, customization, "Home")
    side_toc = document.Section.create("_Sidebar", [index,], dest_path)
    # Map pictires inside the ODT to picture files in the destination folder
    _process_images(doc, archive, dest_path, images_folder, remote_image_path)
    # Convert to markdown
    doc.crosslink()
    doc.dump(functools.partial(github_writer.GithubMarkdownWriter, collapse_level=collapse_level))
    side_toc.dump(functools.partial(github_writer.GithubMarkdownWriter, toc_collapse_level=1))   # Collapse book parts in the ToC
    print(f"GitHub markdown created in {dest_path}")

def convert_to_hugo_markdown(   archive,
                                content, 
                                styles, 
                                dest_path, 
                                collapse_level, 
                                split_level, 
                                images_folder, 
                                remote_image_path,
                                customization):
    assert not collapse_level, "Not implemented"
    # Set up
    strategy = hugo_writer.hugo_strategy
    doc, _ = _create_document(content, styles, dest_path, split_level, strategy, customization, "Table of Contents")
    # Map pictires inside the ODT to picture files in the destination folder
    _process_images(doc, archive, dest_path, images_folder, remote_image_path)
    # Convert to markdown
    doc.crosslink()
    doc.dump(hugo_writer.HugoMarkdownWriter)
    print(f"Hugo markdown created in {dest_path}")


def main():
    description = "Convert ODT to wiki markdown. It can split a book into chapters and match images from the document to those on your drive."
    usage = """
odt2wiki.py <input.odt> --print={files|attrs|tags}
odt2wiki.py <input.odt> <output.txt> --convert=text
odt2wiki.py <input.odt> <output_folder> --convert={github|hugo} [--collapse=<level>] [--split=<level>] [--images-folder=<folder> [--remote-images={<link>|<folder>}]] [--customize=<python_module>]"""
    
    # Set up the CLI arguments
    parser = ArgumentParser(description=description, usage=usage)
    
    parser.add_argument("input", help="input ODT file")
    parser.add_argument("output", help="output file or folder", default=None, nargs="?")
    
    group = parser.add_argument_group("Mode of action")
    group = group.add_mutually_exclusive_group(required=True)
    group.add_argument("-p", "--print", choices=("files", "attrs", "tags"), help="print info about the ODT: %(choices)s")
    group.add_argument("-c", "--convert", choices=("text", "github", "hugo"), help="convert the ODT into a chosen format: %(choices)s")
    
    group = parser.add_argument_group("Options for markdown conversion")
    group.add_argument("-l", "--collapse-level", action="store", type=int, default=0, help="collapse sections at this outline level")
    group.add_argument("-s", "--split-level", action="store", type=int, default=0, help="split sections into files at this outline level")
    group.add_argument("-i", "--images-folder", action="store", help="local folder with images used throughout the document")
    group.add_argument("-r", "--remote-images", action="store", help="route image requests from wiki to this folder")
    group.add_argument("-z", "--customize", action="store", help="custom rules for your document")
    
    args = parser.parse_args()
    
    # Run the user's command
    print()
    print(f"Processing ODT archive {args.input}...")
    with ZipFile(os.path.expanduser(args.input)) as archive:
        assert args.input
        parsed_content = odt_tools.parse(archive.read(TEXT_XML_FILE_NAME))
        parsed_styles = odt_tools.parse(archive.read(STYLES_XML_FILE_NAME))
        if args.print:
            if args.output:
                parser.print_usage()
                print("Output file is not supported with --print")
                exit()
            match args.print:
                case "files":
                    print("Archive contents:")
                    list_files(archive)
                case "attrs":
                    print(f"Attributes for each tag in {STYLES_XML_FILE_NAME}:")
                    list_attrs(parsed_styles)
                    print()
                    print(f"Attributes for each tag in {TEXT_XML_FILE_NAME}:")
                    list_attrs(parsed_content)
                case "tags":
                    print(f"Hierarchy of tags for {STYLES_XML_FILE_NAME}:")
                    tags_tree(parsed_styles)
                    print()
                    print(f"Hierarchy of tags for {TEXT_XML_FILE_NAME}:")
                    tags_tree(parsed_content)
                case _:
                    assert False
        elif args.convert:
            # Process parameters
            if not args.output:
                parser.print_usage()
                print("Output file or folder is required for --convert")
                exit()
            dest_path = os.path.expanduser(args.output)
            if args.customize:
                customization = importlib.import_module("custom." + args.customize).customization
            else:
                customization = document.Customization()
            # Run
            match args.convert:
                case "text":
                    print(f"Extracting text from {TEXT_XML_FILE_NAME} to {args.output}")
                    extract_text(parsed_content, dest_path)
                case "github":
                    print(f"Converting to GitHub markdown in {args.output}")
                    convert_to_github_markdown( archive,
                                                parsed_content, 
                                                parsed_styles, 
                                                dest_path,
                                                args.collapse_level, 
                                                args.split_level,
                                                args.images_folder,
                                                args.remote_images,
                                                customization)
                case "hugo":
                    print(f"Converting to Hugo markdown in {args.output}")
                    convert_to_hugo_markdown(   archive,
                                                parsed_content, 
                                                parsed_styles, 
                                                dest_path,
                                                args.collapse_level, 
                                                args.split_level,
                                                args.images_folder,
                                                args.remote_images,
                                                customization)
                case _:
                    assert False
    print()


if __name__ == "__main__":
    main()