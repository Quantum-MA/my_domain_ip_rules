from pathlib import Path
from datetime import datetime

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

header = [
    f"# 这是由 src/my_class.list自动生成的无注释list",
    f"# Generated at {datetime.utcnow().isoformat()} UTC",
    "# Do not edit manually; edit src/my_class.list instead"
]

DST_FILE.write_text("\n".join(header + output) + "\n", encoding="utf-8")

print(f"[OK] Generated {DST_FILE} ({len(output)} rules)")
