#!/usr/bin/env python

"Convert ODT to markdown splitting the output into chapters."

import argparse
import file_access
import odt_parser


TEXT_XML_FILE_NAME="content.xml"
STYLES_XML_FILE_NAME="styles.xml"


def print_dict_tree(key, tree, level):
    print((" " * 4 * level) + key)
    for (k, v) in sorted(tree.items()):
        print_dict_tree(k, v, level + 1)


def main():
    # Set up the CLI arguments
    parser = argparse.ArgumentParser(description=__doc__)
    
    parser.add_argument("input_filename", help="input ODT file")
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--list-files", action="store_true", help="list files inside the ODT")
    group.add_argument("-g", "--list-tags", action="store_true", help="list unique tags used in the ODT")
    group.add_argument("-t", "--tags-tree", action="store_true", help="print the hierarchy of tags")
    
    args = parser.parse_args()
    
    # Run the user's command
    print()
    # Print files in the archive
    if args.list_files:
        print("ODT contents:")
        for f in file_access.list_files_in_archive(args.input_filename):
            print(f)
    else: # Process content.xml in the archive
        parsed_content = odt_parser.parse(file_access.read_single_file(args.input_filename, TEXT_XML_FILE_NAME))
        # Print tags from content.xml
        if args.list_tags:
            print(f"tags in {args.input_filename + '/' + TEXT_XML_FILE_NAME}:")
            tags = odt_parser.unique_tags(parsed_content)
            max_len = max(len(t) for t in tags)
            for (t, v) in sorted(tags.items()):
                print(f"{t + ':':{max_len + 2}}{v}")
        # Print the tree of tags from content.xml
        elif args.tags_tree:
            print(f"hierarchy of tags for {args.input_filename + '/' + TEXT_XML_FILE_NAME}:")
            tree = odt_parser.tree_of_tags(parsed_content)
            for (k, v) in tree.items():
                print_dict_tree(k, v, 0)
        else:
            assert(False)
    print()


if __name__ == "__main__":
    main()