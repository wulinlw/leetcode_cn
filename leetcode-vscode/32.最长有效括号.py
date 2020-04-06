#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
# https://leetcode-cn.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (29.72%)
# Likes:    586
# Dislikes: 0
# Total Accepted:    50K
# Total Submissions: 166.5K
# Testcase Example:  '"(()"'
#
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
# 
# 示例 1:
# 
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 
# 
# 示例 2:
# 
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
# 
# 
#

# @lc code=start
class Solution:
    # 动态规划，定义 dp[i] 为到第 i 个格子为止，匹配的子串长度
    # 当 s[i] == ( 肯定为 0
    # 当 s[i] == )
    #     如果 s[i - 1] == ( ，刚好组成一对，本身长度为 2 ，考虑是否与上一个子串相连
    #     * 所以为 dp[i] = dp[i - 2] + 2
    #     * 即 上一个子串长度 + 本身长度
    #     如果 s[i - 1] == ) ，无法与其成为匹配的子串
    #     * 需要进一步考虑这个子串之前是否有 ( ，如果能够匹配成新的子串，那么
    #     * 当 s[i - 1] == ) && s[i - dp[i - 1] - 1] == ( 时，匹配成新的子串
    #     * 长度为 dp[i - dp[i - 1] - 2] + 2 + dp[i - 1]
    #     * 即 上上个子串长度 + 本身长度 + 上一个子串长度
    # 因为有 i - 2 所以插入两个 ) 再 dp 比较方便
    # https://leetcode-cn.com/problems/longest-valid-parentheses/solution/32-by-ikaruga/
    def longestValidParentheses(self, s: str) -> int:
        s = "))" + s                                            #前面套2个不影响结果的)),避免i-2越界
        dp = [0] * len(s)
        re = 0
        for i in range(2,len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                elif s[i - dp[i-1] - 1] == '(':
                    dp[i] = dp[i - dp[i-1] - 2] + 2 + dp[i-1]   #dp[i-1]上个子串长度，i-dp[i-1]-1就是倒数第二个)对应的(
                                                                # 上上个子串长度  本身长度2  上个子串长度 
            re = max(re, dp[i])
        return re

    def longestValidParentheses2(self, s: str) -> int:
        stack = [-1]                                            #先放一个-1，便于计算
        re = 0
        for i in range(len(s)):
            if s[i] == '(':                                     #碰到（，记录坐标
                stack.append(i)
            else:
                stack.pop()                                     #碰到），先弹出去栈顶
                if not stack:                                   #栈空了就把当前的放进去，避免再次出现）的时候弹出错误
                    stack.append(i)
                else:                                           #计算当前）到（的距离
                    re = max(re, i-stack[-1])
        return re


# @lc code=end
s = "(()"
s = ")()())"
o = Solution()
print(o.longestValidParentheses(s))