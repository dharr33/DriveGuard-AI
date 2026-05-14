from collections import deque

eye_buffer = deque(maxlen=30)
yawn_buffer = deque(maxlen=30)

def update_states(eye_state, yawn_state):

    eye_buffer.append(eye_state)
    yawn_buffer.append(yawn_state)

    eye_closure_rate = eye_buffer.count("CLOSED") / len(eye_buffer)

    yawn_freq = yawn_buffer.count("YAWN")

    fatigue_score = (0.6 * eye_closure_rate) + (0.4 * (yawn_freq / 10))

    if fatigue_score > 0.6:
        driver_state = "DROWSY"
    else:
        driver_state = "ALERT"

    return fatigue_score, driver_state