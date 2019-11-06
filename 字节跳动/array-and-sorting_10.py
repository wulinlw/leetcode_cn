#!/usr/bin/python
#coding:utf-8


# https://leetcode-cn.com/explore/interview/card/bytedance/243/array-and-sorting/1047/
# 接雨水
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。
# 示例:

# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 这道题我推荐使用双指针的动态规划方法求解，通过动态更新左右的最大高度
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

        
h = [0,1,0,2,1,0,1,3,2,1,2,1]
s = Solution()
n = s.trap(h)
print(n)









