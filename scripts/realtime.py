import cv2
import numpy as np
import mediapipe as mp
import json
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from collections import deque

MODEL_PATH = "models/asl_model.h5"
LABELS_PATH = "models/labels.json"
IMG_SIZE = (128, 128)
CONFIDENCE_THRESHOLD = 0.90

model = load_model(MODEL_PATH)
with open(LABELS_PATH, "r") as f:
    labels = json.load(f)

mp_hands = mp.solutions.hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)

mp_draw = mp.solutions.drawing_utils
dot_spec = mp_draw.DrawingSpec(color=(255,255,255), thickness=2, circle_radius=4)
line_spec = mp_draw.DrawingSpec(color=(0,150,255), thickness=2)

cap = cv2.VideoCapture(0)

buffer = ""
last_letter = ""
lock = False
confidence_queue = deque(maxlen=8)

print("SPACE=space, D=delete, Q=quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = mp_hands.process(rgb)

    pred_letter = ""
    conf = 0.0

    if results.multi_hand_landmarks:
        lm = results.multi_hand_landmarks[0]

        
        xs = [int(p.x * w) for p in lm.landmark]
        ys = [int(p.y * h) for p in lm.landmark]
        x1, x2 = max(min(xs)-20, 0), min(max(xs)+20, w)
        y1, y2 = max(min(ys)-20, 0), min(max(ys)+20, h)

        hand_clean = frame[y1:y2, x1:x2].copy()   

        
        if hand_clean.size > 0:
            img = cv2.resize(hand_clean, IMG_SIZE)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = preprocess_input(img)

            preds = model.predict(np.expand_dims(img, 0), verbose=0)[0]
            conf = float(np.max(preds))
            pred_letter = labels[str(np.argmax(preds))]

            confidence_queue.append(conf)
            average_conf = np.mean(confidence_queue)

            if average_conf > CONFIDENCE_THRESHOLD:
                if pred_letter == last_letter:
                    if not lock:
                        buffer += pred_letter
                        lock = True
                else:
                    last_letter = pred_letter
                    lock = False

        
        mp_draw.draw_landmarks(
            frame,
            lm,
            mp.solutions.hands.HAND_CONNECTIONS,
            dot_spec,
            line_spec
        )

        
        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)

        cv2.putText(
            frame,
            f"{pred_letter}  {conf*100:.1f}%",
            (x1, max(y1 - 10, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,0),
            2
        )

    else:
        last_letter = ""
        lock = False
        confidence_queue.clear()

    
    cv2.putText(
        frame,
        f"Word: {buffer}",
        (10, 460),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (50,255,50),
        2
    )

    cv2.imshow("ASL Detection (Clean + Accurate)", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'): break
    if key == ord(' '): buffer += " "
    if key == ord('d') and buffer: buffer = buffer[:-1]

cap.release()
cv2.destroyAllWindows()
