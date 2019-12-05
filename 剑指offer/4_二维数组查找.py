#!/usr/bin/python
#coding:utf-8

# 二维数组查找
# 在一个二维数组中，每一行都按照从左到右递增的顺序排序
# 每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

# 查找方式从右上角开始查找
# 如果当前元素大于target, 左移一位继续查找
# 如果当前元素小于target, 下移一位继续查找
# 进行了简单的修改, 可以判定输入类型为字符的情况
class Solution(object):
    def find(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        r=0
        c=n-1
        while r<m and c>=0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1
            else:
                r += 1
        return False

        
matrix = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15]]
target = 6
obj = Solution()
re = obj.find(matrix, target)
print(re)
