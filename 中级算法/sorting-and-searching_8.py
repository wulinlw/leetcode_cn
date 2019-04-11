#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/50/sorting-and-searching/103/
# 搜索二维矩阵 II
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。
# 示例:

# 现有矩阵 matrix 如下：
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# 给定 target = 5，返回 true。
# 给定 target = 20，返回 false。


class Solution(object):
    def searchMatrix_0(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        i = 0
        matrix_m = len(matrix) - 1
        matrix_n = len(matrix[0]) - 1 
        j = matrix_n
        while j >= 0 and i <= matrix_m:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                i += 1
            else:
                j -=1
        return False
    
    #每一行头尾比较
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(rows):
            if matrix[r][0] <= target <= matrix[r][-1]:
                for i in range(cols):
                    if matrix[r][i] == target:
                        return True
        return False



matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 12
matrix = [[1,4],[2,5]]
target = 2
# matrix = [[1,1]]
# target = 1
# matrix = [[-5]]
# target = -5
s = Solution()
r = s.searchMatrix(matrix, target)
print(r)





