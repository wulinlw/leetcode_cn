#!/usr/bin/python
#coding:utf-8

# 面试题 01.09. 字符串轮转
# 字符串轮转。给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成（比如，waterbottle是erbottlewat旋转后的字符串）。

# 示例1:

#  输入：s1 = "waterbottle", s2 = "erbottlewat"
#  输出：True
# 示例2:

#  输入：s1 = "aa", "aba"
#  输出：False
# 提示：

# 字符串长度在[0, 100000]范围内。
# 说明:

# 你能只调用一次检查子串的方法吗？
# https://leetcode-cn.com/problems/string-rotation-lcci/

class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):return False
        s1 = s1+s1
        i,j = 0,0
        while i<len(s1) and j<len(s2):
            if s1[i]==s2[j]:
                i+=1
                j+=1 
            else:
                j=0 
                i+=1
        return j == len(s2) 

s1 = "waterbottle"
s2 = "erbottlewat"
o  = Solution()
print(o.isFlipedString(s1, s2))


