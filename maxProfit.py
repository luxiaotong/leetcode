class Solution(object):
    def maxProfit(self, prices: [int]) -> int:
        low_price = 2**31-1
        print(low_price)
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < low_price:
                low_price = prices[i]
            elif prices[i] - low_price > max_profit:
                max_profit = prices[i] - low_price
        return max_profit

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([7,6,4,3,1]))
print(s.maxProfit([2,1]))
