#!/bin/zsh

echo "🧹 Starting cleanup of collapse_algorithm_book directory..."

# 1. Delete macOS + LaTeX log/artifact files
echo "🔸 Removing LaTeX and system junk..."
rm -f .DS_Store texput.log x.log
rm -f Collapse_Algorithm_Main.aux Collapse_Algorithm_Main.log Collapse_Algorithm_Main.out Collapse_Algorithm_Main.toc

# 2. Delete extracted zip clone (redundant)
echo "🔸 Removing unzipped_v2 mirror..."
rm -rf unzipped_v2

# 3. Delete web clutter directory
echo "🔸 Removing browser screenshot artifacts..."
rm -rf "cannas sreenshot from Final Book Compliation chat_files"

# 4. Create legacy folder and archive old chapter fragments
echo "🔸 Archiving legacy chapters..."
mkdir -p legacy_chapters
mv chapters/*.md chapters/*.txt chapters/*.csv legacy_chapters/ 2>/dev/null

# 5. Verify what's left
echo "✅ Cleanup complete. Final contents:"
find . -maxdepth 2 -type f | sort

echo "🧼 All clear. Proceed with build or versioning."

