#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
# https://leetcode-cn.com/problems/coin-change/description/
#
# algorithms
# Medium (37.76%)
# Likes:    503
# Dislikes: 0
# Total Accepted:    66.3K
# Total Submissions: 171.4K
# Testcase Example:  '[1,2,5]\n11'
#
# 给定不同面额的硬币 coins 和一个总金额
# amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
# 
# 示例 1:
# 
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3 
# 解释: 11 = 5 + 5 + 1
# 
# 示例 2:
# 
# 输入: coins = [2], amount = 3
# 输出: -1
# 
# 说明:
# 你可以认为每种硬币的数量是无限的。
# 
#
from typing import List
# @lc code=start
class Solution:
    #每个金额所需的最少硬币数
    #dp[i] = min(dp[i], dp[i-j]+1)   i-j 当前金额-当前硬币
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0 
        for i in range(len(dp)):
            for j in coins: 
                if i<j:continue
                dp[i] = min(dp[i], dp[i-j]+1)
        return dp[-1] if dp[-1] != float('inf') else -1

    # [518] 零钱兑换 II

# @lc code=end

coins = [1, 2, 5]
amount = 11
# coins = [2]
# amount = 3
o = Solution()
print(o.coinChange(coins, amount))