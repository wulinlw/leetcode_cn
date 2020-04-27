# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题05.06.整数转换
# 
# https://leetcode-cn.com/problems/convert-integer-lcci/
# 
# 整数转换。编写一个函数，确定需要改变几个位才能将整数A转成整数B。
#  示例1:
# 
# 
#  输入：A = 29 （或者0b11101）, B = 15（或者0b01111）
#  输出：2
# 
# 
#  示例2:
# 
# 
#  输入：A = 1，B = 2
#  输出：2
# 
# 
#  提示:
# 
# 
# A，B范围在[-2147483648, 2147483647]之间
# 
# 
# 
# Easy 49.9%
# Testcase Example: 29
# 15
# 
# 提示:
# 你要怎样计算两个数字之间有多少位不同？
# 想想异或表示什么。如果你把a异或b，那么结果中哪里是1？哪里是0？
# 
# 

class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        num = (A&0xFFFFFFFF) ^ (B&0xFFFFFFFF)
        re = 0
        while num:
            re += 1
            num = num&(num-1)
        return re

A = 29
B = 15
A = 1
B = 2
o = Solution()
print(o.convertInteger(A, B))