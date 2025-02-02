import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from config import FONT_PATH, FONT_SIZE

# 加载字体
font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

def draw_text_bubble(image, text, x, y, alpha):
    """绘制气泡文本"""
    pil_img = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_img)

    text_size = draw.textbbox((0, 0), text, font=font)
    text_w, text_h = text_size[2] - text_size[0], text_size[3] - text_size[1]

    bubble_w, bubble_h = text_w + 20, text_h + 20
    padding = 10

    x_offset, y_offset = 15, 30
    x1 = min(x + x_offset, image.shape[1] - bubble_w - padding)
    y1 = min(y + y_offset, image.shape[0] - bubble_h - padding)
    x2, y2 = x1 + bubble_w, y1 + bubble_h

    overlay = Image.new("RGBA", pil_img.size, (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)

    fill_color = (50, 50, 50, int(alpha * 255))
    overlay_draw.rectangle([x1, y1, x2, y2], fill=fill_color, outline=(255, 255, 255, int(alpha * 255)))

    text_fill = (255, 255, 255, int(alpha * 255))
    overlay_draw.text((x1 + 10, y1 + 10), text, font=font, fill=text_fill)

    pil_img = Image.alpha_composite(pil_img.convert("RGBA"), overlay).convert("RGB")

    return cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
