def lcm(a, b):
    first = a
    second = b
    while second != 0:
        cache = second
        second = first % second
        first = cache
    min_number = min(a, b)
    max_number = max(a, b)
    multiplier = int(min_number / first)
    return max_number * int(multiplier)
