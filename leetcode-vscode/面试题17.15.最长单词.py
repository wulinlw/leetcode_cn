# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题17.15.最长单词
# 
# https://leetcode-cn.com/problems/longest-word-lcci/
# 
# 给定一组单词words，编写一个程序，找出其中的最长单词，且该单词由这组单词中的其他单词组合而成。若有多个长度相同的结果，返回其中字典序最小的一项，若没有符合要求的单词则返回空字符串。
# 示例：
# 输入： ["cat","banana","dog","nana","walk","walker","dogwalker"]
# 输出： "dogwalker"
# 解释： "dogwalker"可由"dog"和"walker"组成。
# 
# 提示：
# 
# 0 
# 1 
# 
# 
# 
# Medium 36.1%
# Testcase Example: [""]
# 
# 提示:
# 试着简化这个问题：如果你只需要知道由列表中其他两个单词组成的最长单词会如何？
# 如果只想知道由列表中其他两个单词组成的最长单词，那么可以遍历全部单词，从最长到最短，检查每个单词是否可以由其他两个单词组成。为了检查，我们可以将字符串从所有可能的位置分开。
# 将前面的想法扩展到多个单词的情况。我们能不能把每个单词都拆分为所有可能的形式?
# 当你得到非常低效的递归算法时，试着查找重复发生的子问题。
# 
# 
from typing import List
class Solution:
    #[139] 单词拆分 类似
    def longestWord2(self, words: List[str]) -> str:
        wordDict = set(words)
        res = ''
        def wordBreak(s):
            m = {}                              #放入hash，快速查找O(1)
            for i in wordDict:
                m[i] = 1 
            dp = [False] * (len(s)+1)
            dp[0] = True                        #初始值True
            temp_set = set(wordDict)
            temp_set.remove(s)
            for i in range(1, len(s)+1):    
                for j in range(i):              #从0-i，0是true的意思是截止到这一位，是可以在字典中找到的
                    if dp[j] and s[j:i] in temp_set:   #之前的在字典中，现在这一段也在字典中，
                        dp[i] = True            #注意这里是dp[i]，当前值设为True
                        break
            return dp[-1]                       #如果最后一个单词也在字典中，就是True
        for word in words:
            if wordBreak(word) and ((len(word) > len(res)) or (len(word) == len(res) and word < res)):
                res = word
        return res

    # 递归
    def longestWord(self, words: List[str]) -> str:
        d = set(words)
        words.sort(key = lambda x:(-len(x),x))  #长度倒序，一样长的按字典序排

        def dfs(word, k):                       #在单词表中已找到的k个单词数
            if word in d and k:                 #边界条件，最后的字符串在单词表中，索引不为0
                return True
            for i in range(len(word)):          #每个单词切分前半段是单词，后半段也是
                if word[:i] in d and dfs(word[i:], k+1):
                    return True
            return False
        
        for word in words:
            if dfs(word, 0):
                return word
        return ""

words = ["cat","banana","dog","nana","walk","walker","dogwalker"]
words = ["ttaaaa","pp","tpa","kpaqkt","tktpqq","aqppatp"]
o = Solution()
print(o.longestWord(words))
