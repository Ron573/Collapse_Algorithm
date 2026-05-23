#!/bin/zsh

echo "🧽 Cleaning inline # comments inside code blocks..."

for texfile in *.tex; do
  tmpfile="${texfile}.cleaned"
  awk '
    BEGIN { inCode=0; }
    /^\s*\\begin{lstlisting}/ { inCode=1; print; next }
    /^\s*\\end{lstlisting}/   { inCode=0; print; next }
    {
      if (inCode == 1) {
        if ($0 ~ /#/) {
          comment = substr($0, index($0, "#"))
          code = substr($0, 1, index($0, "#") - 1)
          gsub(/[ \t]+$/, "", code)
          print code
          print "% " comment
        } else {
          print
        }
      } else {
        print
      }
    }
  ' "$texfile" > "$tmpfile" && mv "$tmpfile" "$texfile"
done

echo "✅ All inline # comments moved outside code blocks."

