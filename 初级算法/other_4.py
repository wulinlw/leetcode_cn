#!/usr/bin/python
#coding:utf-8

# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 在杨辉三角中，每个数是它左上方和右上方的数的和。

# 示例:
# 输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for i in range(numRows):
            row = [1]
            if i == 0:
                triangle.append(row)
                continue
            for j in range(1, i):
                num = triangle[i-1][j-1] + triangle[i-1][j]
                row.append(num)
            row.append(1)
            triangle.append(row)
        return triangle
        

n=5
s = Solution()
re = s.generate(n)
print("deep:",re)