#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-quesitons-in-2018/266/heap-stack-queue/1159/
# 基本计算器 II
# 实现一个基本的计算器来计算一个简单的字符串表达式的值。
# 字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

# 示例 1:
# 输入: "3+2*2"
# 输出: 7
# 示例 2:

# 输入: " 3/2 "
# 输出: 1
# 示例 3:

# 输入: " 3+5 / 2 "
# 输出: 5
# 说明：
# 你可以假设所给定的表达式都是有效的。
# 请不要使用内置的库函数 eval。

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                tmp = 0
                while i < len(s) and s[i].isdigit():#数字识别
                    tmp = tmp * 10 + int(s[i])
                    i += 1
                stack.append(tmp)#识别好的数字放入栈中
                # 如果栈中有乘除，先算出来
                while len(stack) > 1 and stack[-2] in {"*", "/"}:
                    stack.pop()
                    opt = stack.pop()
                    if opt == "*":
                        stack.append(stack.pop() * tmp)
                    else:
                        stack.append(stack.pop() // tmp)
            elif s[i] in { "*", "/", "+", "-"}:#符号放入栈中
                stack.append(s[i])
                i += 1
            else:#空格跳过
                 i += 1
        res = 0
        sign = 1
        for t in stack:
            if t == "+":
                sign = 1
            elif t == "-":
                sign = -1
            else:
                res += sign * t
        return res
    
    def calculate2(self, s: str) -> int:
        # 小trick
        s += "+0"
        stack = []
        num = 0
        # 记录前一个符号
        sign = "+"
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in {"+", "-", "*", "/"}:
                #print(sign, num)
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack[-1] = stack[-1] * num
                elif sign == "/":
                    # 解决python的负数下取整
                    if stack[-1] < 0:
                        stack[-1] = -(-stack[-1] // num)
                    else:
                        stack[-1] = stack[-1] // num
                sign, num = c, 0
        return sum(stack)



nums = 3+2*2
s = Solution()
n = s.calculate(nums)
print(n)