#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/24/
# 给定一个整数数组，判断是否存在重复元素。

# 如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

# 示例 1:

# 输入: [1,2,3,1]
# 输出: true
# 示例 2:

# 输入: [1,2,3,4]
# 输出: false
# 示例 3:

# 输入: [1,1,1,3,3,4,3,2,4,2]
# 输出: true

class Solution(object):
    # 字典方式，字典不可重复key
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for i in nums:
            d[i] = 0
        print(d)
        if len(nums) != len(d):
            return True
        else:
            return False

    # 集合方式，集合会自动过滤重复
    def containsDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))


nums = [1, 2, 3, 1]
nums = [1, 2, 3, 4]

s = Solution()
n = s.containsDuplicate(nums)
print(n)
