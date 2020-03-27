#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (52.54%)
# Likes:    857
# Dislikes: 0
# Total Accepted:    171.8K
# Total Submissions: 319.4K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
# 
# 注意：你不能在买入股票前卖出股票。
# 
# 
# 
# 示例 1:
# 
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
# ⁠    注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
# 
# 
# 示例 2:
# 
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # 一个方法团灭 6 道股票问题
    # dp[i][k][0 or 1] 在i天还剩k次交易次数，1持有 0不持有
    # dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]) 不动，昨天持有，今天卖了, + prices[i]
    # dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i]) 不动，昨天没有，今天买入, - prices[i]
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:return 0
        dp = [[0, 0] for i in range(len(prices))]
        dp[0][0] = 0 
        dp[0][1] = -prices[0]
        # dp[1][0] = max(0, dp[0][1] + prices[1])                     #昨天有，今天买
        # dp[1][1] = max(-prices[1], -prices[0])                      #昨天就持有的，或今天才持有
        for i in range(1,len(prices)):
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], - prices[i])             #dp[i-1][k-1][0] 中k-1==0，所以dp[i-1][0][0] = 0。
        return dp[-1][0]                                            #不持有就是卖出了，卖出肯定比持有收益多






# @lc code=end

prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]
o = Solution()
print(o.maxProfit(prices))