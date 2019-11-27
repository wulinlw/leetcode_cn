#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/orignial/card/all-about-lockup-table/237/learn-to-use-dict/987/
# 同构字符串
# 给定两个字符串 s 和 t，判断它们是否是同构的。
# 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

# 示例 1:
# 输入: s = "egg", t = "add"
# 输出: true

# 示例 2:
# 输入: s = "foo", t = "bar"
# 输出: false

# 示例 3:
# 输入: s = "paper", t = "title"
# 输出: true
# 说明:
# 你可以假设 s 和 t 具有相同的长度。
class Solution(object):
    # 同构代表两个字符串中每个位置上字符在自身第一次出现的索引相同
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # return [*map(s.index, s)] == [*map(t.index, t)]#和下面相同
        return [s.index(i) for i in s] == [t.index(i) for i in t]

    def isIsomorphic2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashmap = {}
        ismap = {}
        for i in range(len(s)):
            if s[i] in hashmap:
                if hashmap[s[i]] != t[i]:
                    return False
            else:
                if t[i] in ismap:
                    return False
                hashmap[s[i]] = t[i]
                ismap[t[i]] = True
        return True

s = "egg"
t = "add"
ss = Solution()
re = ss.isIsomorphic(s, t)
print(re)

