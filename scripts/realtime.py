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
STABLE_FRAMES = 12   # more = less fluctuation

model = load_model(MODEL_PATH)
with open(LABELS_PATH, "r") as f:
    labels = json.load(f)

mp_hands = mp.solutions.hands.Hands(static_image_mode=False, max_num_hands=1)
cap = cv2.VideoCapture(0)

buffer = ""
last_letter = ""
lock = False
confidence_queue = deque(maxlen=10)

print("SPACE=space, D=delete, Q=quit")

while True:
    ret, frame = cap.read()
    if not ret: break

    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = mp_hands.process(rgb)

    pred_letter = ""
    conf = 0

    if results.multi_hand_landmarks:
        xs, ys = [], []
        for lm in results.multi_hand_landmarks[0].landmark:
            xs.append(int(lm.x * w))
            ys.append(int(lm.y * h))
        x1, x2 = max(min(xs)-20,0), min(max(xs)+20,w)
        y1, y2 = max(min(ys)-20,0), min(max(ys)+20,h)
        hand = frame[y1:y2, x1:x2]

        if hand.size > 0:
            img = cv2.resize(hand, IMG_SIZE)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = preprocess_input(img)
            preds = model.predict(np.expand_dims(img, 0), verbose=0)[0]
            conf = float(np.max(preds))
            pred_letter = labels[str(np.argmax(preds))]
            confidence_queue.append(conf)

            avg_conf = np.mean(confidence_queue)

            if avg_conf > CONFIDENCE_THRESHOLD:
                if pred_letter == last_letter:
                    if not lock:
                        buffer += pred_letter   # add only once
                        lock = True            # lock until hand changes
                else:
                    last_letter = pred_letter
                    lock = False

        cv2.rectangle(frame, (x1,y1),(x2,y2),(0,255,0),2)

    else:
        last_letter = ""
        lock = False
        confidence_queue.clear()

    cv2.putText(frame, f"Letter: {pred_letter}  Conf: {conf:.2f}",
                (10,40), cv2.FONT_HERSHEY_SIMPLEX, 0.8,(255,255,255),2)
    cv2.putText(frame, f"Word: {buffer}", (10,460),
                cv2.FONT_HERSHEY_SIMPLEX, 1,(50,255,50),2)

    cv2.imshow("ASL Detection", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'): break
    if key == ord(' '): buffer += " "
    if key == ord('d') and buffer: buffer = buffer[:-1]

cap.release()
cv2.destroyAllWindows()
