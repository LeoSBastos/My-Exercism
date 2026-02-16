def convert(n = None):
    res = ""
    if n % 3 == 0:
        res += "Pling"
    
    if n % 5 == 0:
        res += "Plang"
    
    if n % 7 == 0:
        res += "Plong"
    
    if res == "":
        return str(n)
    else:
        return res

