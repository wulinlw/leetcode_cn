#!/usr/bin/python
#coding:utf-8

# 单词拆分 II
# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

# 说明：
# 分隔时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 示例 1：

# 输入:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# 输出:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
# 示例 2：

# 输入:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# 输出:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# 解释: 注意你可以重复使用字典中的单词。
# 示例 3：

# 输入:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出:
# []

# https://blog.csdn.net/qqxx6661/article/details/78737010
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        Solution.res = []
        self.dfs(s, wordDict, '')
        return Solution.res

    def dfs(self, s, wordDict, stringlist):
        if self.check(s, wordDict):
            # 如果s已经切完，则加入最后结果集
            if len(s) == 0: 
                Solution.res.append(stringlist[1:])
            for i in range(1, len(s)+1):
                if s[:i] in wordDict:
                    print stringlist+' '+s[:i]
                    self.dfs(s[i:], wordDict, stringlist+' '+s[:i])

    def check(self, s, wordDict):
            dp = [False for i in range(len(s)+1)]
            dp[0] = True
            # 这里循环是len(s)，使得该check函数变成了只要有单词在里面就验证成功，和wordbreak有所不同！
            for i in range(len(s)):
                for j in range(i, -1, -1):
                    if dp[j] and s[j:i + 1] in wordDict:
                        dp[i + 1] = True
                        break
            return dp[len(s)]

    # 另一种解法
    def wordBreak2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = []
        memo = dict()
        return self.dfs2(s, res, wordDict, memo)
    
    def dfs2(self, s, res, wordDict, memo):
        if s in memo: return memo[s]
        if not s:
            return [""]
        res = []
        for word in wordDict:
            if s[:len(word)] != word: continue
            for r in self.dfs2(s[len(word):], res, wordDict, memo):
                res.append(word + ("" if not r else " " + r))
        memo[s] = res
        return res


ss = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
s = Solution()
res = s.wordBreak(ss, wordDict)
print(res)





































