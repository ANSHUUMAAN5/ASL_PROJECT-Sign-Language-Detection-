
✋ Real-Time Sign Language Detection (A–Z & 0–9) | Deep Learning + Computer Vision

Detect American Sign Language (ASL) A–Z alphabets & 0–9 digits in real-time using webcam.
The system recognizes hand gestures and converts them into text live.

Built by **Anshuman Mathur** (B.Tech CSE | AI & ML Enthusiast)

─────────────────────────────────────────
## 🎯 Demo — How It Works

• Show hand sign to webcam ✋  
• AI predicts the sign 🤖  
• Text appears live ⌨️  
• SPACE key builds words

Works on Mac & Windows laptops.

─────────────────────────────────────────
## 🚀 Features
─────────────────────────────────────────
• Real-time ASL Detection  
• 36 classes (A–Z & 0–9)  
• MobileNetV2 (Transfer Learning)  
• Kaggle + Custom Dataset  
• MediaPipe + OpenCV  
• Trainable with your own images  
• Mac (M1/M2/M3) & Windows support

─────────────────────────────────────────
## 🧠 Tech Stack
─────────────────────────────────────────
Python 3.10  
TensorFlow / TensorFlow‑Metal  
OpenCV  
MediaPipe  
MobileNetV2

─────────────────────────────────────────
## 📁 Folder Structure
─────────────────────────────────────────
ASL_PROJECT/
│
├── models/
│   ├── asl_model.h5
│   └── labels.json
├── scripts/
│   ├── realtime.py
│   ├── capture_images.py
│   └── train.py
├── requirements.txt
└── README.md

─────────────────────────────────────────
## 📂 Dataset Required
─────────────────────────────────────────
Create folder manually:

ASL_PROJECT/data/asl_dataset/

Inside → subfolders:
a/ b/ … z/ and 0/ 1/ … 9/

─────────────────────────────────────────
## 📥 Dataset Download
─────────────────────────────────────────
Google Drive Link: (paste your link here)

Steps:  
1) Download ZIP  
2) Extract → get `asl_dataset`  
3) Create `ASL_PROJECT/data/`  
4) Put `asl_dataset` inside it

Final path:
ASL_PROJECT/data/asl_dataset/

─────────────────────────────────────────
## ⚙️ Installation Guide
─────────────────────────────────────────

### 🍏 Mac (Intel/M1/M2/M3)
----------------------------------
cd ASL_PROJECT
pip3 install -r requirements.txt

For M-series GPU acceleration:
pip3 install tensorflow-macos tensorflow-metal

### 🪟 Windows
----------------------------------
cd ASL_PROJECT
pip install -r requirements.txt

✅ Use Python 3.10

─────────────────────────────────────────
## 🎬 Run Real-Time Detection
─────────────────────────────────────────
python3 scripts/realtime.py

Controls:
SPACE = Add space  
D = Delete char  
Q = Quit

─────────────────────────────────────────
## 📸 Capture Training Images (optional)
─────────────────────────────────────────
python3 scripts/capture_images.py

Saves to:
data/asl_dataset/<letter>/

─────────────────────────────────────────
## 🏋️ Retrain Model (optional)
─────────────────────────────────────────
python3 scripts/train.py

─────────────────────────────────────────
## 🚀 Future Enhancements
─────────────────────────────────────────
• Full sentence formation  
• Voice output (TTS)  
• Web & Mobile App  
• Multi‑user sign recognition  
• Bigger dataset

─────────────────────────────────────────
👤 Author
─────────────────────────────────────────
**Anshuman Mathur**  
B.Tech CSE | Bennett University  
AI & ML | Deep Learning

LinkedIn: (add your link)  
GitHub: (your repo)

⭐ Please star the repository if you like it!
