#!/usr/bin/python
#coding:utf-8
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
