# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题17.22.单词转换
# 
# https://leetcode-cn.com/problems/word-transformer-lcci/
# 
# 给定字典中的两个词，长度相等。写一个方法，把一个词转换成另一个词， 但是一次只能改变一个字符。每一步得到的新词都必须能在字典中找到。
# 编写一个程序，返回一个可能的转换序列。如有多个可能的转换序列，你可以返回任何一个。
# 
# 示例 1:
# 
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 输出:
# ["hit","hot","dot","lot","log","cog"]
# 
# 
# 示例 2:
# 
# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# 输出: []
# 
# 解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
# 
# 
# Medium 31.5%
# Testcase Example: "hit"
# "cog"
# ["hot","dot","dog","lot","log","cog"]
# 
# 提示:
# 从一个蛮力的递归解法开始。只需要创建所有一次编辑的单词，检查它们是否在字典中，然后尝试该编辑路径。
# 一旦你有了一个蛮力解法，就可以尝试找到一个更快的方法以得到所有一次编辑的有效单词。当绝大多数字符串都不是有效的字典单词时，你不会想创建所有一次编辑的字符串。
# 为了快速得到编辑距离为1的有效单词，试着将字典中的单词以一种有效的方式进行分组。注意，b_ll形式的所有单词（如bill、ball、bell和bull）的编辑距离为1。然而，这些并不是仅有的编辑距离为1的单词。
# 创建从通配符形式（如b_ll）到该通配符所匹配的所有单词的映射。然后，当你想要查找与bill相隔编辑距离为1的所有单词时，可以在映射中查找_ill、b_ll、bi_l和bil_。
# 你之前的算法可能类似于深度优先搜索。你能使它更快吗?
# 广度优先的搜索通常比深度优先的搜索要快。在最坏的情况下未必如此，但在很多情况下都是这样。为什么？你能找到更快的方法吗？
# 如果同时从起始单词和目标单词开始进行广度优先搜索，结果会怎样？
# 
# 
from typing import List
from collections import defaultdict
class Solution:
    # 127. 单词接龙
    # 预处理 + bfs
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        if not beginWord or not endWord or not wordList:
            return []
        wordDict = defaultdict(list)
        for i in range(len(endWord)):               #都是一样长，随便用哪个的len
            for word in wordList:                   #预处理，每一位替换成*，aa* -> aaa
                tmpWord = word[:i]+'*'+word[i+1:]
                wordDict[tmpWord].append(word)
        # print(wordDict)
        queue = [[beginWord,[beginWord]]]           #
        visited = [beginWord]
        while queue:
            curWord, curRes = queue.pop(0)          #单词，只差一位的所有单词
            for i in range(len(endWord)):
                tmpWord = curWord[:i]+'*'+curWord[i+1:]
                wordList = wordDict[tmpWord]
                for word in wordList:               #只差一位的所有单词bfs，
                    tmpRes = copy.deepcopy(curRes)
                    tmpRes.append(word)
                    if word==endWord:               #找到就返回
                        return tmpRes
                    if word not in visited:         #没有访问过的需要标记
                        visited.append(word)
                        queue.append([word, tmpRes])
                wordDict[tmpWord] = []
        return []




beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
o = Solution()
print(o.findLadders(beginWord, endWord, wordList))
