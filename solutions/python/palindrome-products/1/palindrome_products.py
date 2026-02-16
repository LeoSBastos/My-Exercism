def largest(max_factor, min_factor=0):
    if max_factor < min_factor:
        raise ValueError("Min is larger than max")
    possibleFactors1 = possibleFactors2 = [x for x in range(min_factor, max_factor+1)]
    value = 0
    factors = []
    for x in possibleFactors1:
        for y in possibleFactors2:
            if str(x*y) == str(x*y)[::-1] :
                if value <= (x*y):
                    if value == (x*y):
                        if [y,x] not in factors:
                            factors.append([x,y])
                    else:
                        value = x*y
                        factors=[[x,y]]
    return (value if value else None,factors)


def smallest(max_factor, min_factor=0):
    if max_factor < min_factor:
        raise ValueError("Min is larger than max")
    possibleFactors1 = possibleFactors2 = [x for x in range(min_factor, max_factor+1)]
    numberFlag = (max_factor * max_factor) + 1
    value = numberFlag
    factors = []
    for x in possibleFactors1:
        for y in possibleFactors2:
            if str(x*y) == str(x*y)[::-1] :
                if value >= (x*y):
                    if value == (x*y):
                        if [y,x] not in factors:
                            factors.append([x,y])
                    else:
                        value = x*y
                        factors=[[x,y]]
    return (value if value != numberFlag else None,factors)
