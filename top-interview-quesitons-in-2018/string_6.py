#!/usr/bin/python
#coding:utf-8


# https://leetcode-cn.com/explore/featured/card/top-interview-quesitons-in-2018/275/string/1141/
# 单词搜索 II
# 给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

# 示例:
# 输入: 
# words = ["oath","pea","eat","rain"] and board =
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]

# 输出: ["eat","oath"]
# 说明:
# 你可以假设所有输入都由小写字母 a-z 组成。

# 提示:
# 你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
# 如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？ 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。

# https://blog.csdn.net/weixin_41303016/article/details/88393706
class Trie(object):
        def __init__(self):
            self.root = {}       
        
        def insert(self, word):
            """
            Inserts a word into the trie.
            :type word: str
            :rtype: void
            """
            curNode = self.root
            for i in word:
                if i not in curNode:
                    curNode[i] = {}
                curNode = curNode[i]
            curNode["#"] = True
            # print self.root

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        row = len(board)
        colum = len(board[0])
        res = []

        def find(x, y, word, TrieNode):
            if x >= 0 and x < row and y >= 0 and y < colum and board[x][y] in TrieNode:
                TrieNode = TrieNode[board[x][y]]
                word += board[x][y]
                if TrieNode.get("#", 9) == True:
                    res.append(word)
                t = board[x][y]
                board[x][y] = 3
                find(x + 1, y, word, TrieNode)
                find(x - 1, y, word, TrieNode)
                find(x, y + 1, word, TrieNode)
                find(x, y - 1, word, TrieNode)
                board[x][y] = t

        root = Trie()
        tmp = set()
        for i in words:
            root.insert(i)
            tmp.add(i[0])
        # print tmp
        for i in range(row):
            for j in range(colum):
                if board[i][j] in tmp:#从单词的第一个字符开始找
                    find(i, j, "", root.root)

        return list(set(res))

words = ["oath","pea","eat","rain"]
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

# root = Trie()
# root.insert('abcde')

s = Solution()
res = s.findWords(board, words)
print(res)













