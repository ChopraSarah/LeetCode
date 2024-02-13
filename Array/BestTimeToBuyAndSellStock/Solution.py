class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min =100
        max = 0
        left = 0 
        right = 1
        profit = 0
        l = len(prices)
        while right < l:
            new_profit = prices[right] - prices[left]
            if prices[left]<prices[right]:              
                if new_profit>profit:
                    profit = new_profit
            else:
                left = right
            right = right + 1
        return profit
        
