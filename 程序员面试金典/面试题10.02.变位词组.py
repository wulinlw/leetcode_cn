# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题10.02.变位词组
# 
# https://leetcode-cn.com/problems/group-anagrams-lcci/
# 
# 编写一种方法，对字符串数组进行排序，将所有变位词组合在一起。变位词是指字母相同，但排列不同的字符串。
# 注意：本题相对原题稍作修改
# 
# 示例:
# 
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# 
# 说明：
# 
# 
# 	所有输入均为小写字母。
# 	不考虑答案输出的顺序。
# 
# 
# 
# Medium 63.8%
# Testcase Example: ["eat","tea","tan","ate","nat","bat"]
# 
# 提示:
# 你如何检查两个单词是否互为变位词？想一想如何定义“变位词”。用你自己的话来解释一下。
# 两个单词互为变位词是指含有相同的字符，但顺序不同。怎么才能把字符排好序呢？
# 你能利用标准排序算法吗？
# 你真的需要真正的排序吗？或者仅需重新组织列表就够了？
# 
# 
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tmp = []
        for word in strs:                               #每个单词中字母排序了，索引不变
            tmp.append(''.join(sorted(word)))
        index = {}
        ans = []
        # print(tmp)
        for i in range(len(tmp)):
            if tmp[i] not in index:                     #不存在，新增一个数组，并记录索引
                ans.append([strs[i]])
                index[tmp[i]] = len(ans) - 1
            else:
                ans[index[tmp[i]]].append(strs[i])
        return ans




strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
o = Solution()
print(o.groupAnagrams(strs))