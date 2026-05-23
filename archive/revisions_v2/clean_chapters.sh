#!/bin/bash

echo "Cleaning chapter files..."

for file in chapter_*.tex chapter_??_v*.tex chapter_*_v*.tex; do
    # Skip if file doesn't exist
    [[ -f "$file" ]] || continue

    echo "Processing $file..."

    # Create a backup first
    cp "$file" "$file.bak"

    # Strip preamble and document commands
    sed -e '/\\documentclass/d' \
        -e '/\\usepackage/d' \
        -e '/\\begin{document}/d' \
        -e '/\\end{document}/d' \
        -e '/\\author{.*/d' \
        -e '/\\date{.*/d' \
        -e '1,/\\\(chapter\|section\){/!d' \
        "$file.bak" > "$file"
done

echo "Cleanup complete. Backups saved as *.bak"

