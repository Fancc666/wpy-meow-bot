from dotenv import dotenv_values
from pathlib import Path

config = dotenv_values(Path(__file__).parent.parent / '.env')  # 返回字典

# 加载提示词
with open(Path(__file__).parent.parent / (config.get("PROMPT_FILE") or "prompt.md")) as f:
    config["PROMPT_TEXT"] = f.read()
