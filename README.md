# 🛰️ Space Debris Detection & Risk Assessment

A YOLOv8-based deep learning application to detect **space debris and satellites** in orbital images and assess **collision risk** in real time.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLOv8-FF4081?style=flat&logo=pytorch&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white)

---

## 🚀 Demo

Run the Streamlit app locally:
```bash
streamlit run app.py
```

---

## 📦 Download Model Weights

The trained YOLOv8 model (`best.pt`) is available in the [**GitHub Releases**](../../releases) section.

1. Go to [Releases](../../releases)
2. Download `best.pt`
3. Place it in the **root directory** of this project (same folder as `app.py`)

---

## 🗂️ Project Structure

```
space-debris-detection/
├── app.py                    # Streamlit web app
├── space_debris_v2-1.ipynb   # Training & experimentation notebook
├── requirements.txt          # Python dependencies
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

```bash
# Clone the repo
git clone https://github.com/tanveer-arch/space-debris-detection.git
cd space-debris-detection

# Install dependencies
pip install -r requirements.txt

# Download best.pt from Releases and place it here
# Then run:
streamlit run app.py
```

---

## 🔍 Features

- 🛸 Detects **Satellites** and **Debris** in uploaded orbital images
- 🎯 Adjustable **confidence threshold** via sidebar slider
- 🟢🟡🔴 **Confidence tier coloring** on bounding boxes (High / Medium / Low)
- 📊 Real-time **collision risk assessment** (LOW / MEDIUM / HIGH)
- ⚡ Powered by **YOLOv8** (Ultralytics) and **Streamlit**

---

## 🧠 Model

| Property | Detail |
|---|---|
| Architecture | YOLOv8 |
| Classes | Satellite, Debris |
| Framework | Ultralytics + PyTorch |
| Weights file | `best.pt` (via Releases) |

---

## 👨‍💻 Author

**Tanveer** — [github.com/tanveer-arch](https://github.com/tanveer-arch)  
CS Student @ Nirma University, Ahmedabad  
Interests: Deep Learning, Computer Vision, Space Technology
