#!/usr/bin/python
#coding:utf-8
class Solution(object):
    # 780ms
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums)

    # 56ms
    def removeDuplicates_best(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = 0
        this_num = None
        for num in nums:
            if num != this_num:
                nums[pos] = num
                this_num = num
                pos += 1
        return pos


nums = [1, 1, 2]
s = Solution()
n = s.removeDuplicates(nums)
print(n)
print(nums)