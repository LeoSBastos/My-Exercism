def find(search_list: list[int], value: int, previous_index: int = 0) -> list[int] | int:
    if value not in search_list:
        raise ValueError('value not in array')
    sorted_list = sorted(search_list)
    middle_index = len(sorted_list) // 2

    if sorted_list[middle_index] < value:
        return middle_index + 1 + find(sorted_list[middle_index + 1 :], value, previous_index + middle_index + 1)
    elif sorted_list[middle_index] > value:
        return find(sorted_list[:middle_index], value)
    return middle_index
