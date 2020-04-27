#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# https://leetcode-cn.com/problems/number-of-islands/description/
#
# algorithms
# Medium (47.13%)
# Likes:    494
# Dislikes: 0
# Total Accepted:    85.7K
# Total Submissions: 176.2K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 
# 此外，你可以假设该网格的四条边均被水包围。
# 
# 示例 1:
# 
# 输入:
# 11110
# 11010
# 11000
# 00000
# 输出: 1
# 
# 
# 示例 2:
# 
# 输入:
# 11000
# 11000
# 00100
# 00011
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # bfs O(m*n) 空间复杂度O(min(m, n))
    def numIslands2(self, grid: List[List[str]]) -> int:
        r = len(grid)
        if r == 0: return 0
        c = len(grid[0])
        stack = []
        re = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    re += 1
                    grid[i][j] = '0'
                    stack.append((i,j))                             #当前点加入队列
                    while stack:                                    
                        curx, cury = stack.pop(0)
                        grid[curx][cury] = '0'
                        for j in [(1,0), (-1,0), (0,1), (0,-1)]:    #想4个方向找1，不断扩散
                            newx, newy = curx + j[0], cury + j[1]
                            if 0<=newx<len(grid) and 0<=newy<len(grid[0]) and grid[newx][newy]=='1' :
                                grid[newx][newy] = '0'
                                stack.append((newx, newy))
        return re

    # dfs O(m*n) 空间复杂度O(m*n)
    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        if r == 0: return 0
        c = len(grid[0])
        re = 0

        def dfs(i, j):
            grid[i][j] = '0'
            for d in [(1,0), (-1,0), (0,1), (0,-1)]:
                newx, newy = i + d[0], j + d[1]
                if 0<=newx<len(grid) and 0<=newy<len(grid[0]) and grid[newx][newy]=='1' :   #四周等于1的dfs
                    dfs(newx, newy)

        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    re += 1
                    dfs(i, j)
        return re


# @lc code=end
grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
o = Solution()
print(o.numIslands(grid))   