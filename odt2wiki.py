#!/usr/bin/env python

"Convert ODT to markdown splitting the output into chapters."

from zipfile import ZipFile
from os.path import expanduser
from argparse import ArgumentParser

import odt_tools
import odt_parser
import md_writer


TEXT_XML_FILE_NAME="content.xml"
STYLES_XML_FILE_NAME="styles.xml"


def _print_dict_tree(key, tree, level):
    print((" " * 4 * level) + key)
    for (k, v) in sorted(tree.items()):
        _print_dict_tree(k, v, level + 1)
        
        
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


def extract_text(content, destination):
    visitor = odt_tools.TextVisitor()
    visitor.traverse(content)
    with open(expanduser(destination), "x") as output:
        output.write(visitor.results())
        
def convert_to_markdown(content, destination):
    visitor = odt_parser.FullVisitor()
    visitor.traverse(content)
    tree = visitor.to_tree()
    writer = md_writer.GitHubMdWriter()
    tree.dump(writer)
    with open(expanduser(destination), "x") as output:
        output.write(writer.get_output())

def main():
    # Set up the CLI arguments
    parser = ArgumentParser(description=__doc__)
    
    parser.add_argument("input_filename", help="input ODT file")
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--list-files", action="store_true", help="list files inside the ODT")
    group.add_argument("-a", "--list-attrs", action="store_true", help="list attributes for each tag")
    group.add_argument("-t", "--tags-tree", action="store_true", help="print the hierarchy of tags")
    group.add_argument("-x", "--extract-text", action="store", help="extract text from ODT to this file")
    group.add_argument("-g", "--to-github-md", action="store", help="convert to GitHub markdown in the given dir")
    
    args = parser.parse_args()
    
    # Run the user's command
    print()
    print(f"Processing ODT archive {args.input_filename }...")
    with ZipFile(expanduser(args.input_filename)) as archive:
        # Print files in the archive
        if args.list_files:
            print("Archive contents:")
            list_files(archive)
        else: # Process content.xml in the archive
            parsed_content = odt_tools.parse(archive.read(TEXT_XML_FILE_NAME))
            if args.extract_text:
                print(f"Extracting text from {TEXT_XML_FILE_NAME} to {args.extract_text}")
                extract_text(parsed_content, args.extract_text)
            else:
                parsed_styles = odt_tools.parse(archive.read(STYLES_XML_FILE_NAME))
                # Print tags from content.xml
                if args.list_attrs:
                    print(f"Attributes for each tag in {STYLES_XML_FILE_NAME}:")
                    list_attrs(parsed_styles)
                    print()
                    print(f"Attributes for each tag in {TEXT_XML_FILE_NAME}:")
                    list_attrs(parsed_content)
                # Print the tree of tags from content.xml
                elif args.tags_tree:
                    print(f"Hierarchy of tags for {STYLES_XML_FILE_NAME}:")
                    tags_tree(parsed_styles)
                    print()
                    print(f"Hierarchy of tags for {TEXT_XML_FILE_NAME}:")
                    tags_tree(parsed_content)
                elif args.to_github_md:
                    print(f"Converting to GitHub markdown in {args.to_github_md}")
                    convert_to_markdown(parsed_content, args.to_github_md)
                else:
                    assert(False)
    print()


if __name__ == "__main__":
    main()