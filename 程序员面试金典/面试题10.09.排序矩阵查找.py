# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题10.09.排序矩阵查找
# 
# https://leetcode-cn.com/problems/sorted-matrix-search-lcci/
# 
# 给定M&times;N矩阵，每一行、每一列都按升序排列，请编写代码找出某元素。
# 示例:
# 
# 现有矩阵 matrix 如下：
# 
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# 
# 
# 给定 target&nbsp;=&nbsp;5，返回&nbsp;true。
# 
# 给定&nbsp;target&nbsp;=&nbsp;20，返回&nbsp;false。
# 
# 
# Medium 45.9%
# Testcase Example: [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# 5
# 
# 提示:
# 如果你正在考虑某个特定列，是否有办法快速消除该列（至少在某些情况下）？
# 由于每列都进行了排序，因此如果该值小于此列中的最小值，则可知该值不能位于此列中。除此以外还能告诉你什么？
# 如果值x小于列的开头，那么它也不能在右边的任何列中。
# 考虑行中的上一个提示。
# 如果我们试图使用一个数组来记录它，会发生什么？这有什么优点和缺点呢？
# 可以使用前面的提示在行和列上向上、向下、向左和向右移动吗？
# 另一种方法是，如果你沿着单元格画一个矩形一直延伸到底部，那么矩阵右坐标所在的单元格将大于这个矩形中所有的单元格。
# 每个单元格的数会小于其下方和右侧的所有数，会大于其上方和左侧的所有数。如果我们想在第一轮排除最多元素，应该将x与哪个元素进行比较？
# 如果将x与矩阵中的中心元素进行比较，我们可以排除大约四分之一的元素。
# 先试试一种简单解法。但希望不要太简单。你应该能够借助矩阵是有序的这一实际情况。
# 可以在每一行进行二进制搜索。这需要多长时间？怎样才能做得更好？
# 
# 
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        if rows == 0:return False
        cols = len(matrix[0])
        r, c = 0, cols-1
        while r<rows and c>=0:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                c -= 1
            else:
                r += 1
        return False

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
o = Solution()
print(o.searchMatrix(matrix, target))