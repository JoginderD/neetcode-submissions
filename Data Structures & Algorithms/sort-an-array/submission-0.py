class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for j in range(len(nums)):
            m = nums[j]
            mi = j
            for i in range(j, len(nums)):
                if nums[i] < m:
                    m = nums[i]
                    mi = i

            nums[mi] = nums[j]
            nums[j] = m
            
        return nums