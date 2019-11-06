#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/featured/card/top-interview-quesitons-in-2018/272/dynamic-programming/1174/
# 至少有K个重复字符的最长子串
# 找到给定字符串（由小写字符组成）中的最长子串 T ， 要求 T 中的每一字符出现次数都不少于 k 。输出 T 的长度。
# 示例 1:
# 输入:
# s = "aaabb", k = 3
# 输出:
# 3
# 最长子串为 "aaa" ，其中 'a' 重复了 3 次。
# 示例 2:
# 输入:
# s = "ababbc", k = 2
# 输出:
# 5
# 最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。


# https://blog.csdn.net/weixin_41303016/article/details/88686110
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        for i in set(s):#去重
            if s.count(i) < k: # 找出不满足k次的字母,将其作为分割点进行分治
                return max(self.longestSubstring(m, k) for m in s.split(i))
        return len(s)

ss = "aaabbc"
k = 3
s = Solution()
res = s.longestSubstring(ss, k)
print(res)