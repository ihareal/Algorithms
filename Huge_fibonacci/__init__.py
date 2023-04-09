def get_pisano_period(m):
    a, b = 0, 1
    for i in range(0, m * m):
        c = (a + b) % m
        a = b
        b = c
        if a == 0 and b == 1:
            i += 1
            return i


def huge_fibonacci(n, m):
    remainder = n % get_pisano_period(m)
    a = 0
    b = 1
    res = remainder
    for i in range(1, remainder):
        res = (a + b) % m
        a = b
        b = res
    return res
