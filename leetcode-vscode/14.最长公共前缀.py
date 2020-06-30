#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (36.31%)
# Likes:    1043
# Dislikes: 0
# Total Accepted:    263.8K
# Total Submissions: 705.5K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 示例 1:
# 
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 
# 
# 示例 2:
# 
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 
# 
# 说明:
# 
# 所有输入只包含小写字母 a-z 。
# 
#
from typing import List
# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        re = ''
        for i in zip(*strs):#数组中每个元素list化， 当前字符的元组
            print(i,set(i),len(set(i)))
            if len(set(i)) != 1:#set去重
                return re
            else:
                re += i[0]
        return re
# @lc code=end

obj = Solution()
print(obj.longestCommonPrefix(n))
