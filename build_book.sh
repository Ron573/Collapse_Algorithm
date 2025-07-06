#!/bin/zsh
# Build the Collapse Algorithm PDF
pdflatex Collapse_Algorithm_final_main.tex
biber Collapse_Algorithm_final_main
pdflatex Collapse_Algorithm_final_main.tex
pdflatex Collapse_Algorithm_final_main.tex
echo "✅ Build complete. Output PDF: Collapse_Algorithm_final_main.pdf"

