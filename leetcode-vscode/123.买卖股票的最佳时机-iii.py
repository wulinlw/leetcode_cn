#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (41.39%)
# Likes:    327
# Dislikes: 0
# Total Accepted:    27.9K
# Total Submissions: 66.2K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
# 
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 
# 示例 1:
# 
# 输入: [3,3,5,0,0,3,1,4]
# 输出: 6
# 解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
# 随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
# 
# 示例 2:
# 
# 输入: [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4
# 。   
# 注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
# 因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
# 
# 
# 示例 3:
# 
# 输入: [7,6,4,3,1] 
# 输出: 0 
# 解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。
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
        maxk = 2
        dp = [[[0, 0] for i in range(maxk+1)] for i in range(len(prices))]
        dp[0][2][0] = 0                                                         #第0天，不管还剩几次交易次数，不持有收益是0，也不可能持有(一天内不能瞬间买入卖出)，所以设1为负数
        dp[0][2][1] = -prices[0]                                                
        dp[0][1][0] = 0                                                         
        dp[0][1][1] = -prices[0]                                                
        for i in range(1, len(prices)):
            for k in range(maxk, 0, -1):                                        #这里必须倒着，base case中k是倒着的，这里正序会出现0，1，与前面的设定不同了，就会出错
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])   
        return dp[-1][maxk][0]                                                  #不持有就是卖出了，卖出肯定比持有收益多



# @lc code=end

prices = [3,3,5,0,0,3,1,4]
# prices = [7,6,4,3,1]
# prices = [1,2,3,4,5]
o = Solution()
print(o.maxProfit(prices))