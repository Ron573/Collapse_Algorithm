#!/bin/bash

# Script: md_to_tex_converter.sh
# Converts all .md files in the current folder to .tex using pandoc

echo "Starting Markdown-to-LaTeX conversion..."

for file in *.md; do
  if [[ -f "$file" ]]; then
    filename="${file%.md}"
    pandoc "$file" -o "${filename}.tex"
    echo "Converted: $file → ${filename}.tex"
  fi
done

echo "Conversion complete."

