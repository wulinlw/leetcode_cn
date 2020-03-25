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
    # [518] 零钱兑换 II    
    def waysToChange(self, amount: int) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        coins = [1, 5, 10, 25]
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = (dp[x] + dp[x - coin]) % 1000000007
        return dp[amount]

n = 5
o = Solution()
print(o.waysToChange(5))
print(o.waysToChange(900750)) #预期结果 504188296