#!/usr/bin/python
#coding:utf-8


# 面试题 01.05. 一次编辑
# 字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。
# 示例 1:
# 输入: 
# first = "pale"
# second = "ple"
# 输出: True
 
# 示例 2:
# 输入: 
# first = "pales"
# second = "pal"
# 输出: False
# https://leetcode-cn.com/problems/one-away-lcci/

from typing import List

class Solution:
    #编辑距离 类似题目，动态规划
    #这题没有动态规划
    def oneEditAway(self, first: str, second: str) -> bool:
        if abs(len(first)-len(second)) > 1:         #长度差大于1，false
            return False
        
        replace_count = 0
        if len(first) == len(second):               #长度相等，不同字符>2，false
            for i in range(len(first)):
                if first[i] != second[i]:
                    replace_count += 1
                if replace_count >= 2:
                    return False
            return True
                                                    #相差1的情况下，长串去掉当前字符，看看是否和短串一样
        if len(second) > len(first):                #长的放前面
            first,second = second, first

        if len(first) > len(second):                
            for i in range(len(first)):             #遍历长的，每次取走一个，剩下的和second比是否一样
                if first[0:i] + first[i+1:] == second:
                    return True
            return False
        


first = "pale"
second = "ple"
o = Solution()
print(o.oneEditAway(first, second))