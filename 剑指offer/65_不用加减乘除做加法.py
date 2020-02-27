#!/usr/bin/python
#coding:utf-8

# 不用加减乘除做加法
# 写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
# a, b 均可能是负数或 0
# 结果不会溢出 32 位整数

class Solution(object):
    def Add(self, num1, num2):
        # 0xFFFFFFFF    int最小值，负 11111111111111111111111111111111
        # 0x7FFFFFFF    int最大值，正 01111111111111111111111111111111
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

    #以此为准
    def add(self, a: int, b: int) -> int:
        a &= 0xFFFFFFFF                         #二进制长度限制，取有效部分，题目要求的32位整数
        b &= 0xFFFFFFFF
        while b:
            carry = a & b       
            a ^= b                              #异或，取不进位部分的和，不管进位
            b = ((carry) << 1) & 0xFFFFFFFF     #取进位
        return a if a < 0x80000000 else ~(a^0xFFFFFFFF)
        # ~(a^0xFFFFFFFF) 溢出的数字变化正负
        #  11011
        # ^11111
        # ------
        #  00100
        # ~
        # ------
        #  11011          



num1, num2 =1,2
num1, num2 =-1,2
S = Solution()
deep = S.add(num1, num2)
print("deep:",deep)

print(0x7FFFFFFF)                           #2147483647
print(0xFFFFFFFF)                           #4294967295
print("{:0>32b}".format(0x7FFFFFFF))        #01111111111111111111111111111111
print("{:0>32b}".format(0xFFFFFFFF))        #11111111111111111111111111111111
print(4294967295, ~(4294967296^0xFFFFFFFF)) #2147483648 -2147483648