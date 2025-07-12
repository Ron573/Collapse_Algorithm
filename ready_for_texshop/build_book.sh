#!/bin/bash

# Set file names
TEXFILE="Collapse_Algorithm_final_main"
BIBFILE="references/collapse_algorithm_refs.bib"

# Run LaTeX → BibLaTeX → LaTeX x2
pdflatex "$TEXFILE.tex"
biber "$TEXFILE"
pdflatex "$TEXFILE.tex"
pdflatex "$TEXFILE.tex"

# Notify
echo "✅ Build complete. PDF output generated."

