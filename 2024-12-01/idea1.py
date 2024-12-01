
import sys
from time import time


# Problem description:
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


# Space: O(1) | Time: O(n ^ 2)
def solve(prices):
    best_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            best_profit = max(best_profit, prices[j] - prices[i])
    return best_profit


if __name__ == "__main__":
    prices = list(map(int, sys.stdin.readlines()[0].split()))
    start = time()
    solution = solve(prices)
    print(time() - start, solution)
