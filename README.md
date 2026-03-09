👁️ Face Recognition Attendance System

A Python + OpenCV based Face Recognition Attendance System that detects and recognizes faces using a webcam and automatically records attendance in a CSV file.

The system captures facial images, trains a recognition model using the LBPH algorithm, and performs real-time face recognition.

✨ Features

✅ Face dataset creation using webcam
✅ Automatic face image capture
✅ Face detection using Haar Cascade
✅ Face recognition using LBPH
✅ Automatic attendance logging
✅ Real-time webcam recognition
✅ CSV attendance file generation

📂 Project Structure
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
        
⚙️ Installation

1 Clone Repository
git clone https://github.com/rsamwilson2323-cloud/Face-Recognition.git
cd Face-Recognition

2 Install Dependencies
pip install -r requirements.txt

📦 Requirements
opencv-python
opencv-contrib-python
numpy

📸 Step 1 — Capture Face Dataset

Run the dataset capture script:

python "face recognition data camara.py"

Steps:

Enter your name

Webcam will start

Face images will be captured automatically

Press ENTER to stop

Images will be saved in:

face_samples/Person_Name/
🧠 Step 2 — Run Face Recognition

Run:

python "face recognition source code.py"

The system will:

• Train the face recognition model
• Start the webcam
• Detect and recognize faces
• Log attendance automatically

Press ENTER to exit.

📝 Attendance Output

Attendance is stored in:

attendance.csv

Example:

Sam,IN,2026-03-07,09:30:12
Sam,OUT,2026-03-07,09:45:11
🛠 Technologies Used

🐍 Python
👁️ OpenCV
📊 NumPy
🤖 LBPH Face Recognizer
📷 Haar Cascade Classifier

👨‍💻 Author

Sam Wilson

💻 GitHub
https://github.com/rsamwilson2323-cloud

🔗 LinkedIn
https://www.linkedin.com/in/sam-wilson-14b554385

📜 License

This project is licensed under the MIT License.

See the LICENSE file for more information.
