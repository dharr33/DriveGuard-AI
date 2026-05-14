import matplotlib.pyplot as plt

fatigue_history = []

def update_dashboard(score):

    fatigue_history.append(score)

    if len(fatigue_history) > 50:
        fatigue_history.pop(0)

    plt.clf()
    plt.plot(fatigue_history)
    plt.title("Fatigue Score")
    plt.pause(0.001)