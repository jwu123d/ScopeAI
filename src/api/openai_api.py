import requests
import base64
import cv2
import time
import json
from config import OPENAI_API_KEY, OPENAI_API_ENDPOINT, ROI_SAVE_PATH

def analyze_roi_with_openai(image, language="en"):
    """调用 OpenAI GPT-4o Vision 分析鼠标区域"""
    try:
        time.sleep(1)
        image_path = str(ROI_SAVE_PATH)
        cv2.imwrite(image_path, image)
        
        with open(image_path, "rb") as f:
            image_data = f.read()

        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}"
        }
        
        prompt_texts = {
            "zh": "请仅列出图片中出现的主要物体名称，每个名词最多只可加一个修饰词，例如：'桌子, 浅色木头的椅子, 爱因斯坦的书, 笔'。",
            "en": "Please list only the main objects appearing in the image. Each noun can have at most one modifier, e.g., 'table, light wooden chair, Einstein's book, pen'."
        }

        if language not in prompt_texts:
            language = "en"  # 默认中文

        payload = {
            "model": "gpt-4o",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt_texts[language]},
                        {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64," + base64.b64encode(image_data).decode("utf-8")}}
                    ]
                }
            ],
            "max_tokens": 500
        }

        for attempt in range(5):  
            response = requests.post(OPENAI_API_ENDPOINT, headers=headers, json=payload)
            if response.status_code == 429:
                wait_time = 2 ** attempt  
                print(f"API 限制，等待 {wait_time} 秒后重试...")
                time.sleep(wait_time)
            else:
                response.raise_for_status()
                break

        result = response.json()["choices"][0]["message"]["content"]
        return result.strip()

    except Exception as e:
        return f"API Error: {str(e)}"
    finally:
        if ROI_SAVE_PATH.exists():
            ROI_SAVE_PATH.unlink()
