#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#
# https://leetcode-cn.com/problems/coin-change-2/description/
#
# algorithms
# Medium (48.24%)
# Likes:    120
# Dislikes: 0
# Total Accepted:    8.7K
# Total Submissions: 17.9K
# Testcase Example:  '5\n[1,2,5]'
#
# 给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 
# 
# 
# 
# 
# 
# 
# 示例 1:
# 
# 输入: amount = 5, coins = [1, 2, 5]
# 输出: 4
# 解释: 有四种方式可以凑成总金额:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# 
# 
# 示例 2:
# 
# 输入: amount = 3, coins = [2]
# 输出: 0
# 解释: 只用面额2的硬币不能凑成总金额3。
# 
# 
# 示例 3:
# 
# 输入: amount = 10, coins = [10] 
# 输出: 1
# 
# 
# 
# 
# 注意:
# 
# 你可以假设：
# 
# 
# 0 <= amount (总金额) <= 5000
# 1 <= coin (硬币面额) <= 5000
# 硬币种类不超过 500 种
# 结果符合 32 位符号整数
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # dp[i][j] = 第i个硬币，组成j有多少种方法
    # dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]   不使用当前硬币i的总方法数 + 使用当前硬币i的方法数
    # https://leetcode-cn.com/problems/coin-change-2/solution/dong-tai-gui-hua-wan-quan-bei-bao-wen-ti-by-liweiw/
    def change2(self, amount: int, coins: List[int]) -> int:
        if len(coins)==0:
            if amount==0: return 1                  #组成0，只有1种方法
            return 0
        dp = [[0 for i in range(amount+1)] for i in range(len(coins)+1)]                   
        for i in range(len(coins)+1):         #组成0，只有1种方法
            dp[i][0] = 1

        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                if j>=coins[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]   #由于可以重复使用硬币所以这里是j不是j-1
                else:
                    dp[i][j] = dp[i-1][j]
        # print(dp)
        return dp[-1][amount]
    
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)     #组成i块钱，有这么多种组合
        dp[0] = 1                   #以基本情况没有硬币开始组合数量。dp[0] = 1，然后其余等于 0。
        
        for coin in coins:
            for x in range(coin, amount + 1):
                # dp[x] = (dp[x] + dp[x - coin]) % 1000000007   #大数处理
                dp[x] = dp[x] + dp[x - coin]
        return dp[amount]

        
# @lc code=end
amount = 5
coins = [1, 2, 5]
# amount = 3
# coins = [2]
# amount = 1000
# coins = [3,5,7,8,9,10,11]#1952879228
o = Solution()
print(o.change2(amount, coins))
print(o.change(amount, coins))