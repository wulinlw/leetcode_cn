#!/usr/bin/python
#coding:utf-8

# // 面试题50（一）：字符串中第一个只出现一次的字符
# // 题目：在字符串中找出第一个只出现一次的字符。如输入"abaccdeff"，则输出
# // 'b'。
import heapq
class Solution:
    def FirstNotRepeatingChar(self, s):
        d = {}
        order = []          #存每个字符第一次出现的顺序
        for i in s: 
            if i not in d:
                d[i] = 1
                order.append(i)
            else:
                d[i] += 1
        for j in order:     #从顺序里找第一个出现一次的
            if d[j] == 1: 
                return j
        return -1
        
s = "abaccdeff"
obj = Solution()
print(obj.FirstNotRepeatingChar(s))

