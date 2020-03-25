#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#
# https://leetcode-cn.com/problems/triangle/description/
#
# algorithms
# Medium (63.76%)
# Likes:    338
# Dislikes: 0
# Total Accepted:    46.2K
# Total Submissions: 72.1K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
# 
# 例如，给定三角形：
# 
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
# 
# 
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
# 
# 说明：
# 
# 如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
# 
#
from typing import List
# @lc code=start
class Solution:
    #倒序相加，没有额外空间
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        r = len(triangle)
        for i in range(r-2,-1,-1):
            for j in range(len(triangle[i])):
                triangle[i][j] = triangle[i][j] + min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]


# @lc code=end

triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
o = Solution()
print(o.minimumTotal(triangle))