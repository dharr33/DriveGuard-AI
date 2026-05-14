class Perclos:

    def __init__(self, window_size=50):
        self.window_size = window_size
        self.eye_history = []

    def update(self, eyes_closed):

        if len(self.eye_history) >= self.window_size:
            self.eye_history.pop(0)

        self.eye_history.append(1 if eyes_closed else 0)

        return sum(self.eye_history) / len(self.eye_history)