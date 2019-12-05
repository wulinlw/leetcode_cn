#!/usr/bin/python
#coding:utf-8

# 63. 不同路径 II
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
# 说明：m 和 n 的值均不超过 100。

# 示例 1
# 输入:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/unique-paths-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if obstacleGrid[0][0] ==1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        obstacleGrid[0][0] = 1
        for i in range(1,m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)#true=1 ,false=0
        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)

        # print(obstacleGrid)
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
        # print(obstacleGrid)
        return obstacleGrid[-1][-1]



obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
s = Solution()
r = s.uniquePathsWithObstacles(obstacleGrid)
print(r)




