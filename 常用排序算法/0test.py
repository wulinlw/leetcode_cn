#!/usr/bin/python
#coding:utf-8
class Solution(object):
    def duplicate(self, nums):
        re = []
        for i in range(len(nums)):
            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    re.append(nums[i])
                    break
                else:
                    idx = nums[i]
                    nums[idx],nums[i] = nums[i],nums[idx]
        return re



nums = [2,3,1,0,2,5,3]
obj = Solution()
re = obj.duplicate(nums)
print(re)