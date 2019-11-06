#!/usr/bin/python
#coding:utf-8
import sys
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {}
        ix = {}
        k = ""
        for idx, i in enumerate(s):
            if i in m:
                m[i] += 1
                continue
            else:
                m[i] = 1
                ix[i] = idx
        print(m)
        print(ix)
        mixNum = sys.maxint
        for i in m:
            print(i)
            if m[i] > 1:
                continue
            if ix[i] < mixNum:
                mixNum = ix[i]

        if mixNum == sys.maxint:
            return -1
        else:
            return mixNum

    def firstUniqChar(self, s):
        r = 10**10
        letters = 'abcdefghijklmnopqrstuvwxyz'
        for l in letters:
            if l not in s:
                pass
            elif s.count(l) > 1:
                pass
            else:
                r = min(s.index(l), r)
        if r == 10**10: return -1
        else:
            return r


s = "leetcode"
# s = "loveleetcode"
obj = Solution()
n = obj.firstUniqChar(s)
print('return', n)
