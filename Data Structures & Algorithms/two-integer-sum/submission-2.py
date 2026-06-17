class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, num in enumerate(nums):
            needed = target - num

            if needed in num_map:
                return [num_map[needed], i]

            num_map[num] = i