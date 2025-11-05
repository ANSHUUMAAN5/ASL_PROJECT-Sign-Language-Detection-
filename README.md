# ✌️ Sign Language Detection (A–Z, 0–9) — Real-Time | Deep Learning

A real-time Sign Language recognition system that detects **A–Z alphabets and 0–9 digits** from a webcam and converts them into text.

Built by **Anshuman Mathur** using Deep Learning + Computer Vision.

---

## 🧠 Tech Stack

| Component | Technology |
|---|---|
Model | MobileNetV2 (Transfer Learning)
Framework | TensorFlow / TensorFlow-Metal (Mac M-Series GPU)
Vision | OpenCV + MediaPipe
Language | Python
Input | Laptop Webcam

---

## 🚀 Features

✅ Real-time hand sign detection  
✅ Recognizes **A–Z** and **0–9**  
✅ Works on **Mac & Windows**  
✅ Train with your own images  
✅ Custom fine-tuning for accuracy  

---

✅ Replace ONLY the Folder Structure part with this:
## 📂 Project Folder Structure


```
ASL_PROJECT/
│
├── models/
│ ├── asl_model.h5
│ └── labels.json
│
├── scripts/
│ ├── realtime.py
│ ├── capture_images.py
│ └── train.py
│
├── requirements.txt
└── README.md
```

> ⚠️ YOU MUST create this dataset folder manually:



ASL_PROJECT/data/asl_dataset/


---

Inside `asl_dataset`, you must have:



a/ b/ c/ ... z/ 0/ 1/ ... 9/
---

## 📥 Download Dataset

Google Drive Dataset Link 👇  
👉 **((https://drive.google.com/file/d/1RVGx7QP0sXF_VVaME9N6bFoIjFn8niTb/view?usp=sharing))**

### Steps:

1. Download the zip  
2. Unzip → you will get `asl_dataset`  
3. Create folder: `ASL_PROJECT/data/`  
4. Move `asl_dataset` inside it  

✅ Final path must be:

ASL_PROJECT/data/asl_dataset/


---

## ⚙️ Installation Guide

### 🖥️ Mac (Intel / M1 / M2 / M3)

```bash
cd ASL_PROJECT
pip3 install -r requirements.txt
```
For Apple Silicon (M-series) GPU acceleration:
```
pip3 install tensorflow-macos tensorflow-metal
```

### 🪟 Windows
``` cd ASL_PROJECT
pip install -r requirements.txt
```


Note: MediaPipe works best with Python 3.10 on Windows

## 🎬 Run Live Recognition
python3 scripts/realtime.py

Controls
Key	Action
Space	Add space
D	Delete last character
Q	Quit

## 📸 Capture Your Own Hand Images (optional)
python3 scripts/capture_images.py


Images are saved to:

data/asl_dataset/<letter>/

## 🎓 Retrain Model (optional)
python3 scripts/train.py


# 👤 Author

Anshuman Mathur
B.Tech CSE | AI & ML Enthusiast

LinkedIn: ((https://www.linkedin.com/in/anshuumaan-mathur-35746b261/))

