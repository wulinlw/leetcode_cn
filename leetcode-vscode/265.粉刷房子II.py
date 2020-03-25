#
# @lc app=leetcode.cn id=265 lang=python3
#
# 265.粉刷房子 II
#
# https://leetcode-cn.com/problems/paint-house-ii
#

# 假如有一排房子，共 n 个，每个房子可以被粉刷成 k 种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。
# 当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个 n x k 的矩阵来表示的。
# 例如，costs[0][0] 表示第 0 号房子粉刷成 0 号颜色的成本花费；costs[1][2] 表示第 1 号房子粉刷成 2 号颜色的成本花费，以此类推。请你计算出粉刷完所有房子最少的花费成本。
# 注意：
# 所有花费均为正整数。

# 示例：
# 输入: [[1,5,3],[2,9,4]]
# 输出: 5
# 解释: 将 0 号房子粉刷成 0 号颜色，1 号房子粉刷成 2 号颜色。最少花费: 1 + 4 = 5; 
#      或者将 0 号房子粉刷成 2 号颜色，1 号房子粉刷成 0 号颜色。最少花费: 3 + 2 = 5. 
# 进阶：
# 您能否在 O(nk) 的时间复杂度下解决此问题？


from typing import List
class Solution:
    # f(i, j)是在第i个房间涂第j种颜色的最优解，那么方程式就是
    # f(i, j) = costs(i, j) + min(f(i - 1, x)) 其中x 是（0, 1, 2, 3, ... k）中除去 j的集合（因为不能相邻房间不能同色）
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]: return 0
        dp = costs
        
        def GetMin(idx, k):
            Min = max(costs[idx])
            for i, cost in enumerate(costs[idx]):
                if i == k:
                    continue
                Min = min(Min, cost)
            return Min
        
        for i in range(1, len(costs)):
            for k in range(len(costs[i])):
                dp[i][k] += GetMin(i - 1, k)        #从上一行下标不为k的元素里找最小的那个
                
        return min(dp[-1])

costs = [[1,5,3],[2,9,4]]
o = Solution()
print(o.minCost(costs))
