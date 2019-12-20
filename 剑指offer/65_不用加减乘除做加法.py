#!/usr/bin/python
#coding:utf-8

# 不用加减乘除做加法
# 写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。

class Solution(object):
    def Add(self, num1, num2):
        # 0xFFFFFFFF    int最大值
        # 0x7FFFFFFF    int最小值
        while num2:
            sum = num1 ^ num2
            carry = 0xFFFFFFFF&(num1 & num2)<<1
            carry = -(~(carry - 1) & 0xFFFFFFFF) if carry > 0x7FFFFFFF else carry
            num1 = sum
            num2 = carry
        return num1

    def Add2(self, num1, num2):
        while num2:
            sum = num1 ^ num2           #异或，取不进位部分的和，不管进位
            carry = (num1 & num2)<<1    #取进位
            num1 = sum
            num2 = carry                #有进位就一直循环，直到没有进位
        return num1 

num1, num2 =1,2
S = Solution()
deep = S.Add2(num1, num2)
print("deep:",deep)
