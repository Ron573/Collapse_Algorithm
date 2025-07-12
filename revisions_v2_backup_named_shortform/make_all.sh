#!/bin/zsh

# Step 1: Convert all Markdown files in this directory and subfolders to LaTeX
echo "Converting all .md files to .tex..."
find . -name "*.md" | while read file; do
  base="${file%.md}"
  pandoc "$file" -o "${base}.tex" --standalone --wrap=preserve
done

# Step 2: Copy or update main TeX file if needed
echo "Compiling main LaTeX file..."
cd ~/Documents/collapse_algorithm_book/
pdflatex /Users/RonB/Documents/collapse_algorithm_book/revisions_v2/Collapse_Algorithm_Main.tex

