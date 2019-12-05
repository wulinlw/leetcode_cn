#!/usr/bin/python
#coding:utf-8

# 数组中重复的数字
# 在一个长度为n的数组里的所有数字都在0到n-1的范围内。
# 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
# 请找出数组中任意一个重复的数字。
# 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是重复的数字2或者3。
class Solution(object):
    def duplicate(self, nums):
        if len(nums)== 0:
            return False
        re = []
        for i in range(len(nums)):
            while i != nums[i]: 
                if nums[i] == nums[nums[i]]:
                    re.append(nums[i])
                    break
                else:
                    index = nums[i]
                    nums[index],nums[i] = nums[i],nums[index]
        return re



nums = [2,3,1,0,2,5,3]
obj = Solution()
re = obj.duplicate(nums)
print(re)
