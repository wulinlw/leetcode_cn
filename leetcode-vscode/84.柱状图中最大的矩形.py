#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#
# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (39.07%)
# Likes:    489
# Dislikes: 0
# Total Accepted:    35.1K
# Total Submissions: 89.5K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
# 
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
# 
# 
# 
# 
# 
# 以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
# 
# 
# 
# 
# 
# 图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
# 
# 
# 
# 示例:
# 
# 输入: [2,1,5,6,2,3]
# 输出: 10
# 
#
from typing import List
# @lc code=start
class Solution:
    # 单调栈
    # 以第i根柱子为最矮柱子所能延伸的最大面积
    # 维护一个单调递增的栈，就可以找到两边比i小的 left_i 和 right_i。
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]                           #方便遍历，避免越界
        stack = []
        re = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:      #栈中比当前大的都计算下，记录可以组成的最大矩形（长*高）
                tmp = stack.pop()                               
                re = max(re, (i - stack[-1] - 1) * heights[tmp])#stack[-1]栈中最后一个是上一个比当前小的坐标，i - stack[-1] 就是i到前面柱子的距离，-1是减去那根段的柱子，因为中间的柱子都比当前高，不懂看题目的图
            stack.append(i)
        return re



# @lc code=end
heights = [2,1,5,6,2,3]
o = Solution()
print(o.largestRectangleArea(heights))