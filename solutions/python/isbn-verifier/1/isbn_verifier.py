def is_valid(isbn):
    if not isbn:
        return False
    valid = 0
    flag = True
    numbers = [[n for n in list(i)] for i in isbn.split('-')]
    numbers = [item for sublist in numbers for item in sublist]
    if len(numbers) < 10 or len(numbers) > 10:
        return False
    for i, el in enumerate(numbers):
        if not el.isnumeric():
            if el.upper() == 'X' and i == 9:
                el = 10
            else:
                flag = False
                break
        valid += int(el) * (10 - i)
    return flag and valid % 11 == 0