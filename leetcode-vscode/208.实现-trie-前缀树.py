#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#
# https://leetcode-cn.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (64.95%)
# Likes:    237
# Dislikes: 0
# Total Accepted:    29.4K
# Total Submissions: 44.6K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n' +
#  '[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
# 
# 示例:
# 
# Trie trie = new Trie();
# 
# trie.insert("apple");
# trie.search("apple");   // 返回 true
# trie.search("app");     // 返回 false
# trie.startsWith("app"); // 返回 true
# trie.insert("app");   
# trie.search("app");     // 返回 true
# 
# 说明:
# 
# 
# 你可以假设所有的输入都是由小写字母 a-z 构成的。
# 保证所有输入均为非空字符串。
# 
# 
#

# @lc code=start
#Trie前缀树
class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]       #初始化26个字符，方便insert判断  ,也可以用字典{} insert的判断方式也会改变下
        self.isWord = False                             #标记这个节点是单词结尾
        # self.depth = 0                                #可以记录深度，这题没有用到

class Trie:
    def __init__(self):
        self.root = TrieNode()                          #根节点为空

    def insert(self, word: str) -> None:
        node = self.root                                #拿到根节点
        for i in word: 
            if not node.children[ord(i) - ord('a')]:    #不存在当前字符的，立即创建
                node.children[ord(i) - ord('a')] = TrieNode()   
            node = node.children[ord(i) - ord('a')]     #每次都向后移动一步，和链表一样
        node.isWord = True                              #单词结束后标记下这个位置是单词的结束节点

    def search(self, word: str) -> bool:
        node = self.root 
        for i in word: 
            if not node.children[ord(i) - ord('a')]:    #不存在的立即返回false
                return False
            node = node.children[ord(i) - ord('a')]
        return node.isWord                              #单词跑完后，看看是否是结束节点


    def startsWith(self, prefix: str) -> bool:
        node = self.root 
        for i in prefix: 
            if not node.children[ord(i) - ord('a')]:
                return False
            node = node.children[ord(i) - ord('a')]
        return True                                     #能跑完就是正确的

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

trie = Trie()

trie.insert("apple")
print(trie.search("apple"))   #// 返回 true
print(trie.search("app"))     #// 返回 false
print(trie.startsWith("app")) #// 返回 true
trie.insert("app")   
print(trie.search("app"))     #// 返回 true