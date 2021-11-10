def slices(series, length):
    if len(series) < 1: 
        raise ValueError("series cannot be empty")
    if len(series) < length:
        raise ValueError("slice length cannot be greater than series length")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if length < 1:
        raise ValueError("slice length cannot be zero")
    
    subS= []
    if(length == len(series)):
        subS.append(series)
    else:
        for i in range(0,len(series)-length+1):
            subS.append(series[i:i+length])
    return subS