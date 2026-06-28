class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i, num in enumerate(numbers):
            difference = target - num
            if difference in numbers:
                if numbers.index(difference) + 1 == i + 1:
                    return[i + 1, numbers.index(difference) + 2]
                return[i + 1, numbers.index(difference) + 1]
        