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
        # 计算机二进制加法运算
        # https://blog.csdn.net/gaoyubo_taili/article/details/79694729
        # 两个整数a, b; a ^ b是无进位的相加； a&b得到每一位的进位；让无进位相加的结果与进位不断的异或， 直到进位为0；
        # 2^32 0x100000000
        # 2^32
        MASK = 0x100000000
        # 整型最大值
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1
        while b != 0:
            # print("--->}")
            # print("{:0>32b}".format(a))
            # print("{:0>32b}".format(b))
            # 计算进位
            carry = (a & b) << 1 #进位的和
            # 取余范围限制在 [0, 2^32-1] 范围内
            a = (a ^ b) % MASK #不进位的和
            b = carry % MASK
            # print("{:0>32b}".format(carry))
            # print("{:0>32b}".format(a))
            # print("{:0>32b}".format(b))
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)#~取反


a = -4
b = 6
s = Solution()
n = s.getSum(a, b)
print(n)









