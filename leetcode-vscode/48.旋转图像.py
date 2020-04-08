#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#
# https://leetcode-cn.com/problems/rotate-image/description/
#
# algorithms
# Medium (67.06%)
# Likes:    409
# Dislikes: 0
# Total Accepted:    64.8K
# Total Submissions: 96K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给定一个 n × n 的二维矩阵表示一个图像。
# 
# 将图像顺时针旋转 90 度。
# 
# 说明：
# 
# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
# 
# 示例 1:
# 
# 给定 matrix = 
# [
# ⁠ [1,2,3],
# ⁠ [4,5,6],
# ⁠ [7,8,9]
# ],
# 
# 原地旋转输入矩阵，使其变为:
# [
# ⁠ [7,4,1],
# ⁠ [8,5,2],
# ⁠ [9,6,3]
# ]
# 
# 
# 示例 2:
# 
# 给定 matrix =
# [
# ⁠ [ 5, 1, 9,11],
# ⁠ [ 2, 4, 8,10],
# ⁠ [13, 3, 6, 7],
# ⁠ [15,14,12,16]
# ], 
# 
# 原地旋转输入矩阵，使其变为:
# [
# ⁠ [15,13, 2, 5],
# ⁠ [14, 3, 4, 1],
# ⁠ [12, 6, 8, 9],
# ⁠ [16, 7,10,11]
# ]
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols = len(matrix[0])      
        # transpose matrix
        for i in range(cols):                                               #之遍历列，n行和n列交换，起始就是沿对角线交换[ \ ]
            for j in range(i, cols):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i] 
        # reverse each row
        for i in range(cols):                                               #交换后翻转每一行就是顺时针旋转90度了
            matrix[i].reverse()
    
    def rotate2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        http://www.runoob.com/python/python-func-zip.html
        zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
        如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
        """
        matrix[::] = zip(*matrix[::-1])
# @lc code=end

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
o = Solution()
print(o.rotate(matrix))
print(matrix)
