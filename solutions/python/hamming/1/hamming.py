def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Invalid DNA")
    count = 0
    dnA = list(strand_a)
    dnB = list(strand_b)
    for i in range(len(dnA)):
            if dnA[i] != dnB[i]:
                count += 1
    return count