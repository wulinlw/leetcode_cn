#
# @lc app=leetcode.cn id=301 lang=python3
#
# [301] 删除无效的括号
#
# https://leetcode-cn.com/problems/remove-invalid-parentheses/description/
#
# algorithms
# Hard (45.48%)
# Likes:    131
# Dislikes: 0
# Total Accepted:    7.7K
# Total Submissions: 17K
# Testcase Example:  '"()())()"'
#
# 删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。
# 
# 说明: 输入可能包含了除 ( 和 ) 以外的字符。
# 
# 示例 1:
# 
# 输入: "()())()"
# 输出: ["()()()", "(())()"]
# 
# 
# 示例 2:
# 
# 输入: "(a)())()"
# 输出: ["(a)()()", "(a())()"]
# 
# 
# 示例 3:
# 
# 输入: ")("
# 输出: [""]
# 
#
from typing import List
# @lc code=start
class Solution:
    #bfs
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):                                 #计数法，判断括号字符串是否有效
            count = 0
            for c in s:
                if c == '(':
                    count += 1
                elif c == ')':
                    count -= 1
                if count < 0:                           #）比（多，肯定不对
                    return False
            return count == 0
        
        # #开始bfs
        level = {s}                                     #{}表示set()
        while level:
            res = []
            for s in level:                             #先判断level中有合法的字符串，找到结果了就直接返回，不需要再删减了
                if isValid(s):
                    res.append(s)
            if res != []: return res

            nextlevel = set()                           
            for s in level:
                for i in range(len(s)):                 #删掉每一位，组成新的字符串下次遍历
                    if s[i] in {'(',')'}:               #有其他字符，所以这里判断下，只处理（）
                        nextlevel.add(s[:i] + s[i+1:])
            level = nextlevel


        
# @lc code=end
s = "()())()"
# s = "(a)())()"
s = ")("
s = ")()("
s = "))(()("
o = Solution()
print(o.removeInvalidParentheses(s))