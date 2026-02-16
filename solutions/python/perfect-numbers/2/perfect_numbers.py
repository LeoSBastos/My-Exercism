"""
Perfect Numbers
"""
def factoring_sum(number):
    """
    factoring sum
    """
    vector = [];
    for i in range(1,number):
        if(number % i == 0):
            vector.append(i)
    return sum(vector)
def classify(number):
    """
    classify
    """
    if (number < 1):
        raise ValueError("Classification is only possible for positive integers.")
    elif number == 1:
        return "deficient"
    else:
        facSum = factoring_sum(number);
        if number == facSum:
            return "perfect"
        elif facSum > number:
            return "abundant"
        else:
            return "deficient"
