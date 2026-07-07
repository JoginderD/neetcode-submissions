class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [0] * len(nums), [0] * len(nums)

        for i, num in enumerate(nums):
            if i == 0:
                prefix[i] = num
            else :
                prefix[i] = prefix[i - 1] * num

        for j in range(len(nums) - 1, 0, -1):
            if j == len(nums) - 1:
                suffix[j] = nums[j]
            else:
                suffix[j] = suffix[j + 1] * nums[j]

        l, r = 0, len(nums) - 1
        while l <= r:
            if l == 0:
                nums[l] = suffix[l + 1]
            elif l == r:
                nums[l] = prefix[l - 1]
            else:
                nums[l] = suffix[l + 1] * prefix[l - 1]

            l += 1
        
        return nums