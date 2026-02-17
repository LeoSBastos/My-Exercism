commands_list = ['wink', 'double blink', 'close your eyes', 'jump', 'reverse']


def commands(binary_str: str) -> list[str]:
    cmd_list = [commands_list[i] for i, bit in enumerate(list(binary_str)[::-1]) if bit == '1']
    if 'reverse' in cmd_list:
        cmd_list.remove('reverse')
        cmd_list.reverse()
    return cmd_list
