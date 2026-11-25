"""Write the make.fun competition entry as UTF-8 text to /output/entry.txt.

The output directory is taken from MAKEFUN_OUTPUT_DIR when set and non-empty,
otherwise it defaults to /output. Standard library only.
"""
import os
import sys

TEXT = "fix: added retry. It retries the bug now, at scale.\n"

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
try:
    os.makedirs(output_dir, exist_ok=True)
except OSError as exc:
    print(f"error: cannot create output directory {output_dir!r}: {exc}", file=sys.stderr)
    raise SystemExit(1)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
