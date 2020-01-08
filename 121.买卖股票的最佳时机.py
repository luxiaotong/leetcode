#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low_price = 2**31-1
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < low_price:
                low_price = prices[i]
            elif prices[i] - low_price > max_profit:
                max_profit = prices[i] - low_price
        return max_profit
# @lc code=end

