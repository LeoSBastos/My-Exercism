def nth(n):
    counter = 2
    prime = []
    res = 0
    while True:
        if len(prime) == n+1: 
            if(len(prime) == 0):
                res = counter
            else:
                res = prime[n]
            break
        else: 
            test = 0
            for i in range(1, counter//2+1):
                if (counter % i) == 0:
                    test += 1
                if test >= 2:
                    break
            if test < 2:
                prime.append(counter)
        counter += 1
    return res


print(nth(5))