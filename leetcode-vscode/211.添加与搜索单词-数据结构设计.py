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
class WordDictionary:

    class Node:
        def __init__(self):
            self.is_word = False
            self.next = [None for _ in range(26)]

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = WordDictionary.Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        size = len(word)
        cur_node = self.root
        for i in range(size):
            alpha = word[i]
            next = cur_node.next[ord(alpha) - ord('a')]
            if next is None:
                cur_node.next[ord(alpha) - ord('a')] = WordDictionary.Node()
            cur_node = cur_node.next[ord(alpha) - ord('a')]

        if not cur_node.is_word:
            cur_node.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.__match(word, self.root, 0)

    def __match(self, word, node, start):
        if start == len(word):
            return node.is_word
        alpha = word[start]
        # 关键在这里，如果当前字母是 "." ，每一个分支都要走一遍
        if alpha == '.':
            # print(node.next)
            for i in range(26):
                if node.next[i] and self.__match(word, node.next[i], start + 1):
                    return True
            return False
        else:
            if not node.next[ord(alpha)-ord('a')]:
                return False
            return self.__match(word, node.next[ord(alpha) - ord('a')], start + 1)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

