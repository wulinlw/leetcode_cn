#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/featured/card/top-interview-quesitons-in-2018/275/string/1140/
# 实现 Trie (前缀树)
# 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

# 示例:
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // 返回 true
# trie.search("app");     // 返回 false
# trie.startsWith("app"); // 返回 true
# trie.insert("app");   
# trie.search("app");     // 返回 true
# 说明:
# 你可以假设所有的输入都是由小写字母 a-z 构成的。
# 保证所有输入均为非空字符串。


#字典模拟
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        
 
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        
        node["end"] = True
        # print self.root
            
        
 
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
            
        return "end" in node
        
 
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        
        return True

        

word = "abcde"
# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert(word)#{'a': {'b': {'c': {'d': {'e': {'end': True}}}}}}
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)







