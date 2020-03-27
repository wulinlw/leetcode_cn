#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#
# https://leetcode-cn.com/problems/wildcard-matching/description/
#
# algorithms
# Hard (26.70%)
# Likes:    289
# Dislikes: 0
# Total Accepted:    22.5K
# Total Submissions: 83.6K
# Testcase Example:  '"aa"\n"a"'
#
# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
# 
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
# 
# 
# 两个字符串完全匹配才算匹配成功。
# 
# 说明:
# 
# 
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
# 
# 
# 示例 1:
# 
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 
# 示例 2:
# 
# 输入:
# s = "aa"
# p = "*"
# 输出: true
# 解释: '*' 可以匹配任意字符串。
# 
# 
# 示例 3:
# 
# 输入:
# s = "cb"
# p = "?a"
# 输出: false
# 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
# 
# 
# 示例 4:
# 
# 输入:
# s = "adceb"
# p = "*a*b"
# 输出: true
# 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
# 
# 
# 示例 5:
# 
# 输入:
# s = "acdcb"
# p = "a*c?b"
# 输入: false
# 
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        s_idx = p_idx = 0                                       #s,p的指针
        p_tmp_idx = s_tmp_idx = -1                              #s,p碰到*的坐标，恢复的时候，从这个坐标+1开始
 
        while s_idx < s_len:
            if p_idx < p_len and p[p_idx] in ['?', s[s_idx]]:   #第一个字符是？或相等
                s_idx += 1                                      #都走一步
                p_idx += 1
            elif p_idx < p_len and p[p_idx] == '*':             #如果p是* , 记录 s p 位置
                p_tmp_idx = p_idx
                s_tmp_idx = s_idx
                p_idx += 1                                      #p 继续走，s 不动，看看能否匹配多个
            elif p_tmp_idx == -1:                                #前面2步 ？，*，相同字符都没出现，只能是个错的了
                return False
            else:                                               #碰到过*，回溯（更新p_idx, s_idx即可）
                p_idx = p_tmp_idx + 1
                s_idx = s_tmp_idx + 1
                s_tmp_idx = s_idx
        
        return all(x == '*' for x in p[p_idx:])                 #最后p只剩下*

# @lc code=end

o = Solution()
print(o.isMatch("aa", "*"))
print(o.isMatch("adceb", "*a*b"))
print(o.isMatch("aa", "a"))
print(o.isMatch("cb", "?a"))
print(o.isMatch("acdcb", "a*c?b"))