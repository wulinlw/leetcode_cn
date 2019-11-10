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
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')]*(amount+1)
        # print(dp)
        dp[0] = 0
        for coin in coins:
            for j in range(coin, amount+1):
                dp[j] = min(dp[j], dp[j - coin] + 1)
                # print(dp)
        return -1 if dp[-1] > amount else dp[-1]
# https://blog.csdn.net/u014160286/article/details/80261440
# 当总金额为amount时，所需的最少硬币个数为dp[amount]，
# 那么当amount = 11时，求出所有dp[1]、dp[2]、...、dp[11]的值。
# dp[1]到dp[10]就可以说是dp[11]的子问题
# 所以从11的总金额中取出任意一枚硬币，剩下的金额所需最少硬币个数再加上1就是所需硬币个数
coins = [1, 2, 5]
amount = 11
s = Solution()
r = s.coinChange(coins,amount)
print(r)


