#!/usr/bin/python
#coding:utf-8
import sys
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        f = False
        if x < 0:
            f = True
        x2 = list(reversed(str(abs(x))))
        if f:
            x2.insert(0, "-")
        last = int(''.join(x2))
        if abs(last) > 2147483647:
            return 0
        else:
            return last

    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        sum = 0
        if x < 0:
            y = -x
        else:
            y = x
        # 一位一位计算
        while (y > 0):
            sum = sum * 10 + y % 10
            y = y / 10

        if sum > (2**31 - 1) or -sum < -2**31:
            return 0
        else:
            if x < 0:
                return -sum
            else:
                return sum


s = 123
# s = -123
s = 1534236469
obj = Solution()
n = obj.reverse(s)
print('return', n)
