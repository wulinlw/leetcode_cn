#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/description/
#
# algorithms
# Hard (29.27%)
# Likes:    181
# Dislikes: 0
# Total Accepted:    14.6K
# Total Submissions: 49.8K
# Testcase Example:  '2\n[2,4,1]'
#
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
# 
# 注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 
# 示例 1:
# 
# 输入: [2,4,1], k = 2
# 输出: 2
# 解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
# 
# 
# 示例 2:
# 
# 输入: [3,2,6,5,0,3], k = 2
# 输出: 7
# 解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4
# 。
# 随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
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
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices)<=1:return 0
        maxk = k
        if maxk>len(prices):                                        #交易次数比数据还多，就是无限次数了，主要是过超大k的测试用例，不然dp数组会超出内存
            return self.maxProfitUnlimitedK(prices)
        dp = [[[0, 0] for i in range(maxk+1)] for i in range(len(prices))]
        # dp[0][2][0] = 0                                           #第0天，不管还剩几次交易次数，不持有收益是0，也不可能持有(一天内不能瞬间买入卖出)，所以设1为负数
        # dp[0][2][1] = -prices[0]                                                
        # dp[0][1][0] = 0                                                         
        # dp[0][1][1] = -prices[0]
        for k in range(k,-1,-1):
            dp[0][k][0] = 0 
            dp[0][k][1] = -prices[0] 
        for i in range(1, len(prices)):
            for k in range(maxk, 0, -1):                            #这里必须倒着，base case中k是倒着的，这里正序会出现0，1，与前面的设定不同了，就会出错
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])   
        return dp[-1][maxk][0]                                      #不持有就是卖出了，卖出肯定比持有收益多

    #leetcode 122 无限次交易的解法
    def maxProfitUnlimitedK(self, prices: List[int]) -> int:
        if len(prices)<=1:return 0
        dp = [[0, 0] for i in range(len(prices))]
        dp[0][0] = 0 
        dp[0][1] = -prices[0]
        dp[1][0] = max(0, dp[0][1] + prices[1])                     #昨天有，今天买
        dp[1][1] = max(-prices[1], -prices[0])                      #昨天就持有的，或今天才持有
        for i in range(2,len(prices)):
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])             #dp[i-1][k-1][0] 中k-1==0，所以dp[i-1][0][0] = 0。
        return dp[-1][0]                                            #不持有就是卖出了，卖出肯定比持有收益多

# @lc code=end

prices = [2,4,1]
k = 2
prices = [3,2,6,5,0,3]
k = 2
# prices = [1,2]
# k = 1
o = Solution()
print(o.maxProfit(k, prices))