#!/usr/bin/python
#coding:utf-8

# // 面试题58（一）：翻转单词顺序
# // 题目：输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
# // 为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student."，
# // 则输出"student. a am I"。


class Solution:
    def ReverseSentence(self, s):
        if len(s) == 0 :return False
        s2 = list(s[::-1])

        #leetcode中是需要合并多个空格的
        # s3 = []
        # for i in range(len(s2)):
        #     if i-1>=0:
        #         if s2[i] ==' ' and s2[i-1] ==' ':
        #             pass
        #         else:
        #             s3.append(s2[i])
        # print(s2)
        # s2 = s3
        start = end = 0
        while start < len(s2)-1:
            if s2[start] == " ":
                start += 1                          #起始遇到空格，头尾都后移一位
                end += 1
            elif s2[end] == " " or end == len(s2)-1: #结尾遇到空格，需要翻转了
                s2[start:end] = s2[start:end][::-1]
                # print(start,end)
                # print(s2)
                end += 1                            #转完后，重新设置头尾
                start = end
            else:
                end += 1
        
        return "".join(s2)   

    def reverseWords(self, s):
        s = s.strip()  # 去除首尾的括号
        start = len(s) - 1
        end = len(s)
        res = ''
        while start > 0:
            if s[start] == ' ':
                res += s[start + 1: end] + ' '
                while s[start] == ' ':
                    start -= 1
                end = start + 1
            start -= 1
        return res + s[:end]
     
s = "I am a   student."
obj = Solution()
print(obj.ReverseSentence(s))
