<a href="README.md?lang=en">
  <img src="https://img.shields.io/badge/English-007ACC?style=for-the-badge&logo=googletranslate" align="right">
</a>
<a href="README.md?lang=zh">
  <img src="https://img.shields.io/badge/简体中文-4CAF50?style=for-the-badge&logo=googletranslate" align="right">
</a>

<div id="zh" style="display: block;">

<!-- 中文内容 -->
# ScopeAI 
**一个本地运行的图像识别工具，结合可视化算法与GPT-4o API，实现物体扫描与信息展示**

---

## 🚀 核心功能
- **实时扫描模拟**：Canny 边缘检测 + TV 去噪
- **GPT-4o 物体识别**：返回自然语言描述
- **AR/VR 兼容**：未来支持 Apple Vision Pro

</div>

<div id="en" style="display: none;">

<!-- 英文内容 -->
# ScopeAI 
**A local image recognition tool with visualization algorithms and GPT-4o API integration**

---

## 🚀 Key Features
- **Real-time Scanning Simulation**: Canny Edge Detection + TV Denoising
- **GPT-4o Object Recognition**: Natural language descriptions
- **AR/VR Ready**: Future support for Apple Vision Pro

</div>

<!-- 自动切换脚本 -->
<script>
// 通过 URL 参数控制显示
const langParam = new URLSearchParams(window.location.search).get('lang');
if (langParam === 'en') {
  document.getElementById('zh').style.display = 'none';
  document.getElementById('en').style.display = 'block';
} else {
  document.getElementById('en').style.display = 'none';
}
</script>

---

## 🔧 技术栈 | Tech Stack

| 模块/Module       | 技术选型/Technologies Used                     |
|------------------|-----------------------------------------------|
| 图像处理/Image    | OpenCV, SciPy                                 |
| AI 集成/AI        | GPT-4o API                                    |
| 可视化/Visualization | PyQt5                                        |

---

## 🌟 未来规划 | Roadmap

### 短期/Short-term
- [ ] 多物体识别 | Multi-object recognition
- [ ] AR 原型开发 | AR prototype development

### 长期/Long-term
- **Apple Vision Pro 集成** | Apple Vision Pro Integration
- **手势控制** | Gesture Control

---

## 📧 联系 | Contact

[contact@scopeai.com](mailto:contact@scopeai.com)  
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?logo=twitter)](https://twitter.com/ScopeAI_Official)
