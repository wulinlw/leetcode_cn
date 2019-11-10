#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/49/backtracking/94/
# 子集
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

# 说明：解集不能包含重复的子集。

# 示例:

# 输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = [[]]
        for i in range(len(nums)):
            # print("1>"+str(i))
            for j in range(len(output)):#不断从已有结果中组合新的
                output.append(output[j]+[nums[i]])
                # print(output[j]+[nums[i]])
                # print(output)
        return output



        

nums = [1,2,3]
s = Solution()
r = s.subsets(nums)
print(r)




