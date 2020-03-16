#!/usr/bin/python
#coding:utf-8

# 面试题 08.08. 有重复字符串的排列组合
# 有重复字符串的排列组合。编写一种方法，计算某字符串的所有排列组合。

# 示例1:
#  输入：S = "qqe"
#  输出：["eqq","qeq","qqe"]

# 示例2:
#  输入：S = "ab"
#  输出：["ab", "ba"]
# 提示:
# 字符都是英文字母。
# 字符串长度在[1, 9]之间。
# https://leetcode-cn.com/problems/permutation-ii-lcci/

from typing import List
class Solution:
    def permutation(self, S: str) -> List[str]:
        # S="".join((lambda x:(x.sort(), x)[1])(list(S)))###字符串排序,相同的在一起（排序去重）
        S = "".join(sorted(S))
        # print(S)
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp[:])
                return 
            for i in range(len(nums)):
                if i>0 and nums[i] == nums[i-1]:continue    #每当进入新的构成，先考虑该构成的首字符是否和上一个一样。
                backtrack(nums[:i] + nums[i+1:], nums[i]+tmp)  #nums[:i]+nums[i+1:] 避免了重复利用。
        res = []
        backtrack(S, "")
        return res

S = "qqe"
o = Solution()
print(o.permutation(S))