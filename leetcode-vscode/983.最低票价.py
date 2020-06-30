#
# @lc app=leetcode.cn id=983 lang=python3
#
# [983] 最低票价
#
# https://leetcode-cn.com/problems/minimum-cost-for-tickets/description/
#
# algorithms
# Medium (56.06%)
# Likes:    100
# Dislikes: 0
# Total Accepted:    6.1K
# Total Submissions: 10.6K
# Testcase Example:  '[1,4,6,7,8,20]\n[2,7,15]'
#
# 在一个火车旅行很受欢迎的国度，你提前一年计划了一些火车旅行。在接下来的一年里，你要旅行的日子将以一个名为 days 的数组给出。每一项是一个从 1 到
# 365 的整数。
# 
# 火车票有三种不同的销售方式：
# 
# 
# 一张为期一天的通行证售价为 costs[0] 美元；
# 一张为期七天的通行证售价为 costs[1] 美元；
# 一张为期三十天的通行证售价为 costs[2] 美元。
# 
# 
# 通行证允许数天无限制的旅行。 例如，如果我们在第 2 天获得一张为期 7 天的通行证，那么我们可以连着旅行 7 天：第 2 天、第 3 天、第 4 天、第
# 5 天、第 6 天、第 7 天和第 8 天。
# 
# 返回你想要完成在给定的列表 days 中列出的每一天的旅行所需要的最低消费。
# 
# 
# 
# 示例 1：
# 
# 输入：days = [1,4,6,7,8,20], costs = [2,7,15]
# 输出：11
# 解释： 
# 例如，这里有一种购买通行证的方法，可以让你完成你的旅行计划：
# 在第 1 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 1 天生效。
# 在第 3 天，你花了 costs[1] = $7 买了一张为期 7 天的通行证，它将在第 3, 4, ..., 9 天生效。
# 在第 20 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 20 天生效。
# 你总共花了 $11，并完成了你计划的每一天旅行。
# 
# 
# 示例 2：
# 
# 输入：days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
# 输出：17
# 解释：
# 例如，这里有一种购买通行证的方法，可以让你完成你的旅行计划： 
# 在第 1 天，你花了 costs[2] = $15 买了一张为期 30 天的通行证，它将在第 1, 2, ..., 30 天生效。
# 在第 31 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 31 天生效。 
# 你总共花了 $17，并完成了你计划的每一天旅行。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= days.length <= 365
# 1 <= days[i] <= 365
# days 按顺序严格递增
# costs.length == 3
# 1 <= costs[i] <= 1000
# 
# 
#
from typing import List
import functools
# @lc code=start
class Solution:
    # 正向dp
    # dp[i] = min(dp[i-1]+costs[0], dp[i-7]+costs[1], dp[i-30]+costs[2])
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1]+1)
        for i in days:                                      #出行的天数标记下
            dp[i] = float('inf')
        # print(dp)
        for i in range(1, len(dp)): 
            if dp[i] == 0:                                  #没出行的和前一天一样
                dp[i] = dp[i-1]
                continue
            t1 = costs[0] + dp[i-1]                         #前x天+今天对饮票价然后取最小的，思路和最后一个硬币刚好凑齐x金额的最小硬币数一样
            t2 = costs[1] + dp[i-7] if i>7 else costs[1]
            t3 = costs[2] + dp[i-30] if i>30 else costs[2]
            dp[i] = min(t1, t2, t3)
        # print(dp)
        # for i in days:
        #     print(i,dp[i])
        return dp[-1]
    
    #反向dp
    # dp(i) 来表示从第 i 天开始到一年的结束需要花的钱
    def mincostTickets2(self, days: List[int], costs: List[int]) -> int:
        dayset = set(days)
        durations = [1, 7, 30]

        @functools.lru_cache(None)
        def dp(i):
            if i > 365:
                return 0
            elif i in dayset:
                return min(dp(i + d) + c for c, d in zip(costs, durations)) #若我们购买了 j 天的通行证，那么接下来的 j - 1 天，我们都不再需要购买通行证，只需要考虑第 i + j 天及以后即可
            else:
                return dp(i + 1)                                            #没出行的和前一天一样

        return dp(1)

        
# @lc code=end
days = [1,4,6,7,8,20]
costs = [2,7,15]
days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]
days = [4,5,9,11,14,16,17,19,21,22,24]
costs = [1,4,18] 
o = Solution()
print(o.mincostTickets(days, costs))