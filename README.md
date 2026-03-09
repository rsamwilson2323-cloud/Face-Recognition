# 👁️ Face Recognition Attendance System

Face Recognition Attendance System is a Python-based application built using **OpenCV and Computer Vision**. The system detects and recognizes faces through a webcam and **automatically records attendance in a CSV file**.

It captures facial images, trains a recognition model using the **LBPH (Local Binary Patterns Histograms) algorithm**, and performs **real-time face recognition**.

---

# ✨ Features

✅ Face dataset creation using webcam
✅ Automatic face image capture
✅ Face detection using **Haar Cascade**
✅ Face recognition using **LBPH algorithm**
✅ Automatic attendance logging
✅ Real-time webcam recognition
✅ CSV attendance file generation

---

# 📂 Project Structure

```id="6uvqej"
Face-Recognition
│
├── face recognition data camara.py
├── face recognition source code.py
├── requirements.txt
├── README.md
├── LICENSE
├── attendance.csv
│
└── face_samples
    ├── Person_Name_1
    │   ├── Person_1.jpg
    │   ├── Person_2.jpg
    │   └── Person_n.jpg
    │
    └── Person_Name_2
        ├── Person_1.jpg
        ├── Person_2.jpg
        └── Person_n.jpg
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```id="opvsv2"
git clone https://github.com/rsamwilson2323-cloud/Face-Recognition.git
cd Face-Recognition
```

---

## 2️⃣ Install Dependencies

```id="uwm9y7"
pip install -r requirements.txt
```

---

# 📦 Requirements

```id="kh98aq"
opencv-python
opencv-contrib-python
numpy
```

---

# 📸 Step 1 — Capture Face Dataset

Run the dataset capture script:

```id="x9p85y"
python "face recognition data camara.py"
```

### Steps

1. Enter your **name**
2. Webcam will start
3. Face images will be captured automatically
4. Press **ENTER** to stop

Images will be saved in:

```id="nm61qu"
face_samples/Person_Name/
```

---

# 🧠 Step 2 — Run Face Recognition

Run the recognition system:

```id="p5egsg"
python "face recognition source code.py"
```

The system will:

• Train the face recognition model
• Start the webcam
• Detect and recognize faces
• Log attendance automatically

Press **ENTER ⏎** to exit.

---

# 📝 Attendance Output

Attendance records are stored in:

```id="e4abex"
attendance.csv
```

Example:

```id="8imjae"
Sam,IN,2026-03-07,09:30:12
Sam,OUT,2026-03-07,09:45:11
```

---

# 🛠 Technologies Used

🐍 Python
👁️ OpenCV
📊 NumPy
🤖 LBPH Face Recognizer
📷 Haar Cascade Classifier

---

# 👨‍💻 Author

**Sam Wilson**

🌐 GitHub
https://github.com/rsamwilson2323-cloud

💼 LinkedIn
https://www.linkedin.com/in/sam-wilson-14b554385

---

# 📜 License

This project is licensed under the **MIT License**.

See the **LICENSE file** for more information.
