#!/usr/bin/python
#coding:utf-8


# 面试题 16.17. 连续数列
# 给定一个整数数组（有正数有负数），找出总和最大的连续数列，并返回总和。

# 示例：
# 输入： [-2,1,-3,4,-1,2,1,-5,4]
# 输出： 6
# 解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 进阶：

# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
# https://leetcode-cn.com/problems/contiguous-sequence-lcci/

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0]
        maxsum = nums[0]
        for i in range(1, len(nums)):
            if sum <0:
                sum = nums[i]
            else: 
                sum += nums[i]
            maxsum = max(maxsum, sum)
        return maxsum

nums = [-2,1,-3,4,-1,2,1,-5,4]
o = Solution()
print(o.maxSubArray(nums))
