import os
import time

last_alarm = 0

def trigger_alarm():

    global last_alarm

    current_time = time.time()

    # prevent alarm spamming
    if current_time - last_alarm < 5:
        return

    last_alarm = current_time

    print("⚠ DRIVER DROWSY ALERT")

    try:
        os.system('say "Warning driver fatigue detected"')
    except:
        pass