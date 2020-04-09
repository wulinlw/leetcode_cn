#
# @lc app=leetcode.cn id=336 lang=python3
#
# [336] 回文对
#
# https://leetcode-cn.com/problems/palindrome-pairs/description/
#
# algorithms
# Hard (33.11%)
# Likes:    54
# Dislikes: 0
# Total Accepted:    3.2K
# Total Submissions: 9.6K
# Testcase Example:  '["abcd","dcba","lls","s","sssll"]'
#
# 给定一组唯一的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。
# 
# 示例 1:
# 
# 输入: ["abcd","dcba","lls","s","sssll"]
# 输出: [[0,1],[1,0],[3,2],[2,4]] 
# 解释: 可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
# 
# 
# 示例 2:
# 
# 输入: ["bat","tab","cat"]
# 输出: [[0,1],[1,0]] 
# 解释: 可拼接成的回文串为 ["battab","tabbat"]
# 
#
from typing import List
import collections
# @lc code=start
class Solution:
    # 将一个单词拆分为前缀后后缀两个部分，若前缀是回文的，后缀的逆序能在words中找到，就证明这两个单词可以组成一个回文对。
    # 同理，若后缀是个回文对，前缀的逆序能在words中找到，则这两个单词可以组成一个回文对。
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        lookup = {w: i for i, w in enumerate(words)}                                            #建立单词索引
        res = []
        for i, w in enumerate(words):
            for j in range(len(w) + 1):                                                         #每个字符份分割点，分割单词，得到前缀，后缀
                pre, suf = w[:j], w[j:] 
                if pre[::-1] == pre and suf[::-1] != w and suf[::-1] in lookup:                 #前缀是回文，那只需要找一个单词==后缀翻转，且后缀不是完整单词，后缀翻转后也在索引中
                    res.append([lookup[suf[::-1]], i])
                if suf[::-1] == suf and pre[::-1] != w and pre[::-1] in lookup and j != len(w): #后缀同理，
                                                                                                # j != len(w)，j = w的情况已经出现过
                    res.append([i, lookup[pre[::-1]]])
        return res

# @lc code=end
words = ["abcd","dcba","lls","s","sssll"]
# words = ["bat","tab","cat"]
# words = ["a",""]
words = ["a","abc","aba",""]
words = ["a","b","c","ab","ac","aa"]
o = Solution()
print(o.palindromePairs(words))