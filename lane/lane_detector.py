import cv2
import numpy as np

def detect_lane(frame):

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    lines = cv2.HoughLinesP(
        edges,
        1,
        np.pi/180,
        threshold=50,
        minLineLength=50,
        maxLineGap=10
    )

    if lines is None:
        return "LANE_UNKNOWN"

    return "LANE_STABLE"