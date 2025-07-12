#!/bin/zsh

# Go to your working directory
cd ~/Documents/collapse_algorithm_book || {
  echo "Directory not found"; exit 1
}

# Make revisions_3 structure
mkdir -p revisions_3/{chapters,front_matter,back_matter,assets,notes,build}

# Unzip the corrected starter bundle into revisions_3
unzip -o revisions_3_starter_bundle_v3.1_split_ch11.zip -d revisions_3/

# Confirm structure
echo "\n✅ Directory structure created:"
tree -L 2 revisions_3

echo "\n✅ Now move your chapter files (e.g., chapter_1_erasure.tex) into revisions_3/chapters/"
echo "Then run:"
echo "  cd ~/Documents/collapse_algorithm_book/revisions_3"
echo "  chmod +x build.sh"
echo "  ./build.sh"

