#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/35/
# 有效的字母异位词
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

# 示例 1:

# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:

# 输入: s = "rat", t = "car"
# 输出: false
# 说明:
# 你可以假设字符串只包含小写字母。

# 进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        if isinstance(s, unicode):
            s = s.encode('utf-8')
        if isinstance(t, unicode):
            t = t.encode('utf-8')
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for i in alpha:
            if s.count(i) != t.count(i):
                return False
        return True

    def isAnagram2(self, s, t):
        if len(s) != len(t):
            return False
        h = {}
        for i in range(len(s)):
            if s[i] not in h:
                h[s[i]] = 1
            else:
                h[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in h:
                return False
            elif h[t[i]]==0:
                return False
            else:
                h[t[i]] -= 1
        return True

s = "anagram"
t = "nagaram"
# s = "rat"
# t = "car"
s = "a"
t = "b"
# s = "anagtam"
# t = "nbgbram"
obj = Solution()
n = obj.isAnagram(s, t)
print('return', n)