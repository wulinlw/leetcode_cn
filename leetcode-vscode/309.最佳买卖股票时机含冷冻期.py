#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (51.77%)
# Likes:    248
# Dislikes: 0
# Total Accepted:    18.9K
# Total Submissions: 35.9K
# Testcase Example:  '[1,2,3,0,2]'
#
# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
# 
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
# 
# 
# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 
# 
# 示例:
# 
# 输入: [1,2,3,0,2]
# 输出: 3 
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
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
        dp[1][0] = max(0, dp[0][1] + prices[1])                     #昨天有，今天买
        dp[1][1] = max(-prices[1], -prices[0])                      #昨天就持有的，或今天才持有
        for i in range(2, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])      #冷冻期，买入需要往前推一天dp[i-2][0]
        return dp[-1][0]                                            #不持有就是卖出了，卖出肯定比持有收益多


        
# @lc code=end

prices = [1,2,3,0,2]
o = Solution()
print(o.maxProfit(prices))