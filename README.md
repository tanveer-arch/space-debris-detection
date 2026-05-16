<div align="center">

# 🛰️ Space Debris Detection & Risk Assessment

**A YOLOv8-powered deep learning system for detecting space debris and satellites in orbital imagery — with real-time collision risk assessment.**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-FF4081?style=flat&logo=pytorch&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

</div>

---

## 📌 Overview

Space debris poses a significant risk to operational satellites and future space missions. This project uses **YOLOv8 object detection** trained on orbital imagery to identify and classify **Satellites** and **Debris** in real time, and assess the **collision risk level** based on detected debris count.

The project includes a **Streamlit web application** for easy image upload and visualization, along with the complete training notebook used to develop the model.

---

## 🎯 Key Features

| Feature | Description |
|---|---|
| 🛸 **Object Detection** | Detects Satellites and Debris using YOLOv8 |
| 🎨 **Confidence Tiers** | Color-coded bounding boxes (🟢 High ≥ 0.80 / 🟡 Medium 0.50–0.80 / 🔴 Low < 0.50) |
| 📊 **Risk Assessment** | Collision risk score: LOW / MEDIUM / HIGH based on debris count |
| ⚙️ **Adjustable Threshold** | Sidebar slider to control detection confidence |
| ⚡ **Fast Inference** | FP16 half-precision model for faster predictions |
| 🖥️ **Web Interface** | Clean Streamlit UI — no coding required to use |

---

## 🧠 Model Performance

> Trained for **30 epochs** on orbital imagery dataset using **YOLOv8 (Ultralytics v8.4.27)**

| Metric | Score |
|---|---|
| **Precision** | 0.930 |
| **Recall** | 0.926 |
| **mAP@50** | 0.931 |
| **mAP@50-95** | 0.750 |
| **Image Size** | 640 × 640 |
| **Classes** | Satellite, Debris |
| **Precision (Storage)** | FP16 (Half) |

---

## 📦 Project Structure

```
space-debris-detection/
├── app.py                    # Streamlit web application
├── space_debris_v2-1.ipynb   # Model training & experimentation notebook
├── requirements.txt          # Python dependencies
├── .gitignore
└── README.md
```

> ⚠️ `best.pt` (model weights) is **not** included in the repo due to file size.
> Download it from the [**Releases**](../../releases) section below.

---

## ⬇️ Download Model Weights

The trained YOLOv8 model (`best.pt`) is available as a release asset:

1. Go to [**Releases →**](../../releases)
2. Download `best.pt` from the latest release
3. Place it in the **root directory** of this project (same folder as `app.py`)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/tanveer-arch/space-debris-detection.git
cd space-debris-detection
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Download the model

Download `best.pt` from [Releases](../../releases) and place it in the project root.

### 4. Run the app

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501` and upload an orbital image to get started!

---

## 🖼️ How It Works

```
Upload Image  →  YOLOv8 Inference  →  Draw Bounding Boxes  →  Risk Assessment
    ↓                  ↓                       ↓                      ↓
 JPG/PNG          best.pt model         Color by confidence      LOW / MEDIUM / HIGH
```

**Risk Levels:**
- 🟢 **LOW** — 0–2 debris objects detected
- 🟡 **MEDIUM** — 3–5 debris objects detected
- 🔴 **HIGH** — More than 5 debris objects detected

---

## ⚙️ Requirements

```
streamlit>=1.32.0
ultralytics>=8.0.0
opencv-python-headless>=4.9.0
numpy>=1.24.0
torch>=2.0.0
torchvision>=0.15.0
```

---

## 👨‍💻 Author

**Tanveer** — CS Student @ Nirma University, Ahmedabad
Interests: Deep Learning · Computer Vision · Space Technology

🔗 [GitHub Profile](https://github.com/tanveer-arch)

---

<div align="center">
⭐ If you found this project helpful, consider giving it a star!
</div>
