#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/featured/card/top-interview-quesitons-in-2018/275/string/1138/
# 单词拆分
# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

# 说明：
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 示例 1：

# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# 示例 2：

# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
#      注意你可以重复使用字典中的单词。
# 示例 3：

# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false

# https://blog.csdn.net/weixin_42771166/article/details/85320822
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if len(s) == 0 or not wordDict:
            return False
        max_stride = max([len(x) for x in wordDict])#字典最长值
        print max_stride
        res = [0] * (len(s) + 1)
        res[0] = 1
        for i in range(1, len(s) + 1):
            for j in range(i-max_stride, i):
            # for j in range(i):#不减枝
                if res[j] == 1 and s[j:i] in wordDict:
                    res[i] = 1
        if res[-1] == 1:
            return True
        else:
            return False  






ss = "applepenapple"
wordDict = ["apple", "pen"]
s = Solution()
res = s.wordBreak(ss, wordDict)
print(res)
