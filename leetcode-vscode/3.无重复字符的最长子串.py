#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (33.08%)
# Likes:    3551
# Dislikes: 0
# Total Accepted:    455.9K
# Total Submissions: 1.3M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 
# 示例 1:
# 
# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 
# 
# 示例 2:
# 
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 
# 
# 示例 3:
# 
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {}
        maxlen, curlen = 0, 0
        start = 0
        for i in range(len(s)):
            if s[i] in h and h[s[i]] >= start:      #重复了，新的字符索引大，去掉最左边的（左边界+1）
                start = h[s[i]] + 1         
            curlen = i - start + 1                  #当前长度，更新最大值maxlen
            h[s[i]] = i
            maxlen = max(maxlen, curlen)        
        return maxlen






# @lc code=end
s = "abcabcbb"
o = Solution()
print(o.lengthOfLongestSubstring(s))
