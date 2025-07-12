# Collapse Algorithm – Book Flaps and Covers

This folder contains the finalized assets for the print-ready **Collapse Algorithm** book cover flaps, formatted in LaTeX for compilation in TeXShop.

## 📁 Contents

### 1. `author_bio_flap.tex` → `author_bio_flap.pdf`
A professionally formatted author biography flap featuring:
- Ronald J. Botelho, MS
- Former Counterintelligence Special Agent and Psychological Warfare Specialist
- Includes a formal headshot (`RonB_author_photo.png`)

> _"If the soul is left in darkness, sins will be committed. The guilty one is not he who sins, but the one who causes the darkness."_  
—Victor Hugo, quoted in Mary L. Trump, *Too Much and Never Enough* (2020)

### 2. `front_flap_quote.tex` → `front_flap_quote.pdf`
A front flap designed to introduce the **Collapse Algorithm** without duplicating the preface or abstract.

Includes space for:
- A quote or guiding statement
- Contextual setup for the reader

### 3. `front_cover_final.png`
Final cover image with:
- "Collapse Algorithm"
- Subtitle or series label (e.g., “Final Edition” or “Ph.D. Series Volume I”)
- Optional promotional banner (e.g., “Based on 50+ published essays”)

### 4. `RonB_author_photo.png`
High-resolution author photograph, embedded in the bio flap.

---

## 🧾 Usage

Run `pdflatex` on either `.tex` file from this directory:

```bash
pdflatex author_bio_flap.tex
pdflatex front_flap_quote.tex
```

Ensure all assets (image files) are in the same directory.

---

## 📜 License and Attribution

© 2025 Ronald J. Botelho.  
All content and images are the property of the author. Redistribution is permitted only with written permission.  
Quote attribution: Mary L. Trump (2020), *Too Much and Never Enough*, Simon & Schuster.

---

## ✅ Status

✔️ Verified with TeXShop (macOS)  
✔️ Assets organized for GitHub push  
✔️ All PDFs compiled and tested

