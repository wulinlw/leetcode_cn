#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (73.44%)
# Likes:    866
# Dislikes: 0
# Total Accepted:    99.5K
# Total Submissions: 133.9K
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 
# 
# 
# 示例：
# 
# 输入：n = 3
# 输出：[
# ⁠      "((()))",
# ⁠      "(()())",
# ⁠      "(())()",
# ⁠      "()(())",
# ⁠      "()()()"
# ⁠    ]
# 
# 
#
from typing import List
import functools
# @lc code=start
class Solution:
    #回溯法
    def generateParenthesis2(self, n: int) -> List[str]:
        def backtrack(l, r, tmp):
            if r>l:return 
            if l==0 and r==0:
                re.append(tmp)
                return
            if l>0: 
                backtrack(l-1, r, "("+tmp)
            if r>0:
                backtrack(l, r-1, ")"+tmp)    
        re = []
        backtrack(n, n, "")
        return re
    
    #动态规划
    # 有效括号字符串可以由有效括号子串组成——有点像动态规划中的状态转移
    # 一个n个括号对的有效串，可以分解成'(' + left + ')' + right
    # 其中left与right是有效子串，且left.length() + right.length() == n-1
    @functools.lru_cache(None)
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0:
            return ['']
        re = [] 
        for c in range(n):
            for left in self.generateParenthesis(c):            #左边的递归得到
                for right in self.generateParenthesis(n-1-c):   #右边的n-1 - 左边
                    # re.append('({}){}'.format(left, right))
                    re.append('(' + left + ')' + right)
        return re



# @lc code=end

o = Solution()
print(o.generateParenthesis(3))