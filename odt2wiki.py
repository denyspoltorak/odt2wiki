#!/usr/bin/env python

"Convert ODT to markdown splitting the output into chapters."

import argparse
import file_access
import odt_parser


TEXT_XML_FILE_NAME="content.xml"


def main():
    # Set up the CLI arguments
    parser = argparse.ArgumentParser(description=__doc__)
    
    parser.add_argument("input_filename", help="input ODT file")
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--list-files", action="store_true", help="list files inside the ODT")
    group.add_argument("-t", "--list-tags", action="store_true", help="list tags used in the ODT")
    
    args = parser.parse_args()
    
    # Run the user's command
    print()
    # Print files in the archive
    if args.list_files:
        print("ODT contents:")
        for f in file_access.list_files_in_archive(args.input_filename):
            print(f)
    # Print tags in content.xml
    elif args.list_tags:
        print(f"tags in {args.input_filename + '/' + TEXT_XML_FILE_NAME}:")
        tags = odt_parser.unique_tags(odt_parser.parse(file_access.read_single_file(args.input_filename, TEXT_XML_FILE_NAME)))
        max_len = max(len(t) for t in tags)
        for (t, v) in sorted(tags.items()):
            print(f"{t + ':':{max_len + 2}}{v}")
    else:
        assert(False)
    print()


if __name__ == "__main__":
    main()