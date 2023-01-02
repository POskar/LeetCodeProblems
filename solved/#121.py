#121. Best Time to Buy and Sell Stock

from typing import List


def maxProfit(self, prices: List[int]) -> int:
    min = prices[0]
    maxprofit = 0
    for p in prices:
        if min > p: min = p
        if maxprofit < p - min: maxprofit = p -min

    return maxprofit if maxprofit > 0 else 0

prices = [7,6,4,3,1]
print(maxProfit(0, prices))
