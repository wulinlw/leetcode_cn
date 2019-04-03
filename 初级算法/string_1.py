#!/usr/bin/python
#coding:utf-8
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = list(s)
        arr.reverse()
        return ''.join(arr)

    def reverseString2(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = s[::-1]
        return arr


s = "hello"
ss = Solution()
n = ss.reverseString(s)
print('return', n)
