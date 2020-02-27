#!/usr/bin/python
#coding:utf-8

# // 面试题29：顺时针打印矩阵
# // 题目：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

class Solution:
    def PrintMatrixClockwisely(self, matrix):
        rows = len(matrix)
        if rows ==0:return []
        cols = len(matrix[0])
        if cols ==0:return []

        s = 0
        while rows>2*s and cols>2*s: 
            self.PrintCircle(matrix, rows, cols, s)
            s += 1
        
    # s 行起点x,y轴坐标 如0,0  1,1  2,2  3,3
    def PrintCircle(self, matrix, rows, cols, s):
        endx = cols-s-1
        endy = rows-s-1
        #向右
        for i in range(s, endx+1):
            print(matrix[s][i], end=' ')
        
        #向下
        if s < endy: 
            for i in range(s+1, endy+1):            #s+1向下需要+1
                print(matrix[i][endx], end=' ')     #列不变

        #向左
        if s < endy and s<endx:
            for i in range(endx-1, s-1, -1):        #从后往前， s-1 python的range循环是只到s,这里需要注意
                print(matrix[endy][i], end=' ')     #行不变
        
        #向上
        if s< endx and s<endy-1:
            for i in range(endy-1, s, -1):
                print(matrix[i][s], end=' ')        #列不变，列就是s
        


matrix = [[1, 2, 3, 4],
         [12, 13, 14, 5],
         [11, 16, 15, 6],
         [10, 9, 8, 7]]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
obj = Solution()
obj.PrintMatrixClockwisely(matrix)



