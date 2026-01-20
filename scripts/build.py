from pathlib import Path

SRC_FILE = Path("src/my_class.list")
DST_FILE = Path("Remot_class.list")

output = []

for line in SRC_FILE.read_text(encoding="utf-8").splitlines():
    s = line.strip()
    if not s:
        continue
    if s.startswith("#") or s.startswith(";"):
        continue
    output.append(s)

DST_FILE.write_text("\n".join(output) + "\n", encoding="utf-8")
