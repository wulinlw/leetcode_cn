#!/usr/bin/python
#coding:utf-8


# 面试题 08.11. 硬币
# 硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)
# 示例1:
#  输入: n = 5
#  输出：2
#  解释: 有两种方式可以凑成总金额:
# 5=5
# 5=1+1+1+1+1

# 示例2:
#  输入: n = 10
#  输出：4
#  解释: 有四种方式可以凑成总金额:
# 10=10
# 10=5+5
# 10=5+1+1+1+1+1
# 10=1+1+1+1+1+1+1+1+1+1
# 说明：
# 注意:
# 你可以假设：
# 0 <= n (总金额) <= 1000000
# https://leetcode-cn.com/problems/coin-lcci/

from typing import List
class Solution:
    # dp[i][j] 表示前i个硬币能凑齐j的方案数
    # dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]  没有最后一枚硬币（和少一枚一样）+ 加上最后一枚刚好凑齐
    def waysToChange2(self, n: int) -> int:
        coins = [1,5,10,25]
        dp = [[0 for i in range(n+1)] for j in range(len(coins))]
        for i in range(len(dp)):
            dp[i][0] = 1
        for i in range(n+1):
            dp[0][i] = 1
        for i in range(1, len(coins)):
            for j in range(1, n+1):
                if j<coins[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = (dp[i-1][j] + dp[i][j-coins[i]]) % 1000000007
        return dp[-1][-1]

    # 压缩成一维
    # [518] 零钱兑换 II    
    def waysToChange(self, amount: int) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        coins = [1, 5, 10, 25]
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = (dp[x] + dp[x - coin]) % 1000000007
            print(dp)
        return dp[amount]

n = 5
o = Solution()
print(o.waysToChange(5))
# print(o.waysToChange(900750)) #预期结果 504188296