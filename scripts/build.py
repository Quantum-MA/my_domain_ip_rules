from pathlib import Path
from datetime import datetime

SRC_FILE = Path("src/my_rule.list")

# 输出文件
DST_FILES = {
    "DIRECT": Path("my_Remot_rule_DIRECT.list"),
    "REJECT": Path("my_Remot_rule_REJECT.list"),
    "PROXY": Path("my_Remot_rule_PROXY.list")
}

# 初始化存放规则的列表
output = {
    "DIRECT": [],
    "REJECT": [],
    "PROXY": []
}

# 读取源文件并分组
for line in SRC_FILE.read_text(encoding="utf-8").splitlines():
    s = line.strip()
    if not s:
        continue
    if s.startswith("#") or s.startswith(";"):
        continue
    # 取最后一段逗号分割的策略字段
    parts = s.rsplit(",", 1)
    if len(parts) != 2:
        continue
    rule, policy = parts
    policy_upper = policy.strip().upper()
    if policy_upper not in output:
        policy_upper = "PROXY"  # 默认策略归为 PROXY
    output[policy_upper].append(s)

# 添加文件头并写入
for policy, dst_file in DST_FILES.items():
    header = [
        f"# 自动生成文件: {dst_file.name}",
        f"# 来源: src/my_rule.list",
        f"# Generated at {datetime.utcnow().isoformat()} UTC",
        "# 无注释规则，直接使用"
    ]
    dst_file.write_text("\n".join(header + output[policy]) + "\n", encoding="utf-8")
    print(f"[OK] Generated {dst_file} ({len(output[policy])} rules)")
