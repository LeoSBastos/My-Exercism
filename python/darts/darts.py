from math import sqrt

def score(x, y):
    distance = sqrt(pow(x,2)+pow(y,2))
    if distance > 10:
        return 0
    elif distance > 5:
        return 1
    elif distance > 1:
        return 5
    elif distance <= 1:
        return 10
