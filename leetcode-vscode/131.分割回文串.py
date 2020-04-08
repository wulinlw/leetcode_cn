#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
# https://leetcode-cn.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (65.59%)
# Likes:    252
# Dislikes: 0
# Total Accepted:    27.4K
# Total Submissions: 41.1K
# Testcase Example:  '"aab"'
#
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
# 
# 返回 s 所有可能的分割方案。
# 
# 示例:
# 
# 输入: "aab"
# 输出:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
# 
#
from typing import List
# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def check(s, i, j):
            if i >= j:
                return True
            if s[i] == s[j]:
                i += 1
                j -= 1
                return check(s, i, j)
            else:
                return False

        def backtrack(s, idx, tmp):
            if idx >= len(s):
                re.append(tmp[:])
                return
            for i in range(idx, len(s)):        #分割字符串，起点idx，终点i
                if check(s, idx, i):            #是回文才继续分割，不是回文就剪枝
                    tmp.append(s[idx:i+1])      #包含i(+1)
                    backtrack(s, i+1, tmp)      #子问题
                    tmp.pop()
        
        re = []
        if len(s)==0:return 
        backtrack(s, 0, [])
        return re

# @lc code=end
s = "aab"
o = Solution()
print(o.partition(s))