from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        length_actual = 0
        length_old_max = 0
        for x in nums:
            if x == 1:
                length_actual += 1
            elif x == 0:
                if length_actual > length_old_max:
                    length_old_max = length_actual
                length_actual = 0
            print('actual: ', length_actual)
            print('old: ', length_old_max)
            res = max(length_old_max, length_actual)
            print('result: ', res)
        return res
    def findNumbers(self, nums: List[int]) -> int:
        evenNumberLengthCounter = 0
        for x in nums:
            if len(str(x)) % 2 == 0:
                evenNumberLengthCounter += 1
        print('Even numbers counter: ', evenNumberLengthCounter)
        return evenNumberLengthCounter
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        squaredArray = []
        while i < len(nums):
            squaredArray.append(nums[i] * nums[i])
            i += 1
        squaredArray.sort()
        print(squaredArray)
        return squaredArray
    def duplicateZeros(self, arr: List[int]) -> None:
        arrayCapacity = len(arr) - 1
        i = len(arr) - 1
        while i >= 0:
            if arr[i] == 0 and i < arrayCapacity:
                x = i
                # sol.duplicateZeros([8, 4, 5, 0, 0, 0, 0, 7])
                # sol.duplicateZeros([1,0,2,3,0,4,5,0])
                while arrayCapacity > x:
                    # last element dies
                    arr[arrayCapacity] = arr[arrayCapacity - 1]
                    arrayCapacity -= 1
                arrayCapacity = len(arr) - 1
            i -= 1
        print(arr)
    def duplicateZerosBestSolution(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        possible_dups = 0
        length_ = len(arr) - 1

        # Find the number of zeros to be duplicated
        for left in range(length_):

            # Stop when left points beyond the last element in the original list
            # which would be part of the modified list
            if left > length_ - possible_dups:
                break

            # Count the zeros
            if arr[left] == 0:
                # Edge case: This zero can't be duplicated. We have no more space,
                # as left is pointing to the last element which could be included
                if left == length_ - possible_dups:
                    arr[length_] = 0  # For this zero we just copy it without duplication.
                    length_ -= 1
                    break
                possible_dups += 1

        # Start backwards from the last element which would be part of new list.
        last = length_ - possible_dups

        # Copy zero twice, and non zero once.
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]
    def zerosDuplicateMySolution(self, arr: List[int]) -> None:
        length_ = len(arr) - 1
        amount_of_duplicates = 0
        for i in range(length_):
            if i > length_ - amount_of_duplicates:
                break
            if arr[i] == 0 and i == length_ - amount_of_duplicates:
                arr[length_] = 0
                length_ -= 1
                break
            if arr[i] == 0:
                amount_of_duplicates += 1
        startFrom = length_ - amount_of_duplicates
        for i in range(startFrom, -1, -1):
            if arr[i] == 0:
                arr[i + amount_of_duplicates] = 0
                amount_of_duplicates -= 1
                arr[i + amount_of_duplicates] = 0
            else:
                arr[i + amount_of_duplicates] = arr[i]
        print(arr)
    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    def findTwoMaxValues(self, arr: List[int]) -> None:
        length = len(arr) - 1
        theMax = 0
        theSecondMax = 0

        for i in range(length, -1, -1):
            if arr[i] > theMax:
                theSecondMax = theMax
                theMax = arr[i]
            elif arr[i] > theSecondMax:
                theSecondMax = arr[i]
        print('first', theMax)
        print('second', theSecondMax)
    def max_pairwise_product(self, numbers):
        length = len(numbers) - 1
        max_value = 0
        max_second_value = 0
        max_pairwise_product = 0
        for i in range(length, -1, -1):
            if numbers[i] > max_value:
                max_second_value = max_value
                max_value = numbers[i]
            elif numbers[i] > max_second_value:
                max_second_value = numbers[i]
        print(max_value * max_second_value)

    def intersection(self, lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return lst3
    def intersectUsers(self):
        lst1 = []

        # external ids from crd db.
        lst2 = []
        # data user/tag from bot db.
        result_dict_2 = {}

        # data from crdf db.
        result_dict_3 = {}
        result = sol.intersection(lst1, lst2)
        result2 = {}
        print(result)
        print(len(result))
        i = 0
        for i in range(len(result)):
            user_id = result[i]
            user_tag = result_dict_2[user_id]
            user_guid = result_dict_3[user_id]

            # print(user_guid)
            # print(user_id)
            print(user_tag)
            result2[user_id] = user_tag
        print(len(result2))
        # result_dict[]

    # Driver Code
    def mergeSortedArrays(self, nums1: List[int], m: int, nums2: List[int], n: int):
        length_ = m + n
        i = j = q = 0
        for q in range(length_):
            if nums1[i] == nums2[j]:
                nums1[i+1] = nums2[j]
            elif nums1[i] > nums2[j]:
                



sol = Solution()
# sol.findMaxConsecutiveOnes([1,1,0,1,1,1])
# sol.findMaxConsecutiveOnes([1,1,0,1,0,1])

# sol.findNumbers([12,345,2,6,7896])
# sol.findNumbers([555,901,482,1771])

# sol.sortedSquares([-4,-1,0,3,10])
# sol.sortedSquares([-7,-3,2,3,11])

sol.zerosDuplicateMySolution([1,0,2,3,0,0,5,0])
# expected = [1,0,0,2,3,0,0,0]
# expected = [8,4,5,0,0,0,0,0]

# sol.duplicateZerosBestSolution([8,4,5,0,0,0,0,7])
# sol.duplicateZerosBestSolution([1,0,2,3,0,0,5,0])
# sol.duplicateZerosBestSolution([0,0,0,1,0,0,5,7])
# sol.findTwoMaxValues([1,10,10,5,5])
# external ids from bot.

# sol.max_pairwise_product([1,10,5,5,5])