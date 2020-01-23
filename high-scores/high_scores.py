def latest(scores):
    last_index = len(scores)-1
    return scores[last_index]


def personal_best(scores):
    max = scores[0]
    for i in scores:
        if i > max:
            max = i
    return max


def personal_top_three(scores):
    scores.sort(reverse=True)
    if len(scores) < 4:
        return scores
    return scores[0:3]
