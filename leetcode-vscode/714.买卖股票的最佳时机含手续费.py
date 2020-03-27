#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/
#
# algorithms
# Medium (61.98%)
# Likes:    140
# Dislikes: 0
# Total Accepted:    13.5K
# Total Submissions: 21.3K
# Testcase Example:  '[1,3,2,8,4,9]\n2'
#
# 给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
# 
# 你可以无限次地完成交易，但是你每次交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
# 
# 返回获得利润的最大值。
# 
# 示例 1:
# 
# 输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
# 输出: 8
# 解释: 能够达到的最大利润:  
# 在此处买入 prices[0] = 1
# 在此处卖出 prices[3] = 8
# 在此处买入 prices[4] = 4
# 在此处卖出 prices[5] = 9
# 总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
# 
# 注意:
# 
# 
# 0 < prices.length <= 50000.
# 0 < prices[i] < 50000.
# 0 <= fee < 50000.
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
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices)<=1:return 0
        dp = [[0, 0] for i in range(len(prices))]
        dp[0][0] = 0 
        dp[0][1] = -prices[0] - fee                                       #第一天也要-fee
        for i in range(1,len(prices)):
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i] - fee)  #dp[i-1][k-1][0] 中k-1==0，所以dp[i-1][0][0] = 0。
        return dp[-1][0]                                                  #不持有就是卖出了，卖出肯定比持有收益多
        # fee放下面dp[i][k][1] 的时候，base case里面dp[0][k][1] 也要-fee哦，不然就差了一个手续费 
        # 放上面时，dp[0][1]不用-fee可以是因为base case里面dp[0][k][0] 始终等于0，相当于买入收手续费，卖出不收，所以没影响
# @lc code=end

prices = [1, 3, 2, 8, 4, 9]
fee = 2
o = Solution()
print(o.maxProfit(prices, fee))