#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#
# https://leetcode-cn.com/problems/word-break/description/
#
# algorithms
# Medium (43.53%)
# Likes:    355
# Dislikes: 0
# Total Accepted:    41.3K
# Total Submissions: 93.8K
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
# 
# 说明：
# 
# 
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 
# 
# 示例 1：
# 
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# 
# 
# 示例 2：
# 
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
# 注意你可以重复使用字典中的单词。
# 
# 
# 示例 3：
# 
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = {}                              #放入hash，快速查找O(1)
        for i in wordDict:
            m[i] = 1 
        dp = [False] * (len(s)+1)
        dp[0] = True                        #初始值True
        for i in range(1, len(s)+1):    
            for j in range(i):              #从0-i，0是true的意思是截止到这一位，是可以在字典中找到的
                if dp[j] and s[j:i] in m:   #之前的在字典中，现在这一段也在字典中，
                    dp[i] = True            #注意这里是dp[i]，当前值设为True
                    break
        # print(dp)
        return dp[-1]                       #如果最后一个单词也在字典中，就是True



# @lc code=end

s = "leetcode"
wordDict = ["leet", "code"]
s = "applepenapple"
wordDict = ["apple", "pen"]
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
o = Solution()
print(o.wordBreak(s, wordDict))