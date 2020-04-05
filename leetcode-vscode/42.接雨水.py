#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (48.85%)
# Likes:    977
# Dislikes: 0
# Total Accepted:    69K
# Total Submissions: 139.2K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 
# 
# 
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢
# Marcos 贡献此图。
# 
# 示例:
# 
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
# 
#
from typing import List
# @lc code=start
class Solution:
    # 双指针，通过动态更新左右的最大高度
    # 分别指向头尾，动态找最大值，
    # 接多少雨水是由短板决定的，
    # 如果左边最大值小于右边最大值，就取左边最大值-height[left],然后向右移
    # 反之，右边同理
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1#双指针分别指向头尾
        water, left_max, right_max = 0,0,0
        while left <= right:
            if left_max <= right_max:
                left_max = max(left_max, height[left])#找左边的最高值
                water += left_max-height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])#找右边的最高值
                water += right_max - height[right]
                right -= 1
        return water

    # 动态规划
    # 分别预先算好左边最大值，右边最大值
    # 在遍历每个点，计算每个点能接的雨水，累加起来
    def trap2(self, height: List[int]) -> int:
        n = len(height)
        if n==0:return 0
        re = 0
        left = [0] * n
        right = [0] * n
        for i in range(n):                                                  #先算出左边的最大值
            left[i] = max(left[i-1], height[i]) if i>0 else height[0]
        for i in range(n-1,-1,-1):                                          #在算出右边的最大值
            right[i] = max(right[i+1], height[i]) if i+1<n else height[-1]

        for i in range(n):                                                  #min（左边最高的柱子高度，右边最高的柱子高度） -  这个位置上的柱子高度
            re += min(left[i], right[i]) - height[i]
        return re
    
    #单调栈
    def trap3(self, height: List[int]) -> int:
        if not height:return 0
        re = 0 
        stack = []
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:                  #当前大于栈顶的，说明这一格可以蓄水，把比他矮的都弹出去，每弹一个，计算一次能蓄水的量
                bottomIdx = stack.pop()                                     #取出这一格的坐标
                while stack and height[stack[-1]] == height[bottomIdx]:     #和他一样的要弹出去，避免重复计算
                    stack.pop()
                if stack:                                                                           
                    re += (min(height[stack[-1]], height[i]) - height[bottomIdx]) * (i-stack[-1]-1) #柱子高度较短的 * 长度， 这个格子的蓄水量
            stack.append(i)                                                 #保存坐标
        return re









# @lc code=end


        
h = [0,1,0,2,1,0,1,3,2,1,2,1]
s = Solution()
print(s.trap(h))
print(s.trap2(h))
print(s.trap3(h))