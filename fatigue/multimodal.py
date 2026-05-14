def fatigue_score(perclos, yawn_count, attention):

    score = 0

    score += perclos * 0.5
    score += yawn_count * 0.3

    if attention != "ATTENTIVE":
        score += 0.2

    return score