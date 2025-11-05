import cv2, os, mediapipe as mp

SAVE_DIR = "data/asl_dataset"
CLASS = input("Enter the letter/digit you want to record: ").lower()
SAVE_PATH = os.path.join(SAVE_DIR, CLASS)
5
os.makedirs(SAVE_PATH, exist_ok=True)

mp_hands = mp.solutions.hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
cap = cv2.VideoCapture(0)

count = 0
print("Press SPACE to start capturing, Q to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = mp_hands.process(rgb)

    if results.multi_hand_landmarks:
        h, w, _ = frame.shape
        xs, ys = [], []
        for lm in results.multi_hand_landmarks[0].landmark:
            xs.append(int(lm.x * w))
            ys.append(int(lm.y * h))

        x1, x2 = max(min(xs)-30,0), min(max(xs)+30,w)
        y1, y2 = max(min(ys)-30,0), min(max(ys)+30,h)

        hand = frame[y1:y2, x1:x2]

        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
        cv2.putText(frame, f"Capturing: {CLASS} {count}", (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0),2)

        key = cv2.waitKey(1) & 0xFF
        if key == ord(' '):  # space to save
            if hand.size > 0:
                cv2.imwrite(os.path.join(SAVE_PATH, f"{CLASS}_{count}.jpg"), hand)
                count += 1
        if key == ord('q'):
            break

    cv2.imshow("Capture Hand Images", frame)

cap.release()
cv2.destroyAllWindows()
print(f"Saved {count} images to {SAVE_PATH}")
