from typing import List


def binary_search(self, nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        if nums[mid] > target:
            right = mid - 1
    return -1


def test_binary_search():
    list = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(binary_search(list, target))
