# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题16.20.T9键盘
# 
# https://leetcode-cn.com/problems/t9-lcci/
# 
# 在老式手机上，用户通过数字键盘输入，手机将提供与这些数字相匹配的单词列表。每个数字映射到0至4个字母。给定一个数字序列，实现一个算法来返回匹配单词的列表。你会得到一张含有有效单词的列表。映射如下图所示：
# 示例 1:
# 
# 输入: num = "8733", words = ["tree", "used"]
# 输出: ["tree", "used"]
# 
# 
# 示例 2:
# 
# 输入: num = "2", words = ["a", "b", "c", "d"]
# 输出: ["a", "b", "c"]
# 
# 提示：
# 
# 
# 	num.length <= 1000
# 	words.length <= 500
# 	words[i].length == num.length
# 	num中不会出现 0, 1 这两个数字
# 
# 
# 
# Medium 69.6%
# Testcase Example: "8733"
# ["tree", "used"]
# 
# 提示:
# 想想递归。
# 你能递归地尝试所有的可能性吗？
# 在现实世界中，我们应该知道一些前缀/子字符串是行不通的。例如，考虑数字33835676368。虽然3383确实对应于fftf，但是没有以fftf开头的单词。有没有什么办法对于这样的情况做特殊处理？
# trie可以帮助我们。如果将整个单词列表存储在trie中会怎样？
# 我们可能会多次运行这个算法。如果做更多的预处理，这里有办法优化吗？
# 通过预处理，实际上可以将查找时间降低到O(1)。
# 
# 
from typing import List
class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:
        kb = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        re = []
        for word in words:
            count = 0
            for i in range(len(word)):
                if word[i] in kb[int(num[i])]:
                    count += 1
                else:
                    break
            if count == len(word):
                re.append(word)
        return re

num = "8733"
words = ["tree", "used"]
o = Solution()
print(o.getValidT9Words(num, words))