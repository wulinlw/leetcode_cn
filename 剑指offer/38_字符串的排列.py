#!/usr/bin/python
#coding:utf-8

# // 面试题38：字符串的排列
# // 题目：输入一个字符串，打印出该字符串中字符的所有排列。例如输入字符串abc，
# // 则打印出由字符a、b、c所能排列出来的所有字符串abc、acb、bac、bca、cab和cba。

class Solution:
    def Permutation(self, s):
        re = []
        def bt(s2, tmp):
            if len(s2) == 0:
                re.append(tmp)
                return  
            for i in range(len(s2)):
                bt(s2[:i]+s2[i+1:], s2[i]+tmp)
        bt(s, "") 
        return re
    
    def Permutation2(self, s):
        s = list(s)
        re = []
        def bt(s2, index):
            if len(s2) == index:
                tmp = s2[:]
                re.append("".join(tmp))
            for i in range(index, len(s2)):
                s2[i],s2[index] = s2[index],s2[i]
                bt(s2, index+1)
                s2[i],s2[index] = s2[index],s2[i]
        bt(s, 0)
        return re


        
    
string = 'abc'
obj = Solution()
# re = obj.Permutation(string)
# for i in range(len(re)):
#     print(re[i])

re = obj.Permutation2(string)
for i in range(len(re)):
    print(re[i])
