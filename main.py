import os

TEXT = "fix: added retry. It retries the bug now, at scale.\n"

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
