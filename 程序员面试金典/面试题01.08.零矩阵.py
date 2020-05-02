#!/usr/bin/python
#coding:utf-8

# 面试题01.08.零矩阵
# 
# https://leetcode-cn.com/problems/zero-matrix-lcci/
# 
# 编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。
# &nbsp;
# 
# 示例 1：
# 
# 输入：
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# 输出：
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# 
# 
# 示例 2：
# 
# 输入：
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# 输出：
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
# 
# 
# 
# Medium 63.2%
# Testcase Example: [[1,1,1],[1,0,1],[1,1,1]]
# 
# 提示:
# 如果你在找到0时清除了行和列，则可能会清理整个矩阵。在对矩阵进行任何更改之前，首先尝试找到所有的0。
# 你能只用额外的O(N)空间而不是O(N2)吗？在为0的单元格列表中你真正需要的是什么信息？
# 你可能需要一些数据存储来维护一个需要清零的行与列的列表。通过使用矩阵本身来存储数据，你是否可以把额外的空间占用减小到O(1)？
# 
# 
from typing import List
class Solution:
    # O(1)空间
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        firstRow = False
        firstCol = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0            #第一行和第一列设为0
                    matrix[0][j] = 0
                    if i == 0: firstRow = True  #第一行第一列，标记下，最后处理
                    if j == 0: firstCol = True
        # print(matrix)
        for i in range(1, len(matrix)):         #每行第一个为0，这一行为0
            if matrix[i][0] == 0:
                matrix[i] = [0] * len(matrix[0])
        # print(matrix)
        for j in range(1, len(matrix[0])):      #每列第一个为0，这一列为0
            if matrix[0][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        if firstRow:                            #注意上面行列都是从1开始的，0行0列最后处理，不然就替换掉了不需要处理的位置
            matrix[0] = [0] * len(matrix[0])
        if firstCol:
            for i in range(len(matrix)):
                matrix[i][0] = 0

matrix = [
    [1,1,1],
    [1,0,1],
    [1,1,1]]
matrix=[
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]]
o = Solution()
print(o.setZeroes(matrix))
print(matrix)