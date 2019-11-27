#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/featured/card/array-and-string/199/introduction-to-2d-array/775/
# 螺旋矩阵
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

# 示例 1:

# 输入:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
# 示例 2:

# 输入:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 取一行，逆时针反转90度，刚好竖着的最后一列变成第一行
        # print(list(list(zip(*matrix)))[::-1])
        # print(list(map(list, zip(*matrix)))[::-1])
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(map(list, zip(*matrix)))[::-1]
            # matrix = list(list(zip(*matrix)))[::-1]#和上面一样
        return res



matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
s = Solution()
n = s.spiralOrder(matrix)
print(n)       