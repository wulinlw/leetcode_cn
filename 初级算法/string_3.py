#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/34/
# 字符串中的第一个唯一字符
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

# 案例:

# s = "leetcode"
# 返回 0.

# s = "loveleetcode",
# 返回 2.
 

# 注意事项：您可以假定该字符串只包含小写字母。

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

    def firstUniqChar2(self, s):
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
