import sys
from time import time


# Problem description: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


# Space: O(1) | Time: O(n)
def solve(prices):
    best_profit = 0
    min_price = prices[0]
    for price in prices:
        best_profit = max(best_profit, price - min_price)
        min_price = min(min_price, price)
    return best_profit


if __name__ == "__main__":
    prices = list(map(int, sys.stdin.readlines()[0].split()))
    start = time()
    solution = solve(prices)
    print(time() - start, solution)
