COLOR_CODE = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}
def label(colors: list):
    value = COLOR_CODE[colors[0]]*10 + COLOR_CODE[colors[1]]
    print(value)
    value *= pow(10,COLOR_CODE[colors[2]])
    if value > 1000000000:
        return str(int(value/1000000000)) + " gigaohms"
    elif value > 1000000:
        return str(int(value/1000000)) + " megaohms"
    elif value > 1000:
        return str(int(value/1000)) + " kiloohms"
    else:
        return str(int(value)) + " ohms"
