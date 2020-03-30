#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
# https://leetcode-cn.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (64.81%)
# Likes:    412
# Dislikes: 0
# Total Accepted:    69.6K
# Total Submissions: 106.9K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 
# 说明：每次只能向下或者向右移动一步。
# 
# 示例:
# 
# 输入:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==j==0:continue
                elif i==0: grid[i][j] = grid[i][j] + grid[i][j-1]               #第一行，也可以写在循环前面
                elif j==0: grid[i][j] = grid[i][j] + grid[i-1][j]               #第一列
                else:
                    grid[i][j] = min(grid[i][j-1], grid[i-1][j]) + grid[i][j]
        return grid[-1][-1]

# @lc code=end

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

o = Solution()
print(o.minPathSum(grid))