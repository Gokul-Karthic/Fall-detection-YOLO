🧍‍♂️ YOLOv8 Pose-Based Fall Detection System
<p align="center"> <b>A real-time AI system for accurate human fall detection using pose estimation</b> </p> <p align="center"> <img src="demo.gif" width="650" alt="YOLOv8 Fall Detection Demo"/> </p>
📌 Overview


This project implements a real-time fall detection system using YOLOv8 Pose Estimation.
Unlike traditional bounding-box methods, it analyzes human skeletal keypoints to reliably detect falls from:
➡️ Sideways
⬇️ Forward
⬆️ Backward
The system works with a live camera feed from a mobile phone (IP Webcam) or a webcam, making it suitable for elderly care, healthcare monitoring, and smart surveillance.





✨ Key Features


🧠 Pose-based fall detection using YOLOv8

🎯 Accurate detection for front, back, and sideways falls

🦴 Uses human body keypoints instead of only bounding boxes

❌ Reduces false positives (e.g., hand waving, normal movement)

⏱️ Automatic reset after fall detection (2 seconds)

📱 Supports mobile phone camera (IP Webcam) and laptop webcam

⚡ Runs in real-time using YOLOv8 Nano Pose model





🔍 How It Works


YOLOv8 Pose Model detects 17 human body keypoints


(head, shoulders, hips, knees, ankles)


The system computes:


Body tilt angle


Hip position relative to the frame


Sudden posture changes over time


A fall is confirmed only if:


An abnormal body angle is detected


The person is close to the ground


The condition persists for multiple frames


Displays “FALL DETECTED” alert


Alert automatically resets after 2 seconds


This approach significantly improves detection of front and backward falls, which are difficult for standard YOLO models.





🛠️ Tech Stack


Python 3.9+


YOLOv8 (Ultralytics)


OpenCV


NumPy


IP Webcam (Android) / Webcam
