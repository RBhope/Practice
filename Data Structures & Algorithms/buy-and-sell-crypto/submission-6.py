class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        currMax = 0
        profit = 0
        while r<len(prices):
            if prices[l]<prices[r]:
                profit = prices[r] - prices[l]
                currMax = max(profit,currMax)
            else:
                l=r
            r+=1
            
        return currMax
            

