#
# @lc app=leetcode.cn id=542 lang=python3
#
# [542] 01 矩阵
#
# https://leetcode-cn.com/problems/01-matrix/description/
#
# algorithms
# Medium (37.91%)
# Likes:    207
# Dislikes: 0
# Total Accepted:    19.3K
# Total Submissions: 46.5K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# 给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。
# 
# 两个相邻元素间的距离为 1 。
# 
# 示例 1: 
# 输入:
# 
# 
# 0 0 0
# 0 1 0
# 0 0 0
# 
# 
# 输出:
# 
# 
# 0 0 0
# 0 1 0
# 0 0 0
# 
# 
# 示例 2: 
# 输入:
# 
# 
# 0 0 0
# 0 1 0
# 1 1 1
# 
# 
# 输出:
# 
# 
# 0 0 0
# 0 1 0
# 1 2 1
# 
# 
# 注意:
# 
# 
# 给定矩阵的元素个数不超过 10000。
# 给定矩阵中至少有一个元素是 0。
# 矩阵中的元素只在四个方向上相邻: 上、下、左、右。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # 岛屿问题
    # 广度优先搜索
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        visited = {}                                            #记录访问过的点
        queue = []                                              #广度优先队列
        for i in range(len(matrix)):                            #记录所有0的点
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                    visited[(i, j)] = 1
        while queue:                                            #0点周围的4个点，距离0点为1
            x, y = queue.pop(0)
            for i,j in [(1, 0), (-1, 0), (0, 1), (0,-1)]:
                newx, newy = x+i, y+j
                if 0<=newx<len(matrix) and 0<=newy<len(matrix[0]) and (newx, newy) not in visited:
                    matrix[newx][newy] = matrix[x][y] + 1       
                    visited[(newx,newy)] = 1                    #标记已访问过
                    queue.append((newx, newy))                  #当前点放入队列，下次处理
        return matrix

        
# @lc code=end
matrix = [
    [0,0,0],
    [0,1,0],
    [1,1,1]
    ]
o = Solution()
print(o.updateMatrix(matrix))