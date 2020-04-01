#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#
# https://leetcode-cn.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (32.46%)
# Likes:    243
# Dislikes: 0
# Total Accepted:    47.7K
# Total Submissions: 146.6K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
# 
# 
# 
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
# 
# 说明：m 和 n 的值均不超过 100。
# 
# 示例 1:
# 
# 输入:
# [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r = len(obstacleGrid)
        if r==1:                                                #只有一行的时候，必须全部是0，就是1条路，不然就是0条路
            return 1 if all(obstacleGrid[0][i]==0 for i in range(len(obstacleGrid[0]))) else 0
        c = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1: return 0                    #起始点就不能走，0条路
        dp = [[0 for i in range(c)] for i in range(r)]
        dp[0][0] = 1                                            #初始点
        for i in range(1,c):
            if obstacleGrid[0][i] ==1:              
                dp[0][i] = -1                                   #障碍点在dp中设为-1  就是<=-1
            else:
                dp[0][i] = dp[0][i-1]                           #第一列，每个点都和上面一样，如果有障碍，下面都不能到达了
        for i in range(1,r):
            if obstacleGrid[i][0] ==1: 
                dp[i][0] = -1
            else:
                dp[i][0] = dp[i-1][0]
        # print(dp)
        for i in range(1, r):
            for j in range(1, c):
                if obstacleGrid[i][j] == 1:                     #在dp中标记障碍点
                    dp[i][j] = -1
                else:
                    if dp[i-1][j] <= -1 and dp[i][j-1]>=1:      #上面走不通，左边可以走
                        dp[i][j] = dp[i][j-1]
                    elif dp[i][j-1] <= -1 and dp[i-1][j]>=1:    #左边不不通，上面可以走
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]      #左边加上面，左、上可能会有2个负数，加起来<-1，所有前面的判断要用>= 和<= 
        # print(dp)
        return dp[-1][-1] if dp[-1][-1] > -1 else 0             #到右下角>-1的是右路的，不然就是0条路

    # 优化版，直接在原来的数组上保存结果
    # 链接：https://leetcode-cn.com/problems/unique-paths-ii/solution/bu-tong-lu-jing-ii-by-leetcode/
    def uniquePathsWithObstacles2(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        obstacleGrid[0][0] = 1
        for i in range(1,m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1) #当前为0，上一行为1，走的通放0，不通放1    
        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1) #原理同上

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0                                                  #当前是障碍，到这里的路径是0          
        return obstacleGrid[m-1][n-1]


# @lc code=end

obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
obstacleGrid = [[0]]
obstacleGrid = [[1]]
obstacleGrid = [[0],[0]]
obstacleGrid = [[1],[0]]
obstacleGrid = [[0,0],[1,1],[0,0]]
o = Solution()
print(o.uniquePathsWithObstacles(obstacleGrid))