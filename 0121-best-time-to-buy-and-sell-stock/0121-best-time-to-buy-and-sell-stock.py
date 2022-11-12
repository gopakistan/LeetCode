class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        buy_point = 0
        sell_point = 0
        while sell_point < len(prices):
            possible_profit = prices[sell_point] - prices[buy_point]
            profit = max(profit, possible_profit)
            
            if prices[sell_point] < prices[buy_point]:
                buy_point = sell_point
                
            sell_point += 1
            
            
        return profit
        