#!/usr/bin/python
#coding:utf-8


# 面试题 08.02. 迷路的机器人
# 设想有个机器人坐在一个网格的左上角，网格 r 行 c 列。机器人只能向下或向右移动，但不能走到一些被禁止的网格（有障碍物）。设计一种算法，寻找机器人从左上角移动到右下角的路径。
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
# 返回一条可行的路径，路径由经过的网格的行号和列号组成。左上角为 0 行 0 列。

# 示例 1:
# 输入:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# 输出: [[0,0],[0,1],[0,2],[1,2],[2,2]]
# 解释: 
# 输入中标粗的位置即为输出表示的路径，即
# 0行0列（左上角） -> 0行1列 -> 0行2列 -> 1行2列 -> 2行2列（右下角）
# 说明：r 和 c 的值均不超过 100。
# https://leetcode-cn.com/problems/robot-in-a-grid-lcci/

from typing import List
class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        M = len(obstacleGrid)
        if M == 0: return []
        N = len(obstacleGrid[0])
        dp = [[0] * N for _ in range(M)]

        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return []

        # 初始化第一行                            #最后需要从终点倒推到起点
        dp[0][0] = 1
        for i in range(1,N):
            if obstacleGrid[0][i] == 1:
                break
            else:
                dp[0][i] = 1                    #1表示可以向左

        # 初始化第一列
        for i in range(1,M):
            if obstacleGrid[i][0] == 1:
                break
            else:   
                dp[i][0] = 2                    #2表示可以向上
            
        for i in range(1,M):
            for j in range(1, N):
                # print(i,j,dp[i][j-1],dp[i-1][j])
                if obstacleGrid[i][j] == 1:     #障碍物不能设置
                    continue
                elif dp[i][j-1] >= 1:           #左边 有路，可以左右走
                    dp[i][j] = 1
                elif dp[i-1][j] >= 1:           #上面 有路，可以上下走
                    dp[i][j] = 2
        # print(dp)
        out = []
        if dp[M-1][N-1] == 0:
            return []
        
        i,j = M-1,N-1                           #从终点倒推到起点
        while i >= 0 and j >= 0:
            out.append([i,j])
            if dp[i][j] == 2:                   #2是上下走，倒推回去是向上
                i -= 1                          #上面
            else:
                j -= 1                          #1是左右走，倒推回去是向左
        
        return out[::-1]                        #最后翻转路径


obstacleGrid = [
                [0,0,0],
                [0,1,0],
                [0,0,0]
                ]
o = Solution()
print(o.pathWithObstacles(obstacleGrid))