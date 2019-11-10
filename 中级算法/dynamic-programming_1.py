#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/51/dynamic-programming/104/
# 跳跃游戏
# 给定一个非负整数数组，你最初位于数组的第一个位置。

# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个位置。
# 示例 1:

# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。
# 示例 2:

# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。



class Solution(object):
    # 贪心算法
    # 算法过程：遍历数组，但是每遍历到一个index我们都得思考，我们跳跃能跳跃到这个地方吗？
    # 于是我们会有一个历史能达到的最大的index,去通过大小对比来判断我们能不能到达当前的index。
    # 如果能的话，我们就需要更新当前的历史最大的index。
    # 跳的最大的index < 我们要跳入的这个index，说明跳不到这个位置。
    def canJump(self, nums):
        maxPos = 0
        for i in range(len(nums)-1):
            # print(i, maxPos, nums[i] + i)
            #如果历史最高高度达不到我们目前的index
            if maxPos < i:
                return False
            #更新历史最大值
            maxPos = max(maxPos, nums[i] + i)

        #判断是否完全通过
        if maxPos >= len(nums) - 1:
            return True
        return False

    def canJump2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #从最后一位开始
        i = len(nums) - 1
        for j in range(len(nums)-2, -1, -1):
            print(i,j, nums[j])
            # i-j 从j到i需要的步数
            # nums[j] 实际能走的步数
            #这一步能到就把终点往前移动一位
            if i - j <= nums[j]:
                #我们的i位就往前挪
                i = j
        #如果能走到第一步，最后i会被减为0
        return i == 0



nums = [2,3,1,1,4]
# nums = [3,2,1,0,4]
s = Solution()
r = s.canJump2(nums)
print(r)


