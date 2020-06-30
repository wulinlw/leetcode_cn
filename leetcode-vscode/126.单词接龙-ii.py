#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#
# https://leetcode-cn.com/problems/word-ladder-ii/description/
#
# algorithms
# Hard (32.04%)
# Likes:    187
# Dislikes: 0
# Total Accepted:    11K
# Total Submissions: 33.4K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord
# 的最短转换序列。转换需遵循如下规则：
# 
# 
# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。
# 
# 
# 说明:
# 
# 
# 如果不存在这样的转换序列，返回一个空列表。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
# 
# 
# 示例 1:
# 
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 输出:
# [
# ⁠ ["hit","hot","dot","dog","cog"],
# ["hit","hot","lot","log","cog"]
# ]
# 
# 
# 示例 2:
# 
# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# 输出: []
# 
# 解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。
# 
#
from typing import List
import collections 
# @lc code=start
class Solution:
    #bfs
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        dic = collections.defaultdict(list)
        n = len(beginWord)
        for w in wordList:                              #预处理，每一位替换成*后分类
            for i in range(n):
                dic[w[:i] + '*' + w[i+1:]].append(w)

        q, s = collections.deque([(beginWord, [beginWord])]), collections.deque()
        seen = set()                                    #处理过的记录，不在处理第二次
        res = []
        while q:
            while q:
                w, path = q.popleft()
                if w == endWord: 
                    res.append(path)
                seen.add(w)
                for i in range(n):
                    for v in dic[w[:i] + '*' + w[i+1:]]:
                        if v not in seen:
                            s.append((v, path + [v]))
            if res: 
                return res
            q, s = s, q
        return []

    def findLadders2(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # 先将 wordList 放到哈希表里，便于判断某个单词是否在 wordList 里
        word_set = set(wordList)
        res = []
        if len(word_set) == 0 or endWord not in word_set:
            return res

        successors = defaultdict(set)
        # 第 1 步：使用广度优先遍历得到后继结点列表 successors
        # key：字符串，value：广度优先遍历过程中 key 的后继结点列表
        found = self.__bfs(beginWord, endWord, word_set, successors)
        if not found:
            return res
        # 第 2 步：基于后继结点列表 successors ，使用回溯算法得到所有最短路径列表
        path = [beginWord]
        self.__dfs(beginWord, endWord, successors, path, res)
        return res

    def __bfs(self, beginWord, endWord, word_set, successors):
        queue = deque()
        queue.append(beginWord)

        visited = set()
        visited.add(beginWord)

        found = False
        word_len = len(beginWord)
        next_level_visited = set()

        while queue:
            current_size = len(queue)
            for i in range(current_size):
                current_word = queue.popleft()
                word_list = list(current_word)

                for j in range(word_len):
                    origin_char = word_list[j]

                    for k in string.ascii_lowercase:
                        word_list[j] = k
                        next_word = ''.join(word_list)

                        if next_word in word_set:
                            if next_word not in visited:
                                if next_word == endWord:
                                    found = True
                                next_level_visited.add(next_word)
                                queue.append(next_word)

                                successors[current_word].add(next_word)
                    word_list[j] = origin_char
            if found:
                break
            # 取两集合全部的元素（并集，等价于将 next_level_visited 里的所有元素添加到 visited 里）
            visited |= next_level_visited
            next_level_visited.clear()
        return found

    def __dfs(self, beginWord, endWord, successors, path, res):
        if beginWord == endWord:
            res.append(path[:])
            return

        if beginWord not in successors:
            return

        successor_words = successors[beginWord]
        for next_word in successor_words:
            path.append(next_word)
            self.__dfs(next_word, endWord, successors, path, res)
            path.pop()


# @lc code=end

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

solution = Solution()
res = solution.findLadders(beginWord, endWord, wordList)
print(res)

