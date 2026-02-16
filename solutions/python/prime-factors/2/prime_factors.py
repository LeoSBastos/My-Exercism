"""
Prime factors
"""

def factors(value):
    """Factors function"""
    factors = []
    possibleFactor = 2
    remainingValue = value
    while remainingValue > 1:
        while remainingValue % possibleFactor == 0:
            remainingValue /= possibleFactor
            factors.append(possibleFactor)
        possibleFactor += 1
    return factors
