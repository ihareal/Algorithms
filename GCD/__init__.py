def naive_gcd(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def efficient_gcd(a, b):
    first = a
    second = b
    while second != 0:
        cache = second
        second = first % second
        first = cache
    return first
