#!/usr/bin/python
#coding:utf-8
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        x,y坐标交换，在讲每一列反转即可
        """
        print(matrix[::-1])
        print(zip(matrix))
        return
        p = []
        l = len(matrix)
        for i in range(l):
            for j in range(len(matrix[i])):
                if (i, j) in p or (j, i) in p:
                    continue
                else:
                    p.extend([(i, j), (j, i)])
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(l):
            matrix[i] = matrix[i][::-1]

        print(matrix)

    def rotate2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        http://www.runoob.com/python/python-func-zip.html
        zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
        如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
        """
        matrix[::] = zip(*matrix[::-1])


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

matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
# [5,2,13,15]
# [1,4,3,14]
# [9,8,6,12]
# [11,10,7,16]
s = Solution()
n = s.rotate(matrix)
print('return', matrix)
for i in range(len(matrix)):
    print(matrix[i])
