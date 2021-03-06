#!/usr/bin/python
#coding:utf-8

# 面试题 08.05. 递归乘法
# 递归乘法。 写一个递归函数，不使用 * 运算符， 实现两个正整数的相乘。可以使用加号、减号、位移，但要吝啬一些。

# 示例1:
#  输入：A = 1, B = 10
#  输出：10

# 示例2:
#  输入：A = 3, B = 4
#  输出：12
# 提示:
# 保证乘法范围不会溢出
# https://leetcode-cn.com/problems/recursive-mulitply-lcci/

class Solution:
    # A∗B=(A∗2)(B/2)=(A∗2)(B//2)+A∗(B%2)
    # 其中A*2 = A << 1, B//2 = B >> 1, B%2 = B&1
    def multiply(self, A: int, B: int) -> int:
        if B == 1: return A
        if B == 0: return 0
        if B & 1:
            return self.multiply(A<<1, B>>1) + A 
        else:
            return self.multiply(A<<1, B>>1)


a = 8
b = 9
o = Solution()
print(o.multiply(a,b))