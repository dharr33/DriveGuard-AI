import mediapipe as mp

mp_pose = mp.solutions.pose.Pose()

def detect_steering(frame):

    results = mp_pose.process(frame)

    if not results.pose_landmarks:
        return "UNKNOWN"

    left_shoulder = results.pose_landmarks.landmark[11]
    right_shoulder = results.pose_landmarks.landmark[12]

    tilt = left_shoulder.y - right_shoulder.y

    if abs(tilt) > 0.05:
        return "STEERING_ACTIVE"

    return "STEERING_STABLE"