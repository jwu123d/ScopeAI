import cv2
import numpy as np
from skimage.restoration import denoise_tv_chambolle

def auto_canny(image, sigma=0.33):
    """自动计算 Canny 阈值并进行边缘检测"""
    v = np.median(image)
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    return cv2.Canny(image, lower, upper)

def post_process(edges):
    """使用形态学闭运算和 Total Variation (TV) 去噪"""
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
    closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
    
    denoised = denoise_tv_chambolle(closed.astype(float), weight=0.1)
    denoised = (denoised * 255).astype(np.uint8)
    
    return denoised
