#!/usr/bin/python
#coding:utf-8

# // 面试题53（二）：0到n-1中缺失的数字
# // 题目：一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字
# // 都在范围0到n-1之内。在范围0到n-1的n个数字中有且只有一个数字不在该数组
# // 中，请找出这个数字。
class Solution:
    def GetMissingNumber(self, nums):
        if len(nums) == 0:return False
        left = 0
        right = len(nums)-1
        while left<right:
            mid = left+(right-left)//2
            if nums[mid] != mid:
                if mid==0 or nums[mid-1]==mid-1:    #最左边，或左边一个刚好相等，这个不相等，就是mid了
                    return mid
                right = right - 1
            else:
                left = mid + 1
        if left ==right:                            #找到了最右边，就是最后一个不相等
            return len(nums)


nums = [0,1,2,4,5]
expected = 3
obj = Solution()
print(obj.GetMissingNumber(nums))