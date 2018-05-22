#!/usr/bin/python
#coding:utf-8
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

    def twoSum(self, nums, target):
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
