#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/featured/card/array-and-string/202/conclusion/794/
# 反转字符串中的单词 III
# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

# 示例 1:
# 输入: "Let's take LeetCode contest"
# 输出: "s'teL ekat edoCteeL tsetnoc" 
# 注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split(' ')[::-1])[::-1]

    # 利用堆栈的先进后出的结构很容易做到字符反转
    # 但一串英文单词中，单词的个数总是比空格的字数多一个，在处理的时候很不方便
    # 如：wordA(空格)wordB(空格)wordC
    # 我们不妨在原字符串末尾补充一个空格，让每一小节都变成“单词+空格”（遇见空格就是我们判断出栈的前提条件）这样的形式
    # 预处理后：wordA(空格)wordB(空格)wordC(空格)
    # 反转后：(空格)reversed_wordA(空格)reversed_wordB(空格)reversed_wordC
    # 于是我们只要利用切片返回第一个字符后面的string就可以了
    def reverseWords2(self, s: str) -> str:
        s=s+" "
        stack,res=[],""
        for i in s:
            stack.append(i)
            if i==" ":
                while(stack):
                    res=res+stack.pop()
        return res[1:]


w = "Let's take LeetCode contest"
s = Solution()
n = s.reverseWords(w)
print(n)       