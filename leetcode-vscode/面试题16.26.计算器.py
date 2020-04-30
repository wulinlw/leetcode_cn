# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题16.26.计算器
# 
# https://leetcode-cn.com/problems/calculator-lcci/
# 
# 给定一个包含正整数、加(+)、减(-)、乘(*)、除(/)的算数表达式(括号除外)，计算其结果。
# 表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。
# 
# 示例 1:
# 
# 输入: "3+2*2"
# 输出: 7
# 
# 
# 示例 2:
# 
# 输入: " 3/2 "
# 输出: 1
# 
# 示例 3:
# 
# 输入: " 3+5 / 2 "
# 输出: 5
# 
# 
# 说明：
# 
# 
# 	你可以假设所给定的表达式都是有效的。
# 	请不要使用内置的库函数 eval。
# 
# 
# 
# Medium 37.2%
# Testcase Example: "3+2*2"
# 
# 提示:
# 我们可以从左到右处理表达式吗？为什么会失败？
# 乘法和除法是优先级较高的运算。在3*4 + 5*9/2 + 3这样的表达式中，乘法和除法部分需要组合在一起。
# 把它想成当你遇到乘法或除法时，跳至一个单独的“进程”来计算该结果。
# 你还可以维护两个栈，一个用于操作符，另一个用于数字。每次看到一个数字，就把它压入栈。那么操作符呢？什么时候从栈中取出操作符并将它们与数字进行计算？
# 
# 
from typing import List
class Solution:
    def calculate(self, s: str) -> int:
        # 小trick
        s += "+0"
        stack = []
        num = 0                                             #记录当前数字
        sign = "+"                                          #记录最后的负号
        for c in s:
            if c.isdigit():                                 #当前为是数字，直接累加
                num = num * 10 + int(c)
            elif c in {"+", "-", "*", "/"}:
                #print(sign, num)
                if sign == "+":
                    stack.append(num)                       #+ - 放入栈中，后处理
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":                           #* / 直接和栈中的处理
                    stack[-1] = stack[-1] * num
                elif sign == "/":
                    # 解决python的负数下取整
                    if stack[-1] < 0:
                        stack[-1] = -(-stack[-1] // num)
                    else:
                        stack[-1] = stack[-1] // num
                sign, num = c, 0                            #当前数字归零，记录下最后的负号
        return sum(stack)

s = "3+2*2"
o = Solution()
print(o.calculate(s))