#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#
# https://leetcode-cn.com/problems/min-cost-climbing-stairs/description/
#
# algorithms
# Easy (46.98%)
# Likes:    244
# Dislikes: 0
# Total Accepted:    25.7K
# Total Submissions: 54.2K
# Testcase Example:  '[0,0,0,0]'
#
# 数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
# 
# 每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
# 
# 您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。
# 
# 示例 1:
# 
# 
# 输入: cost = [10, 15, 20]
# 输出: 15
# 解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
# 
# 
# 示例 2:
# 
# 
# 输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# 输出: 6
# 解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
# 
# 
# 注意：
# 
# 
# cost 的长度将会在 [2, 1000]。
# 每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f1 = f2 = 0                         #前一步，前两步
        for i in range(len(cost)):
            cur = cost[i] + min(f1, f2)     #取最小的消耗相加,这里不能直接复制给f2，因为复制后的变量变了
            f1 = f2 
            f2 = cur                        #取最小的消耗相加
        return min(f1, f2)                  #最后一步小号最少的

# @lc code=end

cost = [10, 15, 20]
cost = [0,0,1,0]
o = Solution()
print(o.minCostClimbingStairs(cost))
