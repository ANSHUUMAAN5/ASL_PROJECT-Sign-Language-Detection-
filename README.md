
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

## 📁 Project Folder Structure



ASL_PROJECT/
│
├── models/
│ ├── asl_model.h5 → Trained model
│ └── labels.json → Class labels (A-Z, 0-9)
│
├── scripts/
│ ├── realtime.py → Run real-time detection
│ ├── capture_images.py → Capture your own training images
│ └── train.py → Train the model
│
├── requirements.txt
└── README.md


> ⚠️ You MUST create dataset folder manually!

The required directory:



ASL_PROJECT/data/asl_dataset/


And inside that folder, you must have:



a/ b/ c/ ... z/
0/ 1/ ... 9/


---

## 📥 Download Dataset (Required)

Google Drive link to dataset 👇  
👉 **(Insert your Google Drive link here)**

### Steps

1. Download the dataset ZIP
2. Unzip — you will get folder `asl_dataset`
3. Create folder: `ASL_PROJECT/data/`
4. Move `asl_dataset` inside it

✅ Final path must look like:



ASL_PROJECT/data/asl_dataset/


---

## ⚙️ Installation Guide

### 🖥️ Mac (Intel / M1 / M2 / M3)

```bash
cd ASL_PROJECT
pip3 install -r requirements.txt


Mac M1/M2/M3 users only — enable GPU:

pip3 install tensorflow-macos tensorflow-metal
```
```bash
🪟 Windows Setup
cd ASL_PROJECT
pip install -r requirements.txt


✅ Use Python 3.10 (MediaPipe works best)
```
▶️ Run Real-Time Sign Detection
python3 scripts/realtime.py

Controls
Key	Action
SPACE	Adds space (word separator)
D	Deletes last character
Q	Quit Program
📸 Capture Your Own Training Images (Optional)
python3 scripts/capture_images.py


Images will save to:

data/asl_dataset/<letter>/

🏋️ Train the Model (Optional)
python3 scripts/train.py

🚀 Future Plans

Live voice output (speech)

Full ASL sentence recognition

Web UI / Mobile App

Multi-person sign recognition

Larger dataset

🤝 Contributions

Pull requests welcome — improve accuracy, UI, or add features!

👤 Author

Anshuman Mathur
B.Tech CSE | AI & ML Enthusiast

💼 LinkedIn: (add link here)
