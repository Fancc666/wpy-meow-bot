from dotenv import dotenv_values
from pathlib import Path

config = dotenv_values(Path(__file__).parent.parent / '.env')  # 返回字典
