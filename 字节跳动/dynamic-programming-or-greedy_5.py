#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/bytedance/246/dynamic-programming-or-greedy/1030/
# 三角形最小路径和
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

# 例如，给定三角形：
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
# 说明：
# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = triangle[-1]#最后一排初始化dp
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):  # 从倒数第二层开始向上，变化数字，dp[-1]一开始就用不到了
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])#当前dp值 = index的值+ min(上一行index + 上一行index+1)
        return dp[0]#最后汇总到第一行

        

triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
s = Solution()
res = s.minimumTotal(triangle)
print(res)


