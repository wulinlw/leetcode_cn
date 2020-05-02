#!/usr/bin/python
#coding:utf-8

# 面试题 01.02. 判定是否互为字符重排
# 给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。

# 示例 1：

# 输入: s1 = "abc", s2 = "bca"
# 输出: true 
# 示例 2：

# 输入: s1 = "abc", s2 = "bad"
# 输出: false
# 说明：

# 0 <= len(s1) <= 100
# 0 <= len(s2) <= 100
# https://leetcode-cn.com/problems/check-permutation-lcci/

class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return set(s1)==set(s2) and len(s1)==len(s2)



o  = Solution()
print(o.CheckPermutation("abc","acb"))
