#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#
# https://leetcode-cn.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (44.54%)
# Likes:    352
# Dislikes: 0
# Total Accepted:    21.7K
# Total Submissions: 48.4K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
# 
# 示例:
# 
# 输入:
# [
# ⁠ ["1","0","1","0","0"],
# ⁠ ["1","0","1","1","1"],
# ⁠ ["1","1","1","1","1"],
# ⁠ ["1","0","0","1","0"]
# ]
# 输出: 6
# 
#
from typing import List
# @lc code=start
class Solution:
    # 使用84题的代码
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix)==0:return 0 
        re = 0 
        r = len(matrix)
        c = len(matrix[0])  
        heights = [0] * c                                       #记录当前行的高度
        for i in range(r):
            for j in range(c):
                if matrix[i][j]=='0':
                    heights[j] = 0 
                else:
                    heights[j] = heights[j] + 1                 #每一行在上一行基础上+1
            re = max(re, self.largestRectangleArea(heights))    #套用84题的解法即可
        return re
    # 84题的代码
    # 单调栈
    # 维护一个单调递增的栈，就可以找到 left_i 和 right_i。
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]                           #方便遍历，避免越界
        stack = []
        re = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:      #栈中最后一个比当前大，
                tmp = stack.pop()                               #大的弹出来
                re = max(re, (i - stack[-1] - 1) * heights[tmp])#stack[-1]栈中最后一个是上一个比当前小的坐标，i - stack[-1] - 1 就是前面比当前小的柱子，到当前的距离
            stack.append(i)
        return re

    #动态规划
    # https://leetcode-cn.com/problems/maximal-rectangle/solution/zui-da-ju-xing-by-leetcode/
    def maximalRectangle2(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        m = len(matrix)
        n = len(matrix[0])

        left = [0] * n                                                      #左边比当前小的
        right = [n] * n                                                     #右边比当前小的
        height = [0] * n                                                    #每一行的高度，竖直方向1的高度
        maxarea = 0

        for i in range(m):                                                  #遍历每一行
            cur_left, cur_right = 0, n
            for j in range(n):                                              #更新每一行高度
                if matrix[i][j] == '1': height[j] += 1
                else: height[j] = 0
            for j in range(n):                                              #更新这一行的left情况
                if matrix[i][j] == '1': left[j] = max(left[j], cur_left)    #从左边中取坐标较大的，这样才是最靠近当前点
                else:
                    left[j] = 0                                             #当前设为0，curleft是右边一个
                    cur_left = j + 1
            for j in range(n-1, -1, -1):                                    #更新这一行的right情况，倒着遍历
                if matrix[i][j] == '1': right[j] = min(right[j], cur_right) #从右边中取坐标较小的，这样才是最靠近当前点
                else:
                    right[j] = n
                    cur_right = j
            for j in range(n):
                maxarea = max(maxarea, height[j] * (right[j] - left[j]))    #计算这一行中的最大值

        return maxarea



# @lc code=end
matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
    ]
o = Solution()
print(o.maximalRectangle2(matrix))