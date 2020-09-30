def is_isogram(string):
    for i, letter in enumerate(string):
        for j, test in enumerate(string):
            if letter.lower() == test.lower() and i != j:
                if(letter != " " and letter != "-"):
                    return False
    return True
