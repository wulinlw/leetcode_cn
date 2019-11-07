#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/29/
# 两数之和
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

# 示例:

# 给定 nums = [2, 7, 11, 15], target = 9

# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for idx, i in enumerate(nums):
            h[i] = idx
        for idx, s in enumerate(nums):
            print(s, target - s)
            if h.has_key(target - s) and (idx != h[target - s]):
                return [idx, h[target - s]]

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            x = nums[i]
            if target - x in dict:
                return (dict[target - x], i)
            dict[x] = i


# nums = [2, 7, 11, 15]
# target = 9
nums = [3, 2, 4]
target = 6
# nums = [-3,4,3,90]
# target = 0
s = Solution()
n = s.twoSum(nums, target)
print('return', n)
