
# ✋ Real-Time Sign Language Detection (A–Z & 0–9)

This project detects **American Sign Language (ASL)** hand signs (A–Z & 0–9) in **real-time** using your laptop webcam and converts them into text.

Made by **Anshuman Mathur**  
B.Tech CSE | AI & ML Enthusiast

---

## 🎥 Demo Preview (What it Does)

- You show a hand sign in front of webcam
- The system recognizes the sign
- Converts it into text
- You can build words using SPACE & DELETE

Perfect for learning ASL & building real-time AI apps!

---

## 🧠 Tech Used

| Component | Tech |
|---|---|
Model | MobileNetV2 (Transfer Learning)
Framework | TensorFlow (TensorFlow-Metal on M-series Mac)
Camera Processing | OpenCV
Hand Tracking | MediaPipe
Language | Python 3.10

---

## ✨ Features

✅ Recognizes **A–Z** and **0–9**  
✅ Works in **real time**  
✅ Webcam input  
✅ Includes **custom dataset collected by me**  
✅ Train model yourself (optional)  
✅ Works on **Mac & Windows**

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

🪟 Windows Setup
cd ASL_PROJECT
pip install -r requirements.txt


✅ Use Python 3.10 (MediaPipe works best)

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
