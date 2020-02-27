#!/usr/bin/python
#coding:utf-8

# // 面试题61：扑克牌的顺子
# // 题目：从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
# // 2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王可以看成任意数字。
# 0是大小王

class Solution(object):
    # 大小王的个数大于等于顺子间分割的数，就是顺子
    def IsContinuous(self, nums):
        if len(nums)<5:return False
        nums.sort()
        count0 = 0                      #0的个数
        for i in nums:  
            if i == 0:
                count0 += 1
        
        countGap = 0
        small = count0          
        big = count0+1                  #第一个非0位，下标
        while big<len(nums):
            if nums[small] == nums[big]:    #有一样的，不可能是顺子
                return False
            countGap += nums[big] - nums[small] - 1 #顺子的间隔是0.所以这里-1
            small = big
            big += 1
        return True if count0>=countGap else False




nums = [2,3,4,5,6]
S = Solution()
print(S.IsContinuous([2,3,4,5,6]))
print(S.IsContinuous([2,3,4,5,7]))#false
print(S.IsContinuous([2,3,4,0,0]))
print(S.IsContinuous([2,3,4,5,0]))
