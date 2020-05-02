# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题17.17.多次搜索
# 
# https://leetcode-cn.com/problems/multi-search-lcci/
# 
# 给定一个较长字符串big和一个包含较短字符串的数组smalls，设计一个方法，根据smalls中的每一个较短字符串，对big进行搜索。输出smalls中的字符串在big里出现的所有位置positions，其中positions[i]为smalls[i]出现的所有位置。
# 示例：
# 
# 输入：
# big = "mississippi"
# smalls = ["is","ppi","hi","sis","i","ssippi"]
# 输出： [[1,4],[8],[],[3],[1,4,7,10],[5]]
# 
# 
# 提示：
# 
# 
# 	0 <= len(big) <= 1000
# 	0 <= len(smalls[i]) <= 1000
# 	smalls的总字符数不会超过 100000。
# 	你可以认为smalls中没有重复字符串。
# 	所有出现的字符均为英文小写字母。
# 
# 
# 
# Medium 42.8%
# Testcase Example: ""
# ["a","b","c"]
# 
# 提示:
# 从蛮力解法开始。运行时间是多少？
# 你能用trie吗?
# 一种解决方案是将较大字符串的每个后缀都插入trie。例如，如果单词是dogs，那么后缀应该是dogs、ogs、gs和s。这将如何帮助你解决该问题？其运行时间是多少？
# 或者，可以将每个较小的字符串插入到trie中。你将如何解决这个问题？时间复杂度是什么？
# 
# 
from typing import List
import collections
class TrieNode:
    def __init__(self):
        self.children = {}
        # self.isWord = False
        self.index = -1                                         #在结束时记录起始索引

class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        self.root = TrieNode()									#构建前缀树，Leetcode 208
        for idx,word in enumerate(smalls):
            node = self.root
            for i in word: 
                if i not in node.children:
                    node.children[i] = TrieNode()
                node = node.children[i]
            # node.isWord = True
            node.index = idx                                    #记录每个small单词起始索引

        re = [[] for _ in range(len(smalls))] 
        for i in range(len(big)):                               #每个字符为起点，每次从根节点开始
            node = self.root    
            for k in range(i, len(big)):                        
                if big[k] not in node.children:
                    break
                node = node.children[big[k]]                    #存在就往下找，到单词结尾就添加到结果集
                if node.index != -1:
                    re[node.index].append(i)
        return re
                




big = "mississippi"
smalls = ["is","ppi","hi","sis","i","ssippi"]
o = Solution()
print(o.multiSearch(big, smalls))