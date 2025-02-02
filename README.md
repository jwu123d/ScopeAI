# ScopeAI

**A locally-run image recognition tool that integrates visualization algorithms with the GPT-4o API to enable object scanning and information display, with future scalability to AR/VR applications.**

---

## 📌 Project Overview

ScopeAI is a locally-run intelligent image recognition tool designed to provide an "object scanning" experience through the following core functionalities:
1. **Preprocessing Algorithms**: Simulates the "scanning" process using techniques like Canny edge detection and Total Variation (TV) denoising.
2. **Object Recognition**: Utilizes the GPT-4o API to analyze image content and return object descriptions (e.g., "light-colored table").
3. **Visual Interaction**: Displays information bubbles near identified objects, with future support for AR/VR devices such as Apple Vision Pro.
4. **Scalability**: Includes reserved interfaces for facial recognition, multimodal interaction, and other "spy-like" capabilities.

---

## 🚀 Core Features

### 1. Real-Time Scanning Simulation
- **Canny Edge Detection**: Dynamically displays the edge extraction process to enhance the "scanning" visual effect.
- **TV Denoising Algorithm**: Replaces traditional anisotropic diffusion to optimize image quality and reduce noise interference.

### 2. GPT-4o Object Recognition
- Calls the OpenAI API to analyze images and return natural language descriptions (e.g., material, usage).
- Supports contextual association (e.g., "light-colored table" may be linked to "IKEA furniture style").

### 3. Interactive Information Display
- Generates pop-up bubbles next to recognized objects to display key information.
- Future expansion to HUD interfaces for AR glasses or VR headsets.

---

## 📦 Installation & Execution

### Prerequisites
- Python 3.8+
- OpenAI API key ([Get yours here](https://platform.openai.com/api-keys))

---

## 🔧 Tech Stack

| Module          | Technology Used                                                      |
|----------------|----------------------------------------------------------------------|
| **Image Processing** | OpenCV (Canny edge detection), SciPy (Total Variation denoising)  |
| **AI Integration** | GPT-4o API, Custom prompt engineering for optimized output        |
| **Visualization** | PyQt5 or OpenGL (future AR/VR compatibility)                        |
| **Deployment**   | Poetry for dependency management, Docker for containerization (future expansion) |

---

## 🌟 Future Roadmap

### Short-Term Enhancements
- [ ] Support for simultaneous multi-object recognition and relationship inference
- [ ] Integration of a facial recognition module (using dlib or MediaPipe)
- [ ] Export scan records to Markdown/CSV

### Long-Term Vision
- **AR/VR Integration**: Adaptation for devices such as Apple Vision Pro and Meta Quest
- **Multimodal Interaction**: Voice command scanning and gesture-based target selection
- **Security Enhancement**: Liveness detection to prevent photo spoofing (in conjunction with facial recognition)

---

## 🤝 Contribution Guide

Contributions are welcome! Recommended areas:
- Optimizing the real-time performance of the TV denoising algorithm
- Developing plugins for Unity/Unreal Engine
- Enhancing scanning animations (e.g., particle effects)

---

## 📜 License

MIT License - See [LICENSE](LICENSE) for details.

---

## 📧 Contact

For collaboration or technical inquiries, please reach out to:  
[juw049@ucsd.edu](mailto:juw049@ucsd.edu)

---

### Suggested File Structure
```
ScopeAI/
├── docs/               # Demo GIFs/screenshots
├── samples/            # Sample test images
├── src/                # Core code
│   ├── algorithms/     # Canny/TV algorithm implementation
│   └── api/            # GPT-4o interaction module
├── requirements.txt
├── main.py
└── README.md
```

