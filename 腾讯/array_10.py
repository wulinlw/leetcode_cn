#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/tencent/221/array-and-strings/903/
# 盛最多水的容器
# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

# 说明：你不能倾斜容器，且 n 的值至少为 2。
# 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

# 示例:
# 输入: [1,8,6,2,5,4,8,3,7]
# 输出: 49

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # res最大面积
        L, R, res = 0, len(height) - 1, 0
        while L < R:
            if height[L] < height[R]:
                res = max(res, height[L] * (R - L))#墙壁取短的那头，高出部分无用
                L += 1
            else:
                res = max(res, height[R] * (R - L))
                R -= 1
        return res







nums = [1,8,6,2,5,4,8,3,7]
s = Solution()
n = s.maxArea(nums)
print(n)       