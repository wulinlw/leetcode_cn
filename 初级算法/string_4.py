#!/usr/bin/python
#coding:utf-8
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