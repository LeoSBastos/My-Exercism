"""
Scrabble
"""


def score(word):
    """
    I need a switch case
    """
    score = 0
    for letter in word:
        if letter.upper() in ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']:
            score += 1
        elif letter.upper() in ['D', 'G']:
            score += 2
        elif letter.upper() in ['B', 'C', 'M', 'P']:
            score += 3
        elif letter.upper() in ['F', 'H', 'V', 'W', 'Y']:
            score += 4
        elif letter.upper() == 'K':
            score += 5
        elif letter.upper() in ['J', 'X']:
            score += 8
        else:
            score += 10
    return score
