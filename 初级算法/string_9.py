#!/usr/bin/python
#coding:utf-8
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # print zip(*strs)
        re = ''
        for i in zip(*strs):
            # print set(i),len(set(i))
            if len(set(i)) != 1:
                return re
            else:
                re += i[0]
        return re


n = ["flower", "flow", "flight"]
# n=["dog","racecar","car"]
# n = []
n = ['a']
# n = ['a','a']
obj = Solution()
r = obj.longestCommonPrefix(n)
print r