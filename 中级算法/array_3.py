#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/29/array-and-strings/77/
# 字谜分组
# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

# 示例:

# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# 说明：

# 所有输入均为小写字母。
# 不考虑答案输出的顺序。



class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 排序后放入hash，后面的在hash中找有没有
        hash = {}
        for str in strs:
            char = ''.join(sorted(str))
            if char not in hash:
                hash[char] = [str]
            else:
                hash[char].append(str)
                
        return hash.values()


nums = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
n = s.groupAnagrams(nums)
print(n)




