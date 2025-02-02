# ScopeAI

**一个本地运行的图像识别工具，结合可视化算法与GPT-4o API，实现物体扫描与信息展示，未来可扩展至AR/VR场景。**

---

## 📌 项目概述

ScopeAI 是一个本地运行的智能图像识别工具，通过以下核心功能实现“物体扫描”体验：
1. **预处理算法**：使用 Canny 边缘检测、Total Variation (TV) 去噪等技术模拟“扫描”过程。
2. **物体识别**：通过 GPT-4o API 分析图像内容，返回物体信息（如“浅色桌子”）。
3. **可视化交互**：在物体旁显示信息气泡，支持未来集成 AR/VR 设备（如 Apple Vision Pro）。
4. **可扩展性**：预留接口支持人脸识别、多模态交互等“007特工”式功能。

---

## 🚀 核心功能

### 1. 实时扫描模拟
- **Canny 边缘检测**：动态显示边缘提取过程，增强“扫描”视觉效果。
- **TV 去噪算法**：替代传统各向异性扩散，优化图像质量并减少噪声干扰。

### 2. GPT-4o 物体识别
- 调用 OpenAI API 分析图像，返回自然语言描述（如材质、用途）。
- 支持上下文联想（例如：“浅色桌子”可能关联“宜家家具风格”）。

### 3. 交互式信息展示
- 在识别物体旁生成气泡弹窗，显示关键信息。
- 未来可扩展至 AR 眼镜或 VR 头显的 HUD 界面。

---

## 📦 安装与运行

### 前置条件
- Python 3.8+
- OpenAI API 密钥（[获取地址](https://platform.openai.com/api-keys)）

## 🔧 技术栈

| 模块           | 技术选型                                                                 |
|----------------|-------------------------------------------------------------------------|
| **图像处理**   | OpenCV (Canny边缘检测), SciPy (Total Variation 去噪)                   |
| **AI 集成**    | GPT-4o API, 自定义prompt工程优化输出                                   |
| **可视化**     | PyQt5 或 OpenGL（未来AR/VR兼容）                                       |
| **部署**       | Poetry 依赖管理, Docker 容器化（未来扩展）                             |

---

## 🌟 未来规划

### 短期迭代
- [ ] 支持多物体同时识别与关系推理
- [ ] 添加人脸识别模块（基于 dlib 或 MediaPipe）
- [ ] 导出扫描记录到 Markdown/CSV

### 长期愿景
- **AR/VR 整合**：适配 Apple Vision Pro、Meta Quest 等设备 SDK
- **多模态交互**：语音指令控制扫描，手势识别选择目标
- **安全增强**：活体检测防止照片欺骗（配合人脸识别）

---

## 🤝 贡献指南

欢迎提交 PR！推荐方向：
- 优化 TV 去噪算法的实时性能
- 开发 Unity/Unreal Engine 插件
- 增加更多扫描动画效果（如粒子特效）

---

## 📜 许可证

MIT License - 详见 [LICENSE](LICENSE)

---

## 📧 联系

如有合作意向或技术问题，请联系：  
[juw049@ucsd.edu](mailto:juw049@ucsd.edu)

---

### 文件结构建议
```
ScopeAI/
├── docs/               # 存放演示GIF/截图
├── samples/            # 示例测试图片
├── src/                # 核心代码
│   ├── algorithms/     # Canny/TV 算法实现
│   └── api/            # GPT-4o 交互模块
├── requirements.txt
├── main.py
└── README.md
