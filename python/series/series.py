def slices(series, length):
    if length < 1 or len(series) < 1 or len(series) < length:
        raise ValueError("Operation invalid.")
    subS= []
    if(length == len(series)):
        subS.append(series)
    else:
        for i in range(0,len(series)-length+1):
            subS.append(series[i:i+length])
    return subS