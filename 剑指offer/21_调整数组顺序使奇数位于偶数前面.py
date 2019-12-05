#!/usr/bin/python
#coding:utf-8

# // 面试题21：调整数组顺序使奇数位于偶数前面
# // 题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有
# // 奇数位于数组的前半部分，所有偶数位于数组的后半部分。
# # 
class Solution:
    def ReorderOddEven_1(self, s):
        n = len(s)
        if n==0:return False
        if n==1:return s
        l = 0
        r = n-1
        while l<r:
            while l<r and s[l]&1 != 0:
                l += 1
            while l<r and s[r]&1 == 0:
                r -= 1
            if l<r:
                s[l],s[r] = s[r],s[l]
        return s

        

nums = [1,2,3,4,5]
obj = Solution()
#以下是true
print(obj.ReorderOddEven_1(nums))
print(obj.ReorderOddEven_1([1,2,3,4,5,6,7,8,9,10]))


