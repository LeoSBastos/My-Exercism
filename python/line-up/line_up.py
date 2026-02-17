def line_up(name: str, number: int) -> str:
    suffix = 'th' if 10 < number % 100 < 14 else {1: 'st', 2: 'nd', 3: 'rd'}.get(number % 10, 'th')
    return f'{name}, you are the {number}{suffix} customer we serve today. Thank you!'
