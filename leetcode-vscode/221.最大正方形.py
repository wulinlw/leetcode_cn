#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#
# https://leetcode-cn.com/problems/maximal-square/description/
#
# algorithms
# Medium (39.06%)
# Likes:    260
# Dislikes: 0
# Total Accepted:    27K
# Total Submissions: 68.7K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
# 
# 示例:
# 
# 输入: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# 输出: 4
# 
#
from typing import List
# @lc code=start
class Solution:
    # dp(i,j) 表示的是由 1 组成的最大正方形的边长；
    # if (grid[i][j] == 1) 
    #     f[i][j] = min(f[i-1][j-1], f[i-1][j], f[i][j-1]) + 1
    # 当前格、上、左、左上都不能受 0 的限制，才能成为正方形
    # 若形成正方形（非单 1），以当前为右下角的视角看，则需要：当前格、上、左、左上都是 1
    # https://leetcode-cn.com/problems/maximal-square/solution/li-jie-san-zhe-qu-zui-xiao-1-by-lzhlyle/
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix)<1 or len(matrix[0])<1: return 0
        r = len(matrix)
        c = len(matrix[0])
        maxside = 0
        dp = [[0 for i in range(c+1)] for i in range(r+1)]
        for i in range(r):
            for j in range(c):
                if matrix[i][j]=='1':                                       #当前为1的时候处理右下角，见下方说明，是为了避免边界判断
                    dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1], dp[i][j])+1
                    maxside = max(maxside, dp[i+1][j+1])
        return maxside * maxside
        # 为了避免到边的判断处理，在最左侧加上一列 f[i][0] = 0 ，在左上边加上一行 f[0][j] = 0 ，
        # 这才有了官方题解中所谓的 matrix[i-1][j-1] == '1' 与 dp[i][j] ，
        # 其实都是指可对应上的"当前格子"

    # 其实只需关注"当前格子的周边"，故可二维降一维优化
    # 增加 northwest 西北角解决"左上角"的问题
    # 遍历每行时，还原回辅助的原值0 的问题 northwest = 0
    def maximalSquare2(self, matrix: List[List[str]]) -> int:
        if len(matrix)<1 or len(matrix[0])<1: return 0
        c = len(matrix[0])
        maxside = 0
        dp = [0 for i in range(c+1)]
        for row in matrix:
            northwest = 0                                       #左上角（西北），每行都重设为0
            for j in range(c):
                northwestNext = dp[j+1]                         #下一个先存起来
                if row[j]=='1':                                 #当前为1的时候
                    dp[j+1] = min(dp[j], dp[j+1], northwest)+1  #左上角放在northwest中，这就是动态规划的压缩
                    maxside = max(maxside, dp[j+1])
                else:
                    dp[j+1] = 0                                 #不能组成正方形的设为0
                northwest = northwestNext                       #重置northwest
        return maxside * maxside





# @lc code=end
matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
    ]
o = Solution()
print(o.maximalSquare2(matrix))