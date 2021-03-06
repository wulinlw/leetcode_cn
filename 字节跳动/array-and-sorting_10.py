#!/usr/bin/python
#coding:utf-8


# https://leetcode-cn.com/explore/interview/card/bytedance/243/array-and-sorting/1047/
# 接雨水
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。
# 示例:

# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6


# 每个位置上积水的高度，应该等于min（左边最高的柱子高度，右边最高的柱子高度） -  这个位置上的柱子高度
class Solution(object):
    # 双指针，通过动态更新左右的最大高度
    # 分别指向头尾，动态找最大值，
    # 接多少雨水是由短板决定的，
    # 如果左边最大值小于右边最大值，就取左边最大值-height[left],然后向右移
    # 反之，右边同理
    def trap(self, height):
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

    # 分别预先算好左边最大值，右边最大值
    # 在遍历每个点，计算每个点能接的雨水，累加起来
    def trap2(self, height):
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



        
h = [0,1,0,2,1,0,1,3,2,1,2,1]
s = Solution()
print(s.trap(h))
print(s.trap2(h))








