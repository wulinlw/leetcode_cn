#
# @lc app=leetcode.cn id=820 lang=python3
#
# [820] 单词的压缩编码
#
# https://leetcode-cn.com/problems/short-encoding-of-words/description/
#
# algorithms
# Medium (40.03%)
# Likes:    70
# Dislikes: 0
# Total Accepted:    14.1K
# Total Submissions: 32.8K
# Testcase Example:  '["time", "me", "bell"]'
#
# 给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。
# 
# 例如，如果这个列表是 ["time", "me", "bell"]，我们就可以将其表示为 S = "time#bell#" 和 indexes = [0,
# 2, 5]。
# 
# 对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。
# 
# 那么成功对给定单词列表进行编码的最小字符串长度是多少呢？
# 
# 
# 
# 示例：
# 
# 输入: words = ["time", "me", "bell"]
# 输出: 10
# 说明: S = "time#bell#" ， indexes = [0, 2, 5] 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= words.length <= 2000
# 1 <= words[i].length <= 7
# 每个单词都是小写字母 。
# 
# 
#
import collections,functools
from typing import List
# @lc code=start
#前缀树 Trie树
class TrieNode:
    def __init__(self):
        self.children = {}                      #记录下一个节点，注意是字典，查找0(1)
        self.dept = 0                           #深度
    
    def addWord(self, word, idx):
        if idx>=len(word):return                #递归终止条件，超过长度时结束。 下面有就返回，没有就创建
        tmpNode = self.children[word[idx]] if self.children.__contains__(word[idx]) else TrieNode()
        tmpNode.dept = idx + 1                  #深度+1
        tmpNode.addWord(word, idx+1)            #递归下一个字符
        self.children[word[idx]] = tmpNode      #记录当前字符
    
    def count(self):                            #这个是递归函数
        rst = 0 
        for k in self.children:                 #循环当前的节点
            rst += self.children[k].count()     #迭代他的子节点，一直迭代到最底层
        if not self.children:                   #到最后深度+1，这样rst就是所有分支的深度总和
            return self.dept + 1
        return rst



class Solution:
    #存储后缀，循环去除相同后缀
    # https://leetcode-cn.com/problems/short-encoding-of-words/solution/dan-ci-de-ya-suo-bian-ma-by-leetcode-solution/
    def minimumLengthEncoding2(self, words: List[str]) -> int:
        s = set(words)                      #先去重
        for word in words:                  #依次循环每个单词
            for j in range(1, len(word)):   #截取子串，取后缀，
                if word[j:] in s:           #存在的后缀都删掉
                    s.remove(word[j:])
        length = 0                          #计算总长
        for i in s:                 
            length += len(i) + 1            #单词长度+#的一个长度
        return length

    def minimumLengthEncoding3(self, words: List[str]) -> int:
        words = list(set(words)) #remove duplicates
        #Trie is a nested dictionary with nodes created
        # when fetched entries are missing
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        
        #reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        nodes = [functools.reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]
        print(nodes)

        #Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)

    # 看这个，前缀树 Trie
    # https://leetcode-cn.com/problems/short-encoding-of-words/solution/3chong-fang-fa-python3-by-zhenxiangsimple/
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = [word[::-1] for word in set(words)]
        trie = TrieNode()
        for word in words:
            trie.addWord(word, 0)
        return trie.count()


# @lc code=end


words = ["time", "me", "bell"]
o = Solution()
print(o.minimumLengthEncoding(words))