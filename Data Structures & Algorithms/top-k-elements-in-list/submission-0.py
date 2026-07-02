class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = {}
        res = []

        for num in nums:
            tracker[num] = tracker.get(num, 0) + 1

        for i in range(k):
            maxV = 0
            maxI = None
            for j, val in tracker.items():
                if val > maxV:
                    maxV = val
                    maxI = j
            
            tracker[maxI] = 0
            res.append(maxI)

        return res