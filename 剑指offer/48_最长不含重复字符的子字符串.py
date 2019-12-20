#!/usr/bin/python
#coding:utf-8

# // 面试题48：最长不含重复字符的子字符串
# // 题目：请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子
# // 字符串的长度。假设字符串中只包含从'a'到'z'的字符。

class Solution:
    def longestSubstringWithoutDuplication(self, s):
        if len(s) == 0:return
        maxLen = 0
        curLen = 0
        dp = [-1] * 26
        for i in range(len(s)):
            p = ord(s[i])-ord('a')
            if dp[p] == -1 or i-dp[p]>maxLen:
                curLen += 1
            else:
                curLen = i-dp[p]
            if curLen>maxLen:
                maxLen = curLen
            dp[p] = i
        return maxLen

        

s = "arabcacfr"
obj = Solution()
print(obj.longestSubstringWithoutDuplication(s))
