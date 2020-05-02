# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题17.25.单词矩阵
# 
# https://leetcode-cn.com/problems/word-rectangle-lcci/
# 
# 给定一份单词的清单，设计一个算法，创建由字母组成的面积最大的矩形，其中每一行组成一个单词(自左向右)，每一列也组成一个单词(自上而下)。不要求这些单词在清单里连续出现，但要求所有行等长，所有列等高。
# 如果有多个面积最大的矩形，输出任意一个均可。一个单词可以重复使用。
# 
# 示例 1:
# 
# 输入: ["this", "real", "hard", "trh", "hea", "iar", "sld"]
# 输出:
# [
#    "this",
#    "real",
#    "hard"
# ]
# 
# 示例 2:
# 
# 输入: ["aa"]
# 输出: ["aa","aa"]
# 
# 说明：
# 
# 
# 	words.length <= 1000
# 	words[i].length <= 100
# 	数据保证单词足够随机
# 
# 
# 
# Hard 40.3%
# Testcase Example: ["this", "real", "hard", "trh", "hea", "iar", "sld"]
# 
# 提示:
# 首先根据单词长度对字典进行分组，因为你知道每一列的长度必须相同，每一行的长度也必须相同。
# 你能找到一个特定长宽的单词矩阵吗？如果尝试了所有的选项会怎样？
# 当矩形看起来无效时，可以使用trie提前终止吗？
# 
# 
from typing import List
class Trie:
    def __init__(self):
        self.root = [{}, False]
    
    def addWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur[0]:
                cur[0][c] = [{}, False]
            cur = cur[0][c]
        cur[1] = True


class Solution:
    # https://leetcode-cn.com/problems/word-rectangle-lcci/solution/dfs-jian-zhi-zi-dian-shu-by-guo-zhi-guo/
    def maxRectangle(self, words: List[str]) -> List[str]:
        area = 0
        res = []
        trie = Trie()
        for word in words:
            trie.addWord(word)

        def dfs(arr, li):
            for word in words:
                if len(word) != len(arr):   continue
                for i, c in enumerate(word):
                    if c not in arr[i][0]: break
                else:
                    temp = arr[:]
                    flag = True
                    for i, c in enumerate(word):
                        temp[i] = temp[i][0][c]
                        flag &= temp[i][1]
                    li.append(word)
                    if flag:
                        h, w = len(li), len(word)
                        nonlocal area, res
                        if h * w > area:
                            area = h * w
                            res = li[:]
                    dfs(temp, li)
                    li.pop()

        ll = sorted(set(len(word) for word in words), reverse = True)
        for l in ll:
            if l * ll[0] < area:   break
            dfs([trie.root] * l, [])
        return res


words = ["this", "real", "hard", "trh", "hea", "iar", "sld"]
o = Solution()
print(o.maxRectangle(words))