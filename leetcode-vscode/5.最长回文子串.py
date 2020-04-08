#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (28.68%)
# Likes:    1972
# Dislikes: 0
# Total Accepted:    227.4K
# Total Submissions: 777.2K
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 
# 示例 1：
# 
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 
# 
# 示例 2：
# 
# 输入: "cbbd"
# 输出: "bb"
# 
# 
#

# @lc code=start
class Solution:
    #中心扩展法
    def longestPalindrome(self, s: str) -> str:
        def helper(i, j):
            while i>=0 and j<len(s) and s[i] == s[j]:
                if j-i>=len(self.str):
                    self.str = s[i:j+1]
                i -= 1
                j += 1

        self.str = ""
        for i in range(len(s)):
            helper(i, i)
            helper(i, i+1)
        return self.str
    

# @lc code=end
s = "babad"
s = "cbbd"
s = "a"
o = Solution()
print(o.longestPalindrome(s))