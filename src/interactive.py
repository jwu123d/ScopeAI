import cv2
import numpy as np
import pyautogui
import time
from algorithms.edge_detection import auto_canny, post_process
from api.openai_api import analyze_roi_with_openai
from utils.draw_utils import draw_text_bubble
from config import *


mouse_x, mouse_y = 0, 0
last_result = ""
last_analysis_time = 0
bubble_alpha = 0.0
canny_threshold = 60  # 默认的 Canny 阈值
canny_multiplier = 2    # 默认的 Canny upperbound 倍率


# 变量初始化
mouse_x, mouse_y = 0, 0
last_result = "Hover & press 's' to analyze"
last_analysis_time = 0
bubble_alpha = 0.0
language = "en"

def detect_edge_interactive(image_path, rect_size=200, edge_color=(255, 255, 255), alpha=1):
    """交互式鼠标边缘检测 + GPT-4o 分析 + 鼠标旁边显示结果（仅在按 's' 后短暂显示，带动画）
       添加滚轮缩放检测区域，修复 global 变量冲突
       增加键盘 I/D 调整 canny_threshold
    """
    global mouse_x, mouse_y, last_result, last_analysis_time, bubble_alpha, canny_threshold, canny_multiplier, language

    # 读取原始图像
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("无法读取图像文件")

    # 获取原始尺寸
    original_h, original_w = img.shape[:2]
    screen_width, screen_height = 1200, 800  # 设定屏幕大小（可以根据需求调整）
    
    # 计算缩放比例，确保图片不会超出屏幕
    scale_factor = min(screen_width / original_w, screen_height / original_h, 1.0)  
    new_w, new_h = int(original_w * scale_factor), int(original_h * scale_factor)

    # 调整图像大小
    img = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 统一格式

    # 计算鼠标交互的缩放比例（适配缩放后的图片）
    mouse_scale_x = original_w / new_w
    mouse_scale_y = original_h / new_h

    # 创建窗口
    cv2.namedWindow("Smart Vision Analyzer", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Smart Vision Analyzer", new_w, new_h)  

    result_display_time = 3  # 结果显示时间（秒）

    def mouse_callback(event, x, y, flags, param):
        """更新鼠标位置，监听滚轮调整 `rect_size`"""
        nonlocal rect_size  

        if event == cv2.EVENT_MOUSEMOVE:
            global mouse_x, mouse_y
            mouse_x, mouse_y = x, y

        elif event == cv2.EVENT_MOUSEWHEEL:
            if flags > 0:  
                rect_size = min(rect_size + 20, min(original_h, original_w))  
            else:  
                rect_size = max(rect_size - 20, 50)  

    cv2.setMouseCallback("Smart Vision Analyzer", mouse_callback)

    while True:
        result = img.copy()
        half_size = rect_size // 2
        x1, y1 = max(0, int(mouse_x * mouse_scale_x) - half_size), max(0, int(mouse_y * mouse_scale_y) - half_size)
        x2, y2 = min(original_w, x1 + rect_size), min(original_h, y1 + rect_size)

        roi = cv2.resize(img, (original_w, original_h))[y1:y2, x1:x2]  
        if roi.size == 0:
            continue

        gray_roi = cv2.cvtColor(roi, cv2.COLOR_RGB2GRAY)
        edges = auto_canny(gray_roi)
        edges = post_process(edges) 

        overlay = np.zeros_like(img)

        y1_resized, y2_resized = int(y1 / mouse_scale_y), int(y2 / mouse_scale_y)
        x1_resized, x2_resized = int(x1 / mouse_scale_x), int(x2 / mouse_scale_x)

        overlay_h, overlay_w = y2_resized - y1_resized, x2_resized - x1_resized

        if edges.shape[:2] != (overlay_h, overlay_w):
            edges = cv2.resize(edges, (overlay_w, overlay_h), interpolation=cv2.INTER_NEAREST)

        overlay[y1_resized:y2_resized, x1_resized:x2_resized][edges > 0] = edge_color
        result = cv2.addWeighted(result, 1, overlay, alpha, 0)

        time_since_analysis = time.time() - last_analysis_time
        if time_since_analysis <= result_display_time:
            bubble_alpha = min(1.0, bubble_alpha + 0.1)  
        else:
            bubble_alpha = max(0.0, bubble_alpha - 0.1)  

        if bubble_alpha > 0:
            result = draw_text_bubble(result, last_result, mouse_x, mouse_y, bubble_alpha)

        # 显示 Canny 阈值信息
        cv2.putText(result, f"Threshold: {canny_threshold} Language: {language} | Scroll to resize | 's' to analyze | 'q' to quit",
                    (20, new_h - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

        cv2.imshow("Smart Vision Analyzer", cv2.cvtColor(result, cv2.COLOR_RGB2BGR))

        key = cv2.waitKey(30)  
        if key == ord('q'):
            break
        elif key == ord('s'):
            if roi.size > 0:
                last_result = "分析中..."
                cv2.imshow("Smart Vision Analyzer", cv2.cvtColor(result, cv2.COLOR_RGB2BGR))  
                cv2.waitKey(1)  
                last_result = analyze_roi_with_openai(roi, language)
                last_result = last_result[:20]  
                last_analysis_time = time.time()  
                bubble_alpha = 0.1  
        elif key == ord('i'):  
            canny_threshold = min(canny_threshold + 10, 255)  
        elif key == ord('d'):  
            canny_threshold = max(canny_threshold - 10, 10)  
        elif key == ord('f'):  
            canny_multiplier = max(canny_multiplier - 0.1, 1)
        elif key == ord('g'):  
            canny_multiplier = min(canny_multiplier + 0.1, 5) 
        elif key == ord('z'): 
            language = "zh"
        elif key == ord('e'): 
            language = "en" 