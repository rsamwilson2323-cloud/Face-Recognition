import cv2
import os
import numpy as np
from datetime import datetime

# ================= PATHS =================
DATASET_PATH = r"D:\python coding\Face Recognition\face_samples"
ATT_FILE = r"D:\python coding\Face Recognition\attendance.csv"

# ================= FACE RECOGNIZER =================
recognizer = cv2.face.LBPHFaceRecognizer_create(
    radius=1,
    neighbors=8,
    grid_x=8,
    grid_y=8
)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# ================= TRAINING =================
faces = []
labels = []
label_map = {}
current_id = 0

print("[INFO] Training started...")

for person_name in os.listdir(DATASET_PATH):
    person_dir = os.path.join(DATASET_PATH, person_name)
    if not os.path.isdir(person_dir):
        continue

    label_map[current_id] = person_name

    for img_name in os.listdir(person_dir):
        if not img_name.lower().endswith(".jpg"):
            continue

        img_path = os.path.join(person_dir, img_name)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            continue

        # SAME preprocessing as live camera
        img = cv2.resize(img, (200, 200))
        img = cv2.GaussianBlur(img, (3, 3), 0)
        img = cv2.equalizeHist(img)

        faces.append(img)
        labels.append(current_id)

    current_id += 1

if len(faces) == 0:
    print("❌ No training images found")
    exit()

recognizer.train(faces, np.array(labels))
print("[DONE] Training completed")

# ================= ATTENDANCE LOGIC =================
active_faces = {}

def log_event(name, status):
    now = datetime.now()
    with open(ATT_FILE, "a") as f:
        f.write(f"{name},{status},{now.strftime('%Y-%m-%d')},{now.strftime('%H:%M:%S')}\n")

# ================= CAMERA =================
cap = cv2.VideoCapture(0)
print("[INFO] PC camera started (ENTER to exit)")

CONF_THRESHOLD = 95  # sweet spot for LBPH

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces_detected = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(90, 90)
    )

    seen_now = set()

    for (x, y, w, h) in faces_detected:
        if w < 90 or h < 90:
            continue

        face = gray[y:y+h, x:x+w]

        # SAME preprocessing as training
        face = cv2.resize(face, (200, 200))
        face = cv2.GaussianBlur(face, (3, 3), 0)
        face = cv2.equalizeHist(face)

        id_, conf = recognizer.predict(face)

        if conf < CONF_THRESHOLD:
            name = label_map[id_]
            seen_now.add(name)

            if name not in active_faces:
                active_faces[name] = datetime.now()
                log_event(name, "IN")
        else:
            name = "Unknown"

        # Draw
        color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(
            frame,
            f"{name} ({int(conf)})",
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            color,
            2
        )

    # ===== EXIT DETECTION =====
    for name in list(active_faces.keys()):
        if name not in seen_now:
            log_event(name, "OUT")
            del active_faces[name]

    cv2.imshow("Face Recognition Attendance", frame)

    if cv2.waitKey(1) == 13:  # ENTER
        break

cap.release()
cv2.destroyAllWindows()
print("[INFO] Attendance saved in attendance.csv")
