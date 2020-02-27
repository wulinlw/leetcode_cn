#!/usr/bin/python
#coding:utf-8

import sys,math
from typing import List
# 重点问题
# 19
# 20
# 27
# 30
# 34
# 35
# 37
# 43
# 44
# 46
# 47
# 48
# 49
# 51
# 53
# 53_2
# 54
# 57_2
# 59
65
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnique(self, astr: str) -> bool:
        map = {}
        for i in range(len(astr)):
            if astr[i] in map:
                return False
            map[astr[i]] = 1
        print(map)
        return True
    
nums = [7,1,5,3,6,4]
nums = [9, 11, 8, 5, 7, 12, 16, 14]
S = Solution()
print(S.isUnique("leetcode"))

