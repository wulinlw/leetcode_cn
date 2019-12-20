#!/usr/bin/python
#coding:utf-8

# // 面试题56（二）：数组中唯一只出现一次的数字
# // 题目：在一个数组中除了一个数字只出现一次之外，其他数字都出现了三次。请
# // 找出那个只出现一次的数字。


class Solution:
    # 出现3次的数字，把每一bit位相加，最后都能被3整除
    # 不能被3整除的，余数就是只出现一次的数字的bit位
    def FindNumberAppearingOnce(self, nums):
        if len(nums) ==0:return False
        bitSum = [0] * 32
        for i in nums:
            mask = 1
            for j in range(31,-1,-1):
                if i & mask == 1:       #bit位=1的，累加
                    bitSum[j] += 1
                mask = mask<<1
        # print(bitSum)

        re = 0
        for i in range(32):
            re = re << 1        #已经计算好的，左移一位
            re += bitSum[i]%3   #二进制加法
        return re

        
nums = [1,2,2,2,3,3,3,4,4,4]

obj = Solution()
print(obj.FindNumberAppearingOnce(nums))
# print(1^2)