class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxsell = 0
        mid = len(prices) // 2
        l, r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxsell = max(maxsell, profit)
            else:
                l = r
            r+=1
        return maxsell