#!/usr/bin/python
#coding:utf-8

# 矩阵置零
# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

# 示例 1:
# 输入: 
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# 输出: 
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# 示例 2:

# 输入: 
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# 输出: 
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
# 进阶:

# 一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
# 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
# 你能想出一个常数空间的解决方案吗？



class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        index = []
        #找到0的坐标
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    index.append((i, j))
        for i, j in index:
            matrix[i] = [0] * len(matrix[i])#这一行设为0
            for k in range(len(matrix)):#这一列设为0
                matrix[k][j] = 0
        return



nums = [
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
s = Solution()
n = s.setZeroes(nums)
print(n)






