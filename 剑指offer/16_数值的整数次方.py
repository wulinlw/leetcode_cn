#!/usr/bin/python
#coding:utf-8

# 数值的整数次方
# 写一个Power函数，不能调用函数库，同时不需要考虑大数问题。
# 实现函数 double Power(double base, int exponent)，求 base 的 exponent 次方。不得使用库函数，同时不需要考虑大数问题
class Solution:
    def Power(self, x, n):
        if n==0: return 1
        if n<0:
            return 1/self.Power(x,-n)
        if n%2 == 0:  #如果是偶数
            return self.Power(x*x, n//2)
        return self.Power(x*x,(n-1)//2)*x# 如果是奇数

    def Power2(self, base, exponent):
        if exponent==0: return 1
        if exponent==1: return base
        re = self.Power2(base, exponent>>1)
        re *= re
        if exponent & 1 == 1:#奇数，需要乘以自己
            re *= base
        return re

    
    def myPow(self, x, n):
        if n == 0: return 1
        if n < 0:
            return 1/self.myPow(x,-n)
        result = 1
        while(n):
            if n & 0x1:
                result *= x
            x *= x
            n = n >> 1
        return result



obj = Solution()
print(obj.Power(2, 2))
print(obj.Power(2, 3))
print(obj.Power2(2, 2))
print(obj.Power2(2, 3))
print(obj.Power(2, -2))
