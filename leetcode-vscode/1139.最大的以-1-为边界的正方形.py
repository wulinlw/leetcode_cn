#
# @lc app=leetcode.cn id=1139 lang=python3
#
# [1139] 最大的以 1 为边界的正方形
#
# https://leetcode-cn.com/problems/largest-1-bordered-square/description/
#
# algorithms
# Medium (41.46%)
# Likes:    13
# Dislikes: 0
# Total Accepted:    1.9K
# Total Submissions: 4.4K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# 给你一个由若干 0 和 1 组成的二维网格 grid，请你找出边界全部由 1 组成的最大 正方形 子网格，并返回该子网格中的元素数量。如果不存在，则返回
# 0。
# 
# 
# 
# 示例 1：
# 
# 输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：9
# 
# 
# 示例 2：
# 
# 输入：grid = [[1,1,0,0]]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= grid.length <= 100
# 1 <= grid[0].length <= 100
# grid[i][j] 为 0 或 1
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        maxrow, maxcol, maxline = 0, 0, 0                               #当前竖直方向坐标，当前横向坐标，最大边长
        dp =[[[0,0] for i in range(col)] for i in range(row)]
        for i in range(col):                                            #初始化每个点横竖方向的长度
            for j in range(row):
                if grid[j][i] == 1:
                    dp[j][i][0] = 1 + dp[j][i-1][0] if i>0 else 1       #列，左边+1
                    dp[j][i][1] = 1 + dp[j-1][i][1] if j>0 else 1       #行，上面+1
        for i in range(col):
            for j in range(row):
                curline = min(dp[j][i][0], dp[j][i][1])                 #取较短的边长
                if grid[j][i] == 1 and curline>maxline:
                    for k in range(curline, maxline, -1):               #循环比原来maxline长的这段长度
                        if dp[j-k+1][i][0]>=k and dp[j][i-k+1][1]>=k:   #竖直，横向都大于当前，更新最大值
                            maxrow, maxcol, maxline = j, i, k
                            break
        if maxline == 0: return 0
        return maxline * maxline

        
# @lc code=end
grid = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
    ]#9
# grid = [[1,1,0,0]]#1
# grid = [[0,0,0,1]]

# [
#     [[1, 1], [2, 1], [3, 1]], 
#     [[1, 2], [0, 0], [1, 2]], 
#     [[1, 3], [2, 1], [3, 3]]
#     ]
o = Solution()
print(o.largest1BorderedSquare(grid))