#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#
# https://leetcode-cn.com/problems/add-and-search-word-data-structure-design/description/
#
# algorithms
# Medium (43.07%)
# Likes:    98
# Dislikes: 0
# Total Accepted:    8.4K
# Total Submissions: 19.5K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n' +
#   '[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# 设计一个支持以下两种操作的数据结构：
# 
# void addWord(word)
# bool search(word)
# 
# 
# search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。
# 
# 示例:
# 
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# 
# 
# 说明:
# 
# 你可以假设所有单词都是由小写字母 a-z 组成的。
# 
#

# @lc code=start
#Trie前缀树
class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.isWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:                                           #和leetcode 208一样
        node = self.root
        for i in word: 
            if not node.children[ord(i) - ord('a')]:
                node.children[ord(i) - ord('a')] = TrieNode()
            node = node.children[ord(i) - ord('a')]
        node.isWord = True

    def search(self, word: str) -> bool:
        def dfs(word, node, idx):                                                   #dfs迭代匹配字符
            if len(word) == idx:
                return node.isWord
            ch = word[idx]
            if ch == '.':                                                           #区别就是需要处理通配符“.” ， 每个分支都走一遍
                for i in range(26):                                                 #如果children用字典，这里需要用dict.values()迭代
                    if node.children[i] and dfs(word, node.children[i], idx+1):     #前提是这个分支有内容
                        return True
            elif node.children[ord(ch) - ord('a')]:
                return dfs(word, node.children[ord(ch) - ord('a')], idx+1)
            return False
        return dfs(word, self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
print(obj.search("pad")) #-> false
print(obj.search("bad")) #-> true
print(obj.search(".ad")) #-> true
print(obj.search("b..")) #-> true