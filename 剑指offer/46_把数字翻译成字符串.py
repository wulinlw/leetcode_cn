#!/usr/bin/python
#coding:utf-8

# // 面试题46：把数字翻译成字符串
# // 题目：给定一个数字，我们按照如下规则把它翻译为字符串：0翻译成"a"，1翻
# // 译成"b"，……，11翻译成"l"，……，25翻译成"z"。一个数字可能有多个翻译。例
# // 如12258有5种不同的翻译，它们分别是"bccfi"、"bwfi"、"bczi"、"mcfi"和
# // "mzi"。请编程实现一个函数用来计算一个数字有多少种不同的翻译方法。

class Solution:
    def GetTranslationCount(self, n):
        if n<=0: return 0
        s = str(n)
        n = len(s)
        dp = [1] * n
        for i in range(n,-1,-1):
            if i<n-1: 
                dp[i] = dp[i+1]
                d1 = int(s[i])
                d2 = int(s[i+1])
                tmp = d1*10 + d2
                if tmp>=10 and tmp<=25:
                    if i<n-2:
                        dp[i] += dp[i+2]
                    else:
                        dp[i] += 1
        # print(dp)
        return dp[0]

n = 12258
obj = Solution()
print(obj.GetTranslationCount(n))
