#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/29/array-and-strings/78/
# 无重复字符的最长子串
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

# 示例 1:

# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:

# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:

# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0# 存储历史循环中最长的子串长度
        if s is None or len(s) == 0:
            return max_len
        str_dict = {}# 存储不重复的字符和字符所在的下标
        # one_max = 0# 存储每次循环中最长的子串长度
        start = 0# 记录最近重复字符所在的位置+1
        for i in range(len(s)):
            # 判断当前字符是否在字典中,当前字符的下标是否>=最近重复字符的所在位置
            if s[i] in str_dict and str_dict[s[i]] >= start:
                start = str_dict[s[i]] + 1# 发生重复了，更新当前位置为起始位置
            one_max = i - start + 1# 在此次循环中，最大的不重复子串的长度
            str_dict[s[i]] = i# 把当前位置覆盖字典中的位置
            max_len = max(max_len, one_max)# 比较此次循环的最大不重复子串长度和历史循环最大不重复子串长度
        return max_len

nums = "aabcabcbb"
s = Solution()
n = s.lengthOfLongestSubstring(nums)
print(n)




