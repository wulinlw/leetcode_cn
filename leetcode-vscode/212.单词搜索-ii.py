#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#
# https://leetcode-cn.com/problems/word-search-ii/description/
#
# algorithms
# Hard (39.25%)
# Likes:    124
# Dislikes: 0
# Total Accepted:    11.4K
# Total Submissions: 28.6K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
#  '["oath","pea","eat","rain"]'
#
# 给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。
# 
# 
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
# 
# 示例:
# 
# 输入: 
# words = ["oath","pea","eat","rain"] and board =
# [
# ⁠ ['o','a','a','n'],
# ⁠ ['e','t','a','e'],
# ⁠ ['i','h','k','r'],
# ⁠ ['i','f','l','v']
# ]
# 
# 输出: ["eat","oath"]
# 
# 说明:
# 你可以假设所有输入都由小写字母 a-z 组成。
# 
# 提示:
# 
# 
# 你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
# 如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？
# 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。
# 
# 
#
from typing import List
# @lc code=start
# 前缀树
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word = ""                                              #加一个word属性，用于记录单词

class Solution:
    # https://leetcode-cn.com/problems/word-search-ii/solution/pythontrieshu-dfs-by-tie-dan-du-du-lu/
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        #回溯
        def backtracking(row, col, parent):    
            letter = board[row][col]
            currNode = parent.children[letter]						#当前节点
            
            if currNode.isWord:                                     #边界条件
                matchedWords.add(currNode.word)                     #注意TrieNode中加了一个word记录单词
            
            board[row][col] = '#'                                   #回溯开始时，标记已走过的路
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:           #上下左右
                newRow, newCol = row + rowOffset, col + colOffset     
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if board[newRow][newCol] not in currNode.children:  #当前字符不在Trie树中
                    continue
                backtracking(newRow, newCol, currNode)              #传入当前节点
        
            board[row][col] = letter                                #回溯完成时，恢复原始数据
            if not currNode:                                        #性能优化，匹配过的节点删掉，下个单词匹配更快
                del parent[letter]

        self.root = TrieNode()									#构建前缀树，Leetcode 208
        for word in words:
            node = self.root
            for i in word: 
                if i not in node.children:
                    node.children[i] = TrieNode()
                node = node.children[i]
            node.isWord = True
            node.word = word

        rowNum = len(board)
        colNum = len(board[0])
        matchedWords = set()
        for row in range(rowNum):
            for col in range(colNum):
                if board[row][col] in self.root.children:						#首字母在前缀树中才需要继续
                    backtracking(row, col, self.root)				#每次传入Trie root
        return list(matchedWords)    

# @lc code=end


board =[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
board =[["a","a"]]
words = ["a"]
o = Solution()
print(o.findWords(board, words))