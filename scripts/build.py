from pathlib import Path
from datetime import datetime

SRC_FILE = Path("src/my_class.list")

DST_FILES = {
    "DIRECT": Path("my_Remot_rule_DIRECT.list"),
    "REJECT": Path("my_Remot_rule_REJECT.list"),
    "PROXY": Path("my_Remot_rule_PROXY.list")
}

output = {k: [] for k in DST_FILES}

for line in SRC_FILE.read_text(encoding="utf-8").splitlines():
    s = line.strip()
    if not s or s.startswith("#") or s.startswith(";"):
        continue

    parts = s.split(",")
    # 如果至少有三列，则第三列是策略
    if len(parts) >= 3:
        policy_upper = parts[2].strip().upper()
        if policy_upper not in ["DIRECT", "REJECT"]:
            policy_upper = "PROXY"
    else:
        policy_upper = "PROXY"

    output[policy_upper].append(s)

# 写入三个文件
for policy, dst_file in DST_FILES.items():
    header = [
        f"# 自动生成文件: {dst_file.name}",
        f"# 来源: src/my_rule.list",
        f"# Generated at {datetime.utcnow().isoformat()} UTC",
        "# 无注释规则，直接使用"
    ]
    dst_file.write_text("\n".join(header + output[policy]) + "\n", encoding="utf-8")
    print(f"[OK] Generated {dst_file} ({len(output[policy])} rules)")
