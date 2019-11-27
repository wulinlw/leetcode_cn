#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/33/
# 整数反转
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

# 示例 1:

# 输入: 123
# 输出: 321
#  示例 2:

# 输入: -123
# 输出: -321 
# 示例 3:

# 输入: 120
# 输出: 21
# 注意:

# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

import sys,math
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
            y = y // 10
        print(sum)

        if sum > (2**31 - 1) or -sum < -2**31:
            return 0
        else:
            if x < 0:
                return -sum
            else:
                return sum


s = 123
# s = -123
# s = 1534236469
obj = Solution()
n = obj.reverse2(s)
print('return', n)
