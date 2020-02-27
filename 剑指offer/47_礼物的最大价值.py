#!/usr/bin/python
#coding:utf-8

# // 面试题47：礼物的最大价值
# // 题目：在一个m×n的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值
# // （价值大于0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或
# // 者向下移动一格直到到达棋盘的右下角。给定一个棋盘及其上面的礼物，请计
# // 算你最多能拿到多少价值的礼物？

class Solution:
    # 动态规划
    # dp[i][j] = 上方和左边，取最大的+matrix[i][j]
    def getMaxValue(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n) ]for _ in range(m)]

        for i in range(m):
            for j in range(n):
                left = dp[i-1][j] if i>0 else 0
                up = dp[i][j-1] if j>0 else 0
                dp[i][j] = max(up, left) + matrix[i][j]
        # for i in range(n):
        #     print(dp[i])
        return dp[-1][-1]

        

matrix = [
    [1, 10, 3, 8],
    [12,2,  9, 6],
    [5, 7,  4, 11],
    [3, 7, 16, 5],
]
obj = Solution()
print(obj.getMaxValue(matrix))
