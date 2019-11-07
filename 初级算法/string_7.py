#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/38/
# 实现 strStr()
# 实现 strStr() 函数。

# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

# 示例 1:

# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 示例 2:

# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
# 说明:

# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
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