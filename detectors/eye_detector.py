import cv2

eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

def detect_eyes(frame, face):

    x, y, w, h = face

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    roi_gray = gray[y:y+h//2, x:x+w]

    eyes = eye_cascade.detectMultiScale(
        roi_gray,
        scaleFactor=1.2,
        minNeighbors=5
    )

    # If less than 2 eyes detected -> assume closed
    if len(eyes) < 2:
        return True

    return False