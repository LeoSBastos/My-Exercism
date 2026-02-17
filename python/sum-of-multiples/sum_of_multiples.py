def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    set_of_multiples = set([x for x in range(1, limit) if any(x % m == 0 for m in multiples if m != 0)])
    print(set_of_multiples)
    return sum(set_of_multiples)
