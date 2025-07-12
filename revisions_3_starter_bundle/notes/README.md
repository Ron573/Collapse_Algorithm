# Collapse Algorithm – revisions_3

This directory is the new working structure for finalizing your manuscript.

## Structure

- `chapters/` – Full individual chapter `.tex` files (1–15)
- `front_matter/` – Preface, acknowledgments, quotes
- `back_matter/` – Bibliography `.bib`, license, appendices
- `assets/` – Images and figures (.png, .jpg)
- `build/` – Compiled outputs (PDF, TOC, LOG)
- `notes/` – Planning notes, drafts, README

## Compile Instructions

Use the provided `build.sh` to compile:

```bash
chmod +x build.sh
./build.sh
```

Requires: `pdflatex` and `biber` installed.

## Citation Format

- In-line: APA 7th edition `(Author, Year)`
- Footnotes: Optional for drafts
- Bibliography: Printed at end via `biblatex` + `biber`