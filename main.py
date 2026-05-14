import cv2
import time

from detectors.eye_detector import detect_eyes
from detectors.yawn_detector import detect_yawn

from fatigue.perclos import Perclos
from fatigue.multimodal import fatigue_score

from attention.head_pose import get_attention
from lane.lane_detector import detect_lane
from steering.steering_behavior import detect_steering

from utils.alarm import trigger_alarm
from utils.dashboard import update_dashboard


# Initialize webcam
cap = cv2.VideoCapture(0)

# Haar face detector
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# PERCLOS tracker
perclos_tracker = Perclos(window_size=50)

# Counters
yawn_count = 0
yawn_frames = 0


while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    eyes_closed = False
    attention_state = "UNKNOWN"
    attention_score = 50

    for (x, y, w, h) in faces:

        face = (x, y, w, h)

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

        # Eye detection
        eyes_closed = detect_eyes(frame, face)

        # Yawn detection
        yawn_status = detect_yawn(frame, face)

        if yawn_status == "YAWN":
            yawn_frames += 1
        else:
            if yawn_frames > 3:
                yawn_count += 1
            yawn_frames = 0

        # Attention detection
        attention_score, attention_state = get_attention(frame)

        break


    # Lane detection
    lane_status = detect_lane(frame)

    # Steering behaviour
    steering_status = detect_steering(frame)

    # PERCLOS calculation
    perclos = perclos_tracker.update(eyes_closed)

    # Fatigue score
    fatigue = fatigue_score(perclos, yawn_count, attention_score)

    # Update dashboard graph
    update_dashboard(fatigue)

    # Trigger alarm
    if fatigue > 0.6:
        trigger_alarm()


    # Display information

    cv2.putText(frame, f"Attention Score: {attention_score}",
                (20,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255),2)

    cv2.putText(frame, f"PERCLOS: {round(perclos,2)}",
                (20,60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255),2)

    cv2.putText(frame, f"Yawns: {yawn_count}",
                (20,90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255),2)

    cv2.putText(frame, f"Attention: {attention_state}",
                (20,120), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,0),2)

    cv2.putText(frame, f"Lane: {lane_status}",
                (20,150), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,0),2)

    cv2.putText(frame, f"Steering: {steering_status}",
                (20,180), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,0),2)

    cv2.putText(frame, f"Fatigue Score: {round(fatigue,2)}",
                (20,210), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255),2)


    if fatigue > 0.6:

        cv2.putText(frame, "⚠ DRIVER DROWSY",
                    (380,40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,0,255),
                    3)


    cv2.imshow("AI Driver Monitoring System", frame)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()