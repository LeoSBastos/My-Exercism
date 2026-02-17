def latest(scores):
    return scores.pop()


def personal_best(scores):
    scores.sort()
    return scores.pop()


def personal_top_three(scores):
    scores.sort(reverse=True)
    if len(scores) < 4:
        return scores
    return scores[:3]