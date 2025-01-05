from typing import List


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

def findGCD(self, nums: List[int]) -> None:
    max = min = nums[0]
    i = 1
    for i in range(len(nums) - 1):
        if nums[i] < min:
            min = nums[i]
        if nums[i] > max:
            max = nums[i]
    print(min)
    print(max)
    # return max

