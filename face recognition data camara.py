import cv2
import os
import time
import re

# ================= PATH =================
DATA_DIR = r"D:\python coding\Face Recognition\face_samples"
os.makedirs(DATA_DIR, exist_ok=True)

# ================= NAME =================
name = input("Enter your name: ").strip()
person_dir = os.path.join(DATA_DIR, name)
os.makedirs(person_dir, exist_ok=True)

# ================= FIND LAST IMAGE NUMBER =================
pattern = re.compile(rf"{re.escape(name)}_(\d+)\.jpg")
last_num = 0

for f in os.listdir(person_dir):
    m = pattern.match(f)
    if m:
        last_num = max(last_num, int(m.group(1)))

count = last_num  # continue numbering

CAPTURE_DELAY = 0.7  # stable capture speed

# ================= FACE DETECTOR =================
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

if face_cascade.empty():
    print("❌ Haar Cascade not loaded")
    exit()

# ================= CAMERA =================
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ PC camera not found")
    exit()

print(f"[INFO] Starting capture for '{name}'")
print(f"[INFO] Last image number: {count}")
print("[INFO] Continuous save enabled")
print("[INFO] Press ENTER to stop")

last_save = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=6,
        minSize=(80, 80)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        now = time.time()
        if now - last_save >= CAPTURE_DELAY:
            face = gray[y:y+h, x:x+w]
            face = cv2.resize(face, (200, 200))
            face = cv2.equalizeHist(face)

            count += 1
            img_path = os.path.join(person_dir, f"{name}_{count}.jpg")
            cv2.imwrite(img_path, face)
            last_save = now

            print(f"[SAVED] {img_path}")

    # ================= UI =================
    cv2.putText(
        frame,
        f"Images saved: {count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Continuous Face Capture", frame)

    # ENTER key to stop
    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()

print(f"[DONE] Total images for '{name}': {count}")
print(f"[PATH] {person_dir}")
