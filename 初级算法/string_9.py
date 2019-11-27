#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/5/strings/40/
# 最长公共前缀
# 编写一个函数来查找字符串数组中的最长公共前缀。

# 如果不存在公共前缀，返回空字符串 ""。

# 示例 1:

# 输入: ["flower","flow","flight"]
# 输出: "fl"

# 示例 2:
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:
# 所有输入只包含小写字母 a-z 。
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # print zip(*strs)
        re = ''
        for i in zip(*strs):#数组中每个元素list化， 当前字符的元组
            print(i,set(i),len(set(i)))
            if len(set(i)) != 1:#set去重
                return re
            else:
                re += i[0]
        return re


n = ["flower", "flow", "flight"]
# print(zip(*n))
# n=["dog","racecar","car"]
# n = []
# n = ['a']
# n = ['a','a']
obj = Solution()
r = obj.longestCommonPrefix(n)
print(r)