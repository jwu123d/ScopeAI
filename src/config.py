import os
from dotenv import load_dotenv
from pathlib import Path

# 加载环境变量
load_dotenv()

# 读取 OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY is None:
    raise ValueError("API key not found! Set OPENAI_API_KEY environment variable.")

# OpenAI API 端点
OPENAI_API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

# 其他配置信息
ROI_SAVE_PATH = Path("temp_roi.jpg")
FONT_PATH = "assets/font/DouyinSansBold.ttf"  # 需要替换为你的字体路径
FONT_SIZE = 24