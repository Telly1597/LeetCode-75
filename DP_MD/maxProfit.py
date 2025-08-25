from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        hold = -prices[0]
        cash = 0

        for price in prices[1:]:
            hold = max(hold, cash - price)
            cash = max(cash, hold + price - fee)

        return cash