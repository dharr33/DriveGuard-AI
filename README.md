# 🚗 DriveGuard-AI

### AI-Powered Driver Monitoring & Drowsiness Detection System

DriveGuard-AI is a real-time **AI-based driver monitoring system** designed to detect driver fatigue, drowsiness, and loss of attention using computer vision and deep learning techniques.

The system analyzes **multiple behavioral signals** including eye closure, yawning, head pose, lane deviation, and steering behavior to estimate a **driver fatigue score** and trigger alerts when the driver becomes drowsy.

This project demonstrates how **multi-modal AI perception systems** can improve road safety by continuously monitoring driver state and providing early warnings before accidents occur.

---

# 🧠 Key Features

### 👁 Eye Closure Detection

Detects whether the driver's eyes are open or closed using Haar cascade eye detection.

### 😮 Yawn Detection (Deep Learning)

Uses a trained convolutional neural network to detect yawning in real time from facial images.

### 🧭 Head Pose & Attention Tracking

MediaPipe facial landmarks are used to estimate driver head orientation and determine whether the driver is looking forward or distracted.

### 📊 PERCLOS Fatigue Metric

Implements the **PERCLOS (Percentage of Eye Closure)** metric, one of the most widely used fatigue indicators in driver monitoring systems.

### 🚧 Lane Deviation Detection

Detects road lane edges and monitors potential lane drifting behavior.

### 🎮 Steering Behavior Analysis

Uses body pose estimation to analyze steering movement patterns.

### 🧠 Multi-Modal Fatigue Prediction

Combines multiple signals including:

• Eye closure
• Yawn frequency
• Attention score

to calculate a **real-time fatigue score**.

### 🚨 Real-Time Alarm System

If the fatigue score exceeds a threshold, the system triggers:

• Visual warning
• Voice alert

to warn the driver.

### 📈 Live Fatigue Dashboard

A real-time fatigue score graph visualizes the driver's alertness level over time.

---

# 🏗 System Architecture

```
Camera Input
      │
      ▼
Face Detection
      │
 ┌────┴─────┐
 │          │
 ▼          ▼
Eye Detection   Yawn Detection (CNN)
      │
      ▼
PERCLOS Calculation
      │
      ▼
Head Pose / Attention Estimation
      │
      ▼
Lane Detection + Steering Behaviour
      │
      ▼
Multi-Modal Fatigue Model
      │
      ▼
Fatigue Score
      │
 ┌────┴─────┐
 │          │
 ▼          ▼
Alarm System   Live Dashboard
```

---

# 📂 Project Structure

```
DriveGuard-AI
│
├── main.py
│
├── detectors
│   ├── eye_detector.py
│   └── yawn_detector.py
│
├── attention
│   └── head_pose.py
│
├── fatigue
│   ├── perclos.py
│   └── multimodal.py
│
├── lane
│   └── lane_detector.py
│
├── steering
│   └── steering_behavior.py
│
├── utils
│   ├── alarm.py
│   └── dashboard.py
│
└── models
    └── yawn_detection_model4.keras
```

---

# ⚙️ Technologies Used

Python
OpenCV
TensorFlow / Keras
MediaPipe
NumPy
Matplotlib

---

# 📦 Installation

Clone the repository:

```
git clone https://github.com/cavxn/DriveGuard-AI.git
cd DriveGuard-AI
```

Install dependencies:

```
pip install -r requirements.txt
```

If requirements file is not available, install manually:

```
pip install opencv-python mediapipe tensorflow matplotlib numpy
```

---

# ▶️ Running the System

Run the main program:

```
python main.py
```

Press **Q** to exit the system.

---

# 🖥 Example Output

The system displays real-time information including:

```
Attention Score: 92
PERCLOS: 0.18
Yawns: 1
Lane: STABLE
Steering: ACTIVE
Fatigue Score: 0.32
```

If the fatigue score becomes high:

```
⚠ DRIVER DROWSY
```

A voice alert will also warn the driver.

---

# 📊 Fatigue Score Calculation

The fatigue score is computed using a multi-modal model:

```
Fatigue Score =
0.5 × PERCLOS
+ 0.3 × Yawn Frequency
+ 0.2 × Attention Loss
```

This allows the system to combine multiple indicators of driver fatigue.

---

# 🚘 Applications

Driver monitoring systems for vehicles
Advanced driver assistance systems (ADAS)
Road safety research
Human behavior analysis
Autonomous vehicle safety monitoring

---

# 🔬 Future Improvements

Possible extensions include:

• Eye Aspect Ratio (EAR) based blink detection
• Deep learning driver state classification
• Mobile or embedded deployment
• Steering wheel sensor integration
• Real road lane detection models
• Edge deployment on NVIDIA Jetson or Raspberry Pi

---

# 🤝 Contributions

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

# 📜 License

This project is open-source and available under the MIT License.

---

# 👨‍💻 Author

Developed as a collaborative/group project
