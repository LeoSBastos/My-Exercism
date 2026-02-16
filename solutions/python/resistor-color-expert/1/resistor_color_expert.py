value_dict = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9,
}

tolerance_dict = {
    'grey': 0.05,
    'violet': 0.1,
    'blue': 0.25,
    'green': 0.5,
    'brown': 1,
    'red': 2,
    'gold': 5,
    'silver': 10,
}


def format_value(val):
    rounded = round(val, 2)
    if rounded % 1 == 0:  # Is integer
        return f'{int(rounded):.0f}'
    elif (rounded * 10) % 1 == 0:  # Has only 1 decimal place
        return f'{rounded:.1f}'
    else:  # Needs 2 decimals
        return f'{rounded:.2f}'


def resistor_label(colors: list[str]) -> str:
    if len(colors) == 1:
        return f'{value_dict[colors[0]]} ohms'
    else:
        tolerance = f'±{tolerance_dict[colors[-1]]}%'
        multiplier = 10 ** value_dict[colors[-2]]
        ohms_list = [value_dict.get(color) * (10 ** (len(colors) - 3 - i)) for i, color in enumerate(colors[:-2])]
        ohms = sum(ohms_list) * multiplier

        if ohms >= 1_000_000:
            ohms /= 1_000_000
            ohms = f'{format_value(ohms)} megaohms'
        elif ohms >= 1_000:
            ohms /= 1_000
            ohms = f'{format_value(ohms)} kiloohms'
        else:
            ohms = f'{format_value(ohms)} ohms'
        return f'{ohms} {tolerance}'
