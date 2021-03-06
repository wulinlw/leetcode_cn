#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/53/math/116/
# x 的平方根
# 实现 int sqrt(int x) 函数。

# 计算并返回 x 的平方根，其中 x 是非负整数。
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

# 示例 1:
# 输入: 4
# 输出: 2
# 示例 2:

# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842..., 
#      由于返回类型是整数，小数部分将被舍去。

class Solution(object):
    #二分法
    def mySqrt(self, x):
        left=0
        right=x
        while left<right:
            mid = int((left+right)/2)
            if x< mid**2:
                right=mid
            else:
                left=mid+1
        if left>1:
            return left-1
        else:
            return left
    #牛顿法
    def mySqrt2(self, x):
        if x==0:return x
        t = x//2 + 1
        while t > x//t:
            t = (t + x//t) // 2
        return t





x = 10
s = Solution()
n = s.mySqrt2(x)
print(n)









