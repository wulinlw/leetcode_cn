#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/23/dynamic-programming/55/
# 买卖股票的最佳时机
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
# 注意你不能在买入股票前卖出股票。
# 示例 1:

# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
# 示例 2:

# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 引入两个变量，最小买入价格和最大利润，遍历数组，判断最大和最小值来得到最后的结果。
        if len(prices)<2:
            return 0
        min_price = prices[0]
        max_price = 0
        for i in prices:
            min_price = min(min_price, i)
            max_price = max(max_price, i - min_price)
        return max_price

        


prices = [7,1,5,3,6,4]
s = Solution()
re = s.maxProfit(prices)
print("deep:",re)
