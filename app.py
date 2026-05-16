# app.py — Space Debris Detector
# Usage: streamlit run app.py
# Requires: best.pt in the same directory (download from GitHub Releases)

import streamlit as st
import cv2, numpy as np, tempfile, os
from ultralytics import YOLO

CLASS_NAMES = ["Satellite", "Debris"]
TIER_BGR = {"high": (0, 200, 0), "medium": (0, 165, 255), "low": (0, 0, 255)}

def tier(c):
    return "high" if c >= 0.80 else ("medium" if c >= 0.50 else "low")

def risk(n):
    return ("LOW", "🟢") if n <= 2 else (("MEDIUM", "🟡") if n <= 5 else ("HIGH", "🔴"))

@st.cache_resource
def load_model():
    return YOLO("best.pt")

st.set_page_config(page_title="Space Debris Detector", page_icon="🛰️", layout="wide")
st.title("🛰️ Space Debris Detection & Risk Assessment")
st.caption("Upload an orbital image to detect debris and assess collision risk.")

with st.sidebar:
    st.header("Settings")
    conf = st.slider("Confidence threshold", 0.10, 0.95, 0.50, 0.05)
    st.markdown("---")
    st.markdown("**Confidence tiers**")
    st.markdown("🟢 High >= 0.80")
    st.markdown("🟡 Medium 0.50–0.80")
    st.markdown("🔴 Low < 0.50")

up = st.file_uploader("Choose image", type=["jpg", "jpeg", "png"])

if up:
    model = load_model()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        tmp.write(up.read())
        path = tmp.name

    res = model.predict(source=path, conf=conf, save=False, verbose=False)[0]
    img = cv2.imread(path)
    nd = ns = 0

    if res.boxes is not None:
        for box in res.boxes:
            cid = int(box.cls[0])
            c_ = float(box.conf[0])
            t = tier(c_)
            col = TIER_BGR[t]
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            cv2.rectangle(img, (x1, y1), (x2, y2), col, 2)
            cv2.putText(img, f"{CLASS_NAMES[cid]} {c_:.2f}",
                        (x1, max(y1 - 6, 12)), cv2.FONT_HERSHEY_SIMPLEX, 0.42, col, 2)
            if cid == 1:
                nd += 1
            else:
                ns += 1

    rl, icon = risk(nd)
    c1, c2 = st.columns([3, 1])
    with c1:
        st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="Detection result", use_column_width=True)
    with c2:
        st.metric("Debris", nd)
        st.metric("Satellites", ns)
        rc = {"LOW": "green", "MEDIUM": "orange", "HIGH": "red"}[rl]
        st.markdown("### Risk Level")
        st.markdown(f"<span style='color:{rc}; font-size:1.5em'>{icon} {rl}</span>", unsafe_allow_html=True)

    os.unlink(path)
