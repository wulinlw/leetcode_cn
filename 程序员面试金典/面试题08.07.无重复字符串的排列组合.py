#!/usr/bin/python
#coding:utf-8

# 面试题 08.07. 无重复字符串的排列组合
# 无重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合，字符串每个字符均不相同。

# 示例1:

#  输入：S = "qwe"
#  输出：["qwe", "qew", "wqe", "weq", "ewq", "eqw"]
# 示例2:

#  输入：S = "ab"
#  输出：["ab", "ba"]
# 提示:

# 字符都是英文字母。
# 字符串长度在[1, 9]之间。
# https://leetcode-cn.com/problems/permutation-i-lcci/


from typing import List
class Solution:
    def permutation(self, S: str) -> List[str]:
        re = []
        def backtrack(s2, tmp):
            if len(s2) == 0:
                re.append(tmp[:])
                return
            for i in range(len(s2)):
                backtrack(s2[:i]+s2[i+1:], s2[i]+tmp)
        backtrack(S, "")
        return re
    
    def permutation2(self, S: str) -> List[str]:
        re = []
        def backtrack(s2, idx):
            if len(s2)-1 == idx:
                re.append("".join(s2[:]))
                return
            for i in range(idx, len(s2)):
                s2[i],s2[idx] = s2[idx],s2[i]
                backtrack(s2, idx+1)
                s2[i],s2[idx] = s2[idx],s2[i]
        backtrack(list(S), 0)
        return re

S = "qwe"
o = Solution()
print(o.permutation2(S))