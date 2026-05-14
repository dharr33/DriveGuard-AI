import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

def get_attention(frame):

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if not results.multi_face_landmarks:
        return 50, "UNKNOWN"

    landmarks = results.multi_face_landmarks[0]

    nose = landmarks.landmark[1]

    if nose.x < 0.4:
        return 40, "LOOKING_LEFT"

    if nose.x > 0.6:
        return 40, "LOOKING_RIGHT"

    return 90, "ATTENTIVE"