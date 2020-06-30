#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#
# https://leetcode-cn.com/problems/word-ladder/description/
#
# algorithms
# Medium (40.19%)
# Likes:    317
# Dislikes: 0
# Total Accepted:    41.2K
# Total Submissions: 98.3K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord
# 的最短转换序列的长度。转换需遵循如下规则：
# 
# 
# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。
# 
# 
# 说明:
# 
# 
# 如果不存在这样的转换序列，返回 0。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
# 
# 
# 示例 1:
# 
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 输出: 5
# 
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# ⁠    返回它的长度 5。
# 
# 
# 示例 2:
# 
# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# 输出: 0
# 
# 解释: endWord "cog" 不在字典中，所以无法进行转换。
# 
#
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    #bfs
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList:
            return 0
        L = len(beginWord)
        wordDict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                tmpWord = word[:i]+'*'+word[i+1:]   #预处理，每一位替换成*，aa* -> aaa
                wordDict[tmpWord].append(word)

        queue = [(beginWord, 1)]                    #初始化，(单词，变化次数)
        visited = {beginWord:1}
        while queue:
            curWord, level = queue.pop(0)           
            for i in range(L):                      #这个单词每一位替换为*，进行下一次变化，等于end就返回变化次数，出现过的就不做处理，没出现的放入queue，下次bfs再处理
                intermediate_word = curWord[:i]+'*'+curWord[i+1:]
                for word in wordDict[intermediate_word]:
                    if word == endWord:             #找到就返回变化次数
                        return level + 1
                    if word not in visited:         #没有访问过的需要标记
                        visited[word] = 1
                        queue.append((word, level + 1))
                wordDict[intermediate_word] = []
        return 0


    
# @lc code=end

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
o = Solution()
print(o.ladderLength(beginWord, endWord, wordList))
