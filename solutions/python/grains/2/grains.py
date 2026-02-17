"""
Grains
"""
def square(number):
    """
    Square function
    """
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    grains = 1
    for i in range(number-1):
        grains *= 2
    return grains


def total():
    """
    Total function
    """
    grains = 1
    total = 0
    for i in range(64):
        total += grains
        if i < 64:
            grains *= 2
    return total
