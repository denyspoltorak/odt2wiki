#!/bin/bash

set -e

if [[ "$#" < 2 || "$#" > 4 ]]; then
    echo "Convert all SVG files in a folder to PNG format, optionally adding transparent margins."
    echo "Usage: ./svg2png <input_folder> <output_folder> [zoom_level] [margins_px]"
    exit 1
fi

INPUT_DIR="$1"
OUTPUT_DIR="$2"
ZOOM="${3:-1}"
MARGIN="$4"

mkdir "$OUTPUT_DIR"

for SVG in "$INPUT_DIR"/*.svg; do
    if [ -f "$SVG" ]; then
        BASE=$(basename "$SVG" .svg)
        PNG="${OUTPUT_DIR}/${BASE}.png"
        if [ -z "$MARGIN" ]; then
            rsvg-convert -a "$SVG" -o "$PNG" -z "$ZOOM"
        else
            rsvg-convert -a "$SVG" -z "$ZOOM" | convert png:- -bordercolor none -border "${MARGIN}x${MARGIN}" "$PNG"
        fi
    fi
done
