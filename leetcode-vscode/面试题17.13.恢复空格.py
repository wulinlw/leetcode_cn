# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题17.13.恢复空格
# 
# https://leetcode-cn.com/problems/re-space-lcci/
# 
# 哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。像句子"I reset the computer. It still didn&rsquo;t boot!"已经变成了"iresetthecomputeritstilldidntboot"。在处理标点符号和大小写之前，你得先把它断成词语。当然了，你有一本厚厚的词典dictionary，不过，有些词没在词典里。假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。
# 注意：本题相对原题稍作改动，只需返回未识别的字符数
# 
#  
# 
# 示例：
# 
# 输入：
# dictionary = ["looked","just","like","her","brother"]
# sentence = "jesslookedjustliketimherbrother"
# 输出： 7
# 解释： 断句后为"jess looked just like tim her brother"，共7个未识别字符。
# 
# 
# 提示：
# 
# 
# 	0 <= len(sentence) <= 1000
# 	dictionary中总字符数不超过 150000。
# 	你可以认为dictionary和sentence中只包含小写字母。
# 
# 
# 
# Medium 50.5%
# Testcase Example: ["looked","just","like","her","brother"]
# "jesslookedjustliketimherbrother"
# 
# 提示:
# 试试递归方法。
# 你能把所有的可能性都试一试吗？那会是什么样子？
# 你可以用两种方法中的一种来考虑递归算法：(1)对于每个字符，我应该在这里放一个空格吗？(2)下一个空格应该放在哪里？两种方案都可以递归地解决。
# 递归算法是否会反复遇到相同的子问题？你能用一个散列表进行优化吗？
# 在现实生活中，我们知道有些路径不会构成一个词。例如，没有以hellothisism开头的单词。能在明知行不通的情况下提前终止吗？
# 如果想提前终止，可以试一试trie。
# 
# 
from typing import List
class Solution:
    # dp[i] = (0,i] （区间左开右闭）之前所有未识别字母數目
    # dp[i] = min(dp[i], dp[j-1])
    def respace(self, dictionary: List[str], sentence: str) -> int:
        dictionary = {*dictionary}                  #*将列表转化成元组，这里外面加上{}相当于排序了
        # print(dictionary)
        n = len(sentence)
        d = [0] * (n+1)
        for i in range(1, n+1):
            d[i] = d[i-1] + 1                       #默认不匹配，在前一个基础上+1
            for j in range(i+1):                    #分割sentence[:i]，sentence[j:i]是单词，则取较小的，d[i]（默认）， d[j]去掉匹配的单词后之前未匹配的
                if sentence[j:i] in dictionary:
                    d[i] = min(d[i], d[j])
        return d[-1]



dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
o = Solution()
print(o.respace(dictionary, sentence))