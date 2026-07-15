class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxP = 0

        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            else:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)

        return maxP