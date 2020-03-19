#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#
# https://leetcode-cn.com/problems/letter-case-permutation/description/
#
# algorithms
# Easy (62.81%)
# Likes:    149
# Dislikes: 0
# Total Accepted:    15.1K
# Total Submissions: 23.9K
# Testcase Example:  '"a1b2"'
#
# 给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。
# 
# 
# 示例:
# 输入: S = "a1b2"
# 输出: ["a1b2", "a1B2", "A1b2", "A1B2"]
# 
# 输入: S = "3z4"
# 输出: ["3z4", "3Z4"]
# 
# 输入: S = "12345"
# 输出: ["12345"]
# 
# 
# 注意：
# 
# 
# S 的长度不超过12。
# S 仅由数字和字母组成。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # 一位一位处理
    # 碰到字母时，分出小写路径和大写路径
    def letterCasePermutation2(self, S: str) -> List[str]:
        re = []
        def backtrack(s2, idx):
            if idx==len(S):
                re.append("".join(s2[:]))
                return
            backtrack(s2, idx+1)            #先放小写的情况，数字也直接放
            if s2[idx].isalpha():           #在放大写的情况，分出一条新路径
                s2[idx] = s2[idx].upper()
                backtrack(s2, idx+1)
        backtrack(list(S), 0)
        return re

    def letterCasePermutation(self, S: str) -> List[str]:
        ans = [[]]
        for char in S:
            n = len(ans)
            if char.isalpha():
                for i in range(n):
                    ans.append(ans[i][:])
                    ans[i].append(char.lower())
                    ans[n+i].append(char.upper())
            else:
                for i in range(n):
                    ans[i].append(char)
        for i in range(len(ans)):
            ans[i] = "".join(ans[i])
        return ans
# @lc code=end
S = "a1b2"
# S = "3z4"
# S = "12345"
o = Solution()
print(o.letterCasePermutation2(S))