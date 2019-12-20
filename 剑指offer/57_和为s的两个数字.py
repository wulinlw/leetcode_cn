#!/usr/bin/python
#coding:utf-8

# // 面试题57（一）：和为s的两个数字
# // 题目：输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们
# // 的和正好是s。如果有多对数字的和等于s，输出任意一对即可。


class Solution:
    def FindNumbersWithSum(self, nums, target):
        if len(nums) ==0:return False
        left = 0
        right = len(nums)-1
        while left<right:
            if nums[left] + nums[right] == target:
                return nums[left], nums[right]
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        return False

        
nums = [1,2,4,7,11,15]
target = 15
obj = Solution()
print(obj.FindNumbersWithSum(nums, target))
