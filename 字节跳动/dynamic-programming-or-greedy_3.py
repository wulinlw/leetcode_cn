#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/bytedance/246/dynamic-programming-or-greedy/1028/
# 最大正方形
# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
# 示例:
# 输入: 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 输出: 4

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # dp[i][j]表示以第i行第j列为右下角所能构成的最大正方形边长, 则递推式为: 
        # dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])  ，
        # 当前格子 = 当前的1+ min(最近的左上角，左边，上面)
        # 矩阵中的每一个点作为正方形右下角端点所能构成最大正方形的边长，
        # 亦或是该点 左方、上方、左上方相邻端点所能构成最大正方形边长的最小值加1（该点为"1"），亦或为0（该点为0）
        if matrix == []: return 0 
        M, N = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(N)]for _ in range(M)]
        Max = 0
        for i in range(N):   # 第一排，dp矩阵初始化
            dp[0][i] = int(matrix[0][i])
            Max = max(dp[0][i], Max)
        # print(dp,Max)
        for i in range(M):   # 第一列，dp矩阵初始化
            dp[i][0] = int(matrix[i][0])
            Max = max(dp[i][0], Max)
        # print(dp,Max)
        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][j] == '1': 
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    Max = max(dp[i][j], Max)
        return Max**2

matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]
# matrix = [["1"]]
s = Solution()
res = s.maximalSquare(matrix)
print(res)