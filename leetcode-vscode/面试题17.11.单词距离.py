# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题17.11.单词距离
# 
# https://leetcode-cn.com/problems/find-closest-lcci/
# 
# 有个内含单词的超大文本文件，给定任意两个单词，找出在这个文件中这两个单词的最短距离(相隔单词数)。如果寻找过程在这个文件中会重复多次，而每次寻找的单词不同，你能对此优化吗?
# 示例：
# 
# 输入：words = ["I","am","a","student","from","a","university","in","a","city"], word1 = "a", word2 = "student"
# 输出：1
# 
# 提示：
# 
# 
# 	words.length <= 100000
# 
# 
# 
# Medium 67.9%
# Testcase Example: ["I","am","a","student","from","a","university","in","a","city"]
# "a"
# "student"
# 
# 提示:
# 如果只运行一次算法，请首先考虑寻找最近距离的算法。你应该能够在 O(N) 时间内完成这项工作，其中 N 是文档中的字数。
# 调整你的算法，使它成为可以重复调用的算法的一次执行。它哪里慢?你能优化它吗?
# 你可以构建一个查找表，把每个单词映射到它出现位置的列表。然后怎样找到最近的两个位置呢?
# 如果你有一个每个单词出现次数的列表，那么你实际上需要在两个数组中寻找一对值(每个数组中选一个值)，使它们之间的差异最小。这应该是一个与初始算法很相似的算法。
# 能用两个指针遍历两个数组吗?你应该能在 O(A+B)时间内完成，其中 A 和 B 是两个数组的大小。
# 
# 
from typing import List
class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        dic = {}
        for i,word in enumerate(words):                     #记录每个单词的位置
            if word not in dic:
                dic[word] = []
            dic[word].append(i)
        minlen = float('inf')                               #记录最小值
        i, j = 0, 0                                         #双指针，每一步计算两个索引的距离，记录最小值
        while i < len(dic[word1]) and j < len(dic[word2]):
            idx1 = dic[word1][i]
            idx2 = dic[word2][j]
            dist = abs(idx1 - idx2)
            minlen = min(minlen, dist)
            if idx1 > idx2:                                 #索引小的+1，这样越来越接近
                j += 1
            else:
                i += 1
        return minlen 


words = ["I","am","a","student","from","a","university","in","a","city"]
word1 = "a"
word2 = "student"


o = Solution()
print(o.findClosest(words, word1, word2))