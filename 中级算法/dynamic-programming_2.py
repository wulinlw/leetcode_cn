#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/51/dynamic-programming/105/
# 不同路径
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 问总共有多少条不同的路径？

# 例如，上图是一个7 x 3 的网格。有多少可能的路径？
# 说明：m 和 n 的值均不超过 100。
# 示例 1:
# 输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
# 示例 2:

# 输入: m = 7, n = 3
# 输出: 28


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 横列竖列只有可能有1种情况，而剩下的坐标的路径数都等于它左边和上边的值相加。
        # m = 3,n = 2
        # 1,1,1
        # 1,2,3
        # 因为只能向下或者向右走，所以
        # 每一步 = 上面的 + 左边的
        if m == 1 or n == 1:
            return 1
        dp = [[1 for _ in range(m)] for _ in range(n)]#创建网格数组
        for i in range(1, n):
            for j in range(1, m):
                #等于上边和左边的值相加
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # print(dp)
        return dp[-1][-1]


m = 3
n = 2
s = Solution()
r = s.uniquePaths(m,n)
print(r)




