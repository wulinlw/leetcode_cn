#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/51/dynamic-programming/106/
# 零钱兑换
# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

# 示例 1:

# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3 
# 解释: 11 = 5 + 5 + 1
# 示例 2:

# 输入: coins = [2], amount = 3
# 输出: -1
# 说明:
# 你可以认为每种硬币的数量是无限的。

# https://blog.csdn.net/qq_17550379/article/details/82909656
from typing import List
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 自底向上
        # dp[i] 表示金额为i需要最少的硬币
        # dp[i] = min(dp[i], dp[i - coins[j]]+1) j所有硬币
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if i - coin < 0:continue
                dp[i] = min(dp[i], dp[i - coin]+1)
        print(dp)
        return dp[-1] if dp[-1] != float("inf") else -1

    def coinChange2(self, coins: List[int], amount: int) -> int:
        def dp(n):
            if n==0:return 0
            if n<0:return -1
            res = float('inf')
            for coin in coins:
                sub = dp(n-coin)
                if sub==-1:continue
                res = min(res, sub+1)
            return res if res!=float('inf') else -1
        return dp(amount)


coins = [1, 2, 5]
amount = 11
s = Solution()
r = s.coinChange(coins,amount)
print(r)


