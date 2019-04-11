#!/usr/bin/python
#coding:utf-8

# 最长回文子串
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

# 示例 1：

# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：

# 输入: "cbbd"
# 输出: "bb"

# https://zhuanlan.zhihu.com/p/43844178
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        maxl = 0  #最大字符串长度
        start = 0 #起始位置
        for i in xrange(n):
            # print(i,start,maxl )
            # print(s[i-maxl-1: i+1], s[i-maxl-1: i+1][::-1])
            # print(s[i-maxl: i+1], s[i-maxl: i+1][::-1])
            if i - maxl >= 1 and s[i-maxl-1: i+1] == s[i-maxl-1: i+1][::-1]:
                print(i)
                start = i - maxl - 1
                maxl += 2
                continue
            if i - maxl >= 0 and s[i-maxl: i+1] == s[i-maxl: i+1][::-1]:
                start = i - maxl
                maxl += 1
        return s[start: start + maxl]
    




nums = "babadabd"
s = Solution()
n = s.longestPalindrome(nums)
print(n)



