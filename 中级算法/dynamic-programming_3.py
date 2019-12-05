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
        # 自底向上
        # dp[i] 表示金额为i需要最少的硬币
        # dp[i] = min(dp[i], dp[i - coins[j]]+1) j所有硬币
        
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c]+1)
        print(dp)
        return dp[-1] if dp[-1] != float("inf") else -1

# 作者：powcai
# 链接：https://leetcode-cn.com/problems/coin-change/solution/dong-tai-gui-hua-bfs-dfs-by-powcai/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

coins = [1, 2, 5]
amount = 11
s = Solution()
r = s.coinChange(coins,amount)
print(r)


