#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/31/
# 旋转图像
# 给定一个 n × n 的二维矩阵表示一个图像。

# 将图像顺时针旋转 90 度。

# 说明：

# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

# 示例 1:

# 给定 matrix = 
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],

# 原地旋转输入矩阵，使其变为:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
# 示例 2:

# 给定 matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ], 

# 原地旋转输入矩阵，使其变为:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        x,y坐标交换，在将每一列反转即可
        """
        # print(matrix[::-1])
        # print(zip(matrix))
        # return
        p = []
        l = len(matrix)
        for i in range(l):
            for j in range(len(matrix[i])):
                if (i, j) in p or (j, i) in p:
                    continue
                else:
                    p.extend([(i, j), (j, i)])
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # print(matrix)
        for i in range(l):
            matrix[i] = matrix[i][::-1]

    def rotate2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        http://www.runoob.com/python/python-func-zip.html
        zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
        如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
        """
        matrix[::] = zip(*matrix[::-1])

    def rotate3(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])        
        # transpose matrix
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i] 
        # reverse each row
        for i in range(n):
            matrix[i].reverse()


# matrix = [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]
# x,y坐标交换
# [1,4,7]
# [2,5,8]
# [3,6,9]
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]

matrix = [
    [5, 1, 9, 11], 
    [2, 4, 8, 10], 
    [13, 3, 6, 7], 
    [15, 14, 12, 16]]
# [5,2,13,15]
# [1,4,3,14]
# [9,8,6,12]
# [11,10,7,16]
s = Solution()
n = s.rotate3(matrix)
print('return', matrix)
for i in range(len(matrix)):
    print(matrix[i])
