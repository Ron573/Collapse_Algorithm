# Repository Cleanup Plan

## Current diagnosis

The repository contains a working manuscript structure, but it also includes large media archives, duplicate revision bundles, old TeX entry files, screenshots, notes, and generated/support folders.

Largest issue:
- media_archive: 1.5G

Likely cleanup targets:
- media_archive/
- revisions_v2*/
- revisions_3*/
- collapse_algorithm_structure*/
- Images/ versus assets/
- README.html
- duplicate main TeX files
- SSH key
- notes PDF export folders

## Proposed stable structure

- README.md
- LICENSE
- main.tex
- chapters/
- appendices/
- front_matter/
- back_matter/
- assets/figures/
- data/
- code/
- docs/
- archive/

## Rule

Do not delete historical material until it has been moved into archive/ or backed up externally.
