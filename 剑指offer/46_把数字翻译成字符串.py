#!/usr/bin/python
#coding:utf-8

# // 面试题46：把数字翻译成字符串
# // 题目：给定一个数字，我们按照如下规则把它翻译为字符串：0翻译成"a"，1翻
# // 译成"b"，……，11翻译成"l"，……，25翻译成"z"。一个数字可能有多个翻译。例
# // 如12258有5种不同的翻译，它们分别是"bccfi"、"bwfi"、"bczi"、"mcfi"和
# // "mzi"。请编程实现一个函数用来计算一个数字有多少种不同的翻译方法。

class Solution:
    # 设f(i)表示从第i位数字开始的不同翻译数目，则：
    # f(i)=1×f(i+1)+g(i,i+1)×f(i+2)
    # 其中g(i,i+1)为0或者1，表示第i位和第i+1位能否组成合法的(10~25)两位数。
    def GetTranslationCount(self, num):
        if num<=0: return 0
        s = str(num)
        n = len(s)
        dp = [1] * n
        for i in range(n,-1,-1):
            if i<n-1:               #防止越界
                dp[i] = dp[i+1]
                d1 = int(s[i])
                d2 = int(s[i+1])
                tmp = d1*10 + d2
                if tmp>=10 and tmp<=25:
                    if i<n-2:               #不是最后2位，有+2种
                        dp[i] += dp[i+2]
                    else:                   #最后2位，只有1种
                        dp[i] += 1
        print(dp)
        return dp[0]
        
    # 都不能组合，那每一位都是f(x)， 状态 dp(i)=dp(i-1)
    # 如果可以组合，那就是dp(i) = dp(i-1)+dp(i-2)
    def translateNum(self, num: int) -> int:
        if num<10:return 1
        num = str(num)
        n = len(num)
        dp =[1]* (n+1)
        for i in range(2,n+1): 
            if int(num[i-2])==1 or (int(num[i-2])==2 and int(num[i-1])<=5):
                dp[i] = dp[i - 1]+dp[i-2]
            else:
                dp[i] = dp[i-1]
        print(dp)
        return dp[-1]

n = 12258
obj = Solution()
# print(obj.GetTranslationCount(n))
print(obj.translateNum(n))