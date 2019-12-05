#!/usr/bin/python
#coding:utf-8

# 剪绳子
# 给你一根长度为n绳子，请把绳子剪成m段（m、n都是整数，n>1并且m>1）。
# 每段的绳子的长度记为k[0]、k[1]、……、k[m]。k[0] * k[1]*…*k[m]可能的最大乘积是多少？
# 例如当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到最大的乘积18。

class Solution:
    # 动态规划
    # F(5) 可以分解成 F(1)和F(4)； F(2)和F(3)；
    # 然后F(4)可以分解成F(1)和F(3)；F(2)和F(2)；
    # F(3)又可以分解成F(1)和F(2)；F(1)和F(1)和F(1)；
    # 因此f(n)=max(f(i)*f(n-i))
    def maxProfuctAfterCutting(self, length):
        if length == 0:return 0
        if length == 1:return 1
        if length == 2:return 2
        dp = [0] * (length)
        dp[:3] = [0,1,2,3]
        # print(dp)
        for i in range(4,length + 1):
            max = 0
            for j in range(i//2 + 1):
                tmp = dp[j] * dp[i-j]
                if tmp>max:
                    max = tmp
            dp[i] = max
        return dp[-1]
        
    # 贪心算法
    # 当n>=5时，我们尽可能多地剪长度为3的绳子，
    # 当剩下的绳子长度为4时，把绳子剪成两段长度为2的绳子
    def maxProfuctAfterCutting2(self, length):
        import math
        if length == 0:return 0
        if length == 1:return 1
        if length == 2:return 2
        timesOf3 = length//3
        if length-timesOf3*3==1: #最后一段是4就不用剪
            timesOf3 -= 1

        timesOf2 = (length-timesOf3*3)//2 #能被3整除的部分去掉，剩下长度是2的部分
        f = math.pow(3, timesOf3) * math.pow(2, timesOf2)
        return int(f)
obj = Solution()
print(obj.maxProfuctAfterCutting(0))
print(obj.maxProfuctAfterCutting(1))
print(obj.maxProfuctAfterCutting(2))
print(obj.maxProfuctAfterCutting(3))
print(obj.maxProfuctAfterCutting(4))
print(obj.maxProfuctAfterCutting2(5))

