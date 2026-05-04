# 🎯 ProctorVision: Intelligent Exam Monitoring System

ProctorVision is a real-time AI-based proctoring system designed to detect suspicious behavior during online examinations using computer vision and audio analysis.

---

## 🚀 Features

- 👁️ Facial recognition and identity verification  
- 👀 Eye tracking and head pose estimation  
- 🗣️ Audio monitoring with speech-to-text detection  
- 📱 Detection of mobile phone usage  
- 👥 Multiple person detection in frame  
- ⚠️ Real-time alerts for suspicious activities  

---

## 🧠 Tech Stack

- Python  
- OpenCV  
- Dlib  
- SpeechRecognition / Audio Processing  
- NumPy  

---

## ⚙️ System Overview

The system continuously monitors the user during an online exam using both video and audio inputs. It applies multiple AI-based detection modules to identify suspicious patterns and triggers alerts when anomalies are detected.

---

## 🔄 Workflow

1. Capture live video feed from webcam  
2. Perform face detection and recognition  
3. Track eye movement and head pose  
4. Detect objects such as mobile phones and additional persons  
5. Process audio input to detect conversations  
6. Flag suspicious activities and generate alerts in real time  

---

## 📂 Project Structure
proctorvision/
│── src/
│── models/
│── audio/
│── utils/
│── main.py
│── requirements.txt


---

## ▶️ Installation & Setup

```bash
git clone https://github.com/yourusername/proctorvision.git
cd proctorvision
pip install -r requirements.txt
python main.py

⚠️ Limitations
Accuracy depends on lighting and camera quality
Audio detection may vary based on background noise
Requires webcam and microphone access
🚀 Future Improvements
Web-based dashboard for monitoring
Cloud-based storage and logging
Integration with online exam platforms
Improved model accuracy with deep learning
👨‍💻 Author

Shrikar Vidyasagar Gujjeti

GitHub: https://github.com/ShrikarGujjeti
LinkedIn: https://linkedin.com/in/shrikar-gujjeti
