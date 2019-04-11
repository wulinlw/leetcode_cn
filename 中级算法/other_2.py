#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/54/others/120/
# 逆波兰表达式求值
# 根据逆波兰表示法，求表达式的值。
# 有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

# 说明：
# 整数除法只保留整数部分。
# 给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
# 示例 1：

# 输入: ["2", "1", "+", "3", "*"]
# 输出: 9
# 解释: ((2 + 1) * 3) = 9
# 示例 2：

# 输入: ["4", "13", "5", "/", "+"]
# 输出: 6
# 解释: (4 + (13 / 5)) = 6
# 示例 3：

# 输入: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# 输出: 22
# 解释: 
#   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22

# https://blog.csdn.net/qq_32424059/article/details/86994342
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # 首先声明一个栈stack，然后线性扫描input数组，
        # 如果当前元素是运算符，就把栈的最上面两个元素进行相应运算，把它们俩弹出来，再把运算结果push进栈，
        # 如果当前元素不是运算符，直接push就行了。
        # 注意最后返回的结果要转换成int的形式，
        # 而且除法需要只保留整数位。
        stack = []
        for item in tokens:
            if item in ["+", "-", "*", "/"]:
                if item == "+":
                    temp = int(stack[-2]) + int(stack[-1])
                elif item == "-":
                    temp = int(stack[-2]) - int(stack[-1])
                    # print temp                
                elif item == "*":
                    temp = int(stack[-2]) * int(stack[-1])             
                elif item == "/":
                    temp = int(float(stack[-2])/ float(stack[-1]))                    
                stack.pop()
                stack.pop()
                stack.append(temp)
            else:
                stack.append(item)
        return int(stack[0])

tokens = ["2", "1", "+", "3", "*"]
s = Solution()
n = s.evalRPN(tokens)
print(n)









