#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/54/others/119/
# 两整数之和
# 不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。

# 示例 1:
# 输入: a = 1, b = 2
# 输出: 3
# 示例 2:

# 输入: a = -2, b = 3
# 输出: 1

# https://blog.csdn.net/qq_34364995/article/details/80738911
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 利用&求进位，^异或求值
        # 但是在Python中并不可行，因为Python会直接将
        # int扩展为long
        while b != 0:
            carry = a & b
            a = (a ^ b) % 0x100000000
            b = (carry << 1) % 0x100000000
        return a if a <= 0x7FFFFFFF else a | (~0x100000000+1)

a = 1
b = 2
s = Solution()
n = s.getSum(a, b)
print(n)









