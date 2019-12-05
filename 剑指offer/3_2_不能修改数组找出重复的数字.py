#!/usr/bin/python
#coding:utf-8

# 不能修改数组找出重复的数字
# 在一个长度为 n+1 的数组里，所有数字都在 1～n 范围内，所以数组中至少有一个数字是重复的。
# 请找出数组中任意一个重复的数字，但不能修改输入的数组。
# 例如，如果输入长度为8的数组 {2,3,5,4,3,2,6,7}, 
# 那么对应的输出是重复的2 或者3.

# 用hash做这道题，时间复杂度o(n)
# 二分+记数，时间复杂度o(logn)
class Solution(object):
    def duplicate(self, nums):
        if len(nums)== 0:
            return False

        # 计算数组中l至r区间有多少个元素，如1-4区间，1-4的数多余4，说明有重复
        def counter(l, r):
            c = 0
            for i in nums:
                if i>=l and i<=r:
                    c +=1
            return c

        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (r-l)//2 + l
            c = counter(l,mid)
            if l==r:        #指针重合时指只有一个元素，
                if c>1:     #这时这个元素在整个数组中出现超过1次，那就是重复了
                    return l
            if c>(mid-l+1): #超过区域中元素个数，有重复，需要继续往左找
                r = mid
            else:
                l = mid+1
        return -1


nums = [2,3,1,0,2,5,3]
obj = Solution()
re = obj.duplicate(nums)
print(re)
