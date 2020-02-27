#!/usr/bin/python
#coding:utf-8

# 斐波那契数列
# 大家都知道斐波那契数列，现在要求输入一个整数n，
# 请你输出斐波那契数列的第n项（从0开始，第0项为0）。


class Solution:
    def fabonacii(self,n):
        a=0
        b=1
        tmp = 0
        for i in range(1,n+1):
            tmp = a+b
            a = b
            b = tmp
        return tmp

    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
        # return a % 1000000007 # leetcode中答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。


        
obj = Solution()
print(obj.fabonacii(0))
print(obj.fabonacii(1))
print(obj.fabonacii(5))