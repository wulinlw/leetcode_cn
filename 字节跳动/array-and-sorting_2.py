#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/bytedance/243/array-and-sorting/1034/
# 岛屿的最大面积
# 给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。
# 找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)

# 示例 1:
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。

# 示例 2:
# [[0,0,0,0,0,0,0,0]]
# 对于上面这个给定的矩阵, 返回 0。

# 注意: 给定的矩阵grid 的长度和宽度都不超过 50。


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 图
        def cal(L,i,j):
            c = 1
            x = len(L)
            y = len(L[0])
            L[i][j] = 0
            if i-1>=0 and L[i-1][j]: #上
                c = c + cal(L,i-1,j)
            if j+1 < y and L[i][j+1]: #右
                c = c + cal(L,i,j+1)
            if  i+1 < x and L[i+1][j]: #下
                c = c + cal(L,i+1,j)
            if j-1>=0 and L[i][j-1]: #左
                c = c + cal(L,i,j-1)
            return c


        lenr = len(grid)
        lenc = len(grid[0])
        count = 0
        result = 0
        for i in range(lenr):
            for j in range(lenc):
                if grid[i][j] == 1:
                    count = cal(grid,i,j)
                    result = max(result,count)
        return result


grid = [
 [0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
s = Solution()
n = s.maxAreaOfIsland(grid)
print(n)

