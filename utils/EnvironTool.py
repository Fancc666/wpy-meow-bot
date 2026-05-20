from dotenv import dotenv_values
from pathlib import Path
import os

# 环境变量统一管理
config = {
    **dotenv_values(Path(__file__).parent.parent / '.env'),
    **os.environ
}

# 加载提示词
with open(Path(__file__).parent.parent / (config.get("PROMPT_FILE") or "prompt.md")) as f:
    config["PROMPT_TEXT"] = f.read()

if __name__ == "__main__":
    # print(config)
    ...
