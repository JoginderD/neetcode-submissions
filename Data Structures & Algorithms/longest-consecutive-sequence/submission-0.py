class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set()

        if len(nums) == 0:
            return 0

        minS = nums[0]
        maxS = nums[0]

        for num in nums:
            if num not in a:
                a.add(num)
            
            minS = min(minS, num)
            maxS = max(maxS, num)

        maxC = 0

        for num in a:
            if num - 1 not in a:
                length = 1

                while num + length in a:
                    length += 1

                maxC = max(maxC, length)

        return maxC