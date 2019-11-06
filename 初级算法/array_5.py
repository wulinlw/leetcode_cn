#!/usr/bin/python
#coding:utf-8
class Solution(object):
    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 1
        while (p < len(nums)):
            if nums[p] == nums[0]:
                del nums[p], nums[0]
                return self.singleNumber(nums)
            if p + 1 == len(nums):
                return nums[0]
            p += 1
        if len(nums) == 1:
            return nums[0]

    # 如果a、b两个值不相同，则异或结果为1。如果a、b两个值相同，异或结果为0
    def singleNumber(self, nums):
        s = 0
        for i in nums:
            s = s ^ i
            print(s)
        return s


# [1,2,2]
# [1,1,2,2,4]
# nums = [2,2,1]
nums = [4, 1, 2, 1, 2]
# nums = [17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6]

s = Solution()
n = s.singleNumber(nums)
print('return', n)
