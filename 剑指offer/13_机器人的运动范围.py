#!/usr/bin/python
#coding:utf-8

# 机器人的运动范围
# 地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。
# 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
# 但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

class Solution:
    def movingCount(self, threshold, rows, cols):
        if rows==1 or cols==1 or threshold==0:
            return 0
        visited = [[False for j in range(cols)] for i in range(rows)]
        return self.moving(threshold, rows, cols, 0, 0, visited)

    def moving(self, threshold, rows, cols, i, j, visited):
        cnt = 0
        if i<0 or i>=rows or j<0 or j>=cols or visited[i][j] or self.isok(threshold, i,j)==False:
            return cnt
        visited[i][j] = True
        cnt = 1 + self.moving( threshold, rows, cols, i+1, j, visited) + \
              self.moving(threshold, rows, cols, i-1, j, visited) + \
              self.moving(threshold, rows, cols, i, j+1, visited) + \
              self.moving(threshold, rows, cols, i, j-1, visited)
        return cnt
    
    def isok(self, threshold, i, j):
        sumVal = 0
        s = list(str(i)+str(j))
        for i in s: 
            sumVal += int(i)
        return True if sumVal<=threshold else False 
        

obj = Solution()
print(obj.movingCount(5, 10, 10))
# print(obj.isok(18, 35, 38))
