#!/usr/bin/python
#coding:utf-8

# // 面试题56（一）：数组中只出现一次的两个数字
# // 题目：一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序
# // 找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。


class Solution:
    # 所有数字异或，相同的数字异或后=0，所以最后得到的结果是2个单独数字的异或值
    # 把他们按照异或值的最右边的1分组，
    # 异或是不同为1，所以2个单独的数字会被分到不同组
    # 这样各组异或，相同值异或为0，留下单独的数
    def FindNumsAppearOnce(self, nums):
        if len(nums) ==0:return False
        OR = 0
        for i in nums:
            OR ^= i                     #OR等于2个只出现一次的数字的异或，出现2次的异或=0
        index = self.findFirstBitIs1(OR)
        tmp = 1 << index                #1左移index位
        n1 = n2 = 0
        for i in nums:
            if i & tmp:                 #右边第一位=1的分一组，不为1的份一组，
                n1 ^= i                 #异或肯定不为0，所以2个只出现一次的数字会被分到2个组
            else:
                n2 ^= i
        return n1,n2
        
    # 找到右边第一个=1的位
    def findFirstBitIs1(self, num):
        index = 0
        while num&1 == 0:               #num右移，找到第一个=1的位
            num = num>>1
            index += 1
        return index


        
nums = [1,2,3,3,4,4,5,5]

obj = Solution()
print(obj.FindNumsAppearOnce(nums))
# print(1^2)