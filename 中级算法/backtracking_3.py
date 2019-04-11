#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/49/backtracking/93/
# 全排列
# 给定一个没有重复数字的序列，返回其所有可能的全排列。

# 示例:

# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res=[]
        self.helper(nums,0)
        return self.res

    def helper(self,nums,i):
        nums1=nums[:]
        if i == (len(nums1)-1):
            self.res.append(nums1)
            return
        for l in range(i,len(nums)):
            nums1[i],nums1[l]=nums1[l],nums1[i]
            self.helper(nums1,i+1)
            nums1[i],nums1[l]=nums1[l],nums1[i]



        

nums = [1,2,3]
s = Solution()
r = s.permute(nums)
print(r)




