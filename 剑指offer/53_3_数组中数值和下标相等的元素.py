#!/usr/bin/python
#coding:utf-8

# // 面试题53（三）：数组中数值和下标相等的元素
# // 题目：假设一个单调递增的数组里的每个元素都是整数并且是唯一的。请编程实
# // 现一个函数找出数组中任意一个数值等于其下标的元素。例如，在数组{-3, -1,
# // 1, 3, 5}中，数字3和它的下标相等。
class Solution:
    def GetNumberSameAsIndex(self, nums):
        if len(nums) == 0:return False
        left = 0
        right = len(nums) - 1
        while left<= right:
            mid = left + (right - left) // 2
            if nums[mid] == mid:
                return mid
            if nums[mid] > mid:
                right = mid - 1
            else:
                left = mid + 1
        return False

nums = [-3, -1, 1, 3, 5]
expected = 3
obj = Solution()
print(obj.GetNumberSameAsIndex(nums))