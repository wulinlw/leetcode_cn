# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题16.02.单词频率
# 
# https://leetcode-cn.com/problems/words-frequency-lcci/
# 
# 设计一个方法，找出任意指定单词在一本书中的出现频率。
# 你的实现应该支持如下操作：
# 
# WordsFrequency(book)构造函数，参数为字符串数组构成的一本书
# get(word)查询指定单词在数中出现的频率
# 
# 示例：
# WordsFrequency wordsFrequency = new WordsFrequency({"i", "have", "an", "apple", "he", "have", "a", "pen"});
# wordsFrequency.get("you"); //返回0，"you"没有出现过
# wordsFrequency.get("have"); //返回2，"have"出现2次
# wordsFrequency.get("an"); //返回1
# wordsFrequency.get("apple"); //返回1
# wordsFrequency.get("pen"); //返回1
# 
# 提示：
# 
# book[i]中只包含小写字母
# 1 
# 1 
# get函数的调用次数不会超过100000
# 
# 
# 
# Medium 77.3%
# Testcase Example: ["WordsFrequency","get","get","get","get","get"]
# [[["i","have","an","apple","he","have","a","pen"]],["you"],["have"],["an"],["apple"],["pen"]]
# 
# 提示:
# 想想这个问题的最佳运行时间是多少。如果你的解法匹配最理想的运行时间，那么你可能无法做的更好了。
# 可以使用散列表来优化重复的情况吗？
# 
# 
from typing import List
class WordsFrequency:

    def __init__(self, book: List[str]):
        self.dic = {}
        for i in book:
            self.dic[i] = self.dic.get(i, 0) + 1

    def get(self, word: str) -> int:
        if word in self.dic:
            return self.dic[word]
        else:
            return 0




# Your WordsFrequency object will be instantiated and called as such:
book = ["i","have","an","apple","he","have","a","pen"]
obj = WordsFrequency(book)
print(obj.get("you"))
print(obj.get("have"))
print(obj.get("an"))
print(obj.get("apple"))
print(obj.get("pen"))



