def compute_fatigue(perclos, yawn_count):

    score = (perclos * 0.7) + (yawn_count * 0.3)

    return score