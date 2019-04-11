#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/32/trees-and-graphs/90/
# 岛屿的个数
# 给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

# 示例 1:

# 输入:
# 11110
# 11010
# 11000
# 00000

# 输出: 1
# 示例 2:

# 输入:
# 11000
# 11000
# 00100
# 00011

# 输出: 3

class Solution(object):
    # 遍历二维数组每一个元素,找到一块陆地后遍历寻找与这块陆地相连的所有陆地并将找到的陆地全部改为"0",
    # 每一个1，岛屿数量加一
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = len(grid)#列数
        if n == 0: return 0
        m = len(grid[0])#行数
        if m == 0: return 0
        res = 0
        # 遍历每一个字符
        for i in range(n):
            for j in range(m):
                # 如果遍历字符是陆地"1"
                if grid[i][j] == "1":
                    res += 1
                    # 递归查找与这块陆地相连的所有陆地 并将他们改为零
                    self.change(grid, i, j)
        return res

    def change(self, grid, i, j):
        grid[i][j] = "0"
        # 判断上方字符
        if i > 0 and grid[i - 1][j] == "1":
            self.change(grid, i - 1, j)
        # 判断左方字符
        if j > 0 and grid[i][j - 1] == "1":
            self.change(grid, i, j - 1)
        # 判断下方字符
        if i < len(grid) - 1 and grid[i + 1][j] == "1":
            self.change(grid, i + 1, j)
        # 判断右方字符
        if j < len(grid[0]) - 1 and grid[i][j + 1] == "1":
            self.change(grid, i, j + 1)


grid = [
  [1, 1, 0, 0, 0],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1]
]

s = Solution()
r = s.numIslands(grid)
print(r)