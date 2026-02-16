def factoring_sum(number):
    vector = [];
    for i in range(1,number):
        if(number % i == 0):
            vector.append(i)
    return sum(vector)
def classify(number):
    if (number < 1):
        raise ValueError("Number must be positive")
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