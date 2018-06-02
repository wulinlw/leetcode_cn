#!/usr/bin/python
#coding:utf-8
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        hl = len(haystack)
        nl = len(needle)
        if nl == 0:
            return 0
        if nl > hl:
            return -1
        idx = 0
        while True:
            # print idx,haystack[idx]
            if idx >= hl:
                return -1
            if (idx + nl) > hl:
                return -1
            if haystack[idx] == needle[0]:
                if self.diff(haystack, needle, idx):
                    return idx
            idx += 1

    def diff(self, haystack, needle, i):
        c = 0
        while True:
            if (c >= len(haystack)) or (c >= len(needle)):
                return False
            # print '--',i,c,haystack[i],needle[c]
            if haystack[i] != needle[c]:
                return False
            if c == len(needle) - 1:
                return True
            c += 1
            i += 1

    # 作弊
    def strStr_py(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not len(needle):
            return 0
        i = haystack.find(needle)
        return i


# haystack = "hello"
# needle = "ll"
# haystack = "aaaaa"
# needle = "a"
# haystack = "aaaaabcdefg"
# needle = "g"
haystack = "mississippi"
needle = "issipi"
haystack = "a"
needle = "a"
obj = Solution()
n = obj.strStr(haystack, needle)
print('return', n)