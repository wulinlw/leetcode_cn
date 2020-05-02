#!/usr/bin/python
#coding:utf-8

# 面试题 08.09. 括号
# 括号。设计一种算法，打印n对括号的所有合法的（例如，开闭一一对应）组合。

# 说明：解集不能包含重复的子集。

# 例如，给出 n = 3，生成结果为：

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
# https://leetcode-cn.com/problems/bracket-lcci/

from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        re = []
        tmp = ""
        #l,r 表示左右括号剩余个数
        def backtrack(tmp, l, r):
            if l>r:return                   #剩余的左边比右边多，错误
            if r==0:                        #右括号用完就结束了
                re.append(tmp)
            if l>0:                         #右左边的先用，左边剩余-1
                backtrack(tmp+'(', l-1, r)
            if r>0:                         #右边还有，右边-1
                backtrack(tmp+')', l, r-1)
            
        backtrack(tmp, n, n)
        return re


o = Solution()
print(o.generateParenthesis(3))