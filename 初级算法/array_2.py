#!/usr/bin/python
#coding:utf-8
import sys
class Solution(object):
    # 36ms
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        :由于买卖次数无限，所以只要能获利就进行买卖，这样能保证所有利润都吃到自然利润最大
        """
        profit = 0
        n = len(prices)
        for index in range(n):
            if index == 0:
                continue
            if prices[index] > prices[index - 1]:
                profit += prices[index] - prices[index - 1]
        return profit

    # 28ms
    def maxProfit(self, prices):
        total = 0
        prev = sys.maxint
        for price in prices:
            if price > prev:
                total += price - prev
            prev = price
        return total


prices = [7, 1, 5, 3, 6, 4]
prices = [1, 2, 3, 4, 5]
prices = [7, 6, 4, 3, 1]

s = Solution()
n = s.maxProfit(prices)
print(n)
