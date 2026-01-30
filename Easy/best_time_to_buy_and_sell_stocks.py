from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_prices= prices[0]

        for p in prices[1:]:
            if buy_prices > p:
                buy_prices=p

            profit = max(profit, p-buy_prices)
        return profit
prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))
