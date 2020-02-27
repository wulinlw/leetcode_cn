#!/usr/bin/python
#coding:utf-8

# 剪绳子
# 给你一根长度为n绳子，请把绳子剪成m段（m、n都是整数，n>1并且m>1）。
# 每段的绳子的长度记为k[0]、k[1]、……、k[m]。k[0] * k[1]*…*k[m]可能的最大乘积是多少？
# 例如当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到最大的乘积18。

# F(5) 可以分解成 F(1)和F(4)； F(2)和F(3)；
# 然后F(4)可以分解成F(1)和F(3)；F(2)和F(2)；
# F(3)又可以分解成F(1)和F(2)；F(1)和F(1)和F(1)；
# 因此f(n)=max(f(i)*f(n-i))
class Solution:
    # 动态规划
    # https://leetcode-cn.com/problems/jian-sheng-zi-lcof/solution/xiang-jie-bao-li-di-gui-ji-yi-hua-ji-zhu-dong-tai-/
    # 建立一维动态数组 dp：
    # 边界条件：dp[1] = dp[2] = 1，表示长度为 2 的绳子最大乘积为 1；
    # 状态转移方程：dp[i] = max(dp[i], max((i-j)*j, dp[i-j]*j))，可以这样理解：
    # dp[i]           维持原装，不剪
    # (i - j) * j     从j处见一下，剪下部分是i-j，i-j不剪了
    # dp[i - j]*j     从j处剪一下，剪下部分是i-j，i-j继续剪
    def cuttingRope(self, n) :
        if n<2:return n
        dp = [0 for _ in range(n + 1)]  # dp[0] dp[1]其实没用
        dp[2] = 1  # 初始化
        for i in range(3, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], max((i - j) * j, j * dp[i - j]))
        return dp[n]

    # 贪心算法
    # 当n>=5时，我们尽可能多地剪长度为3的绳子，
    # 当剩下的绳子长度为4时，把绳子剪成两段长度为2的绳子
    def maxProfuctAfterCutting2(self, length):
        import math
        if length == 0:return 0
        if length == 1:return 1
        if length == 2:return 1
        timesOf3 = length//3
        if length-timesOf3*3==1: #最后一段是4就不用剪
            timesOf3 -= 1

        timesOf2 = (length-timesOf3*3)//2 #能被3整除的部分去掉，剩下长度是2的部分
        f = math.pow(3, timesOf3) * math.pow(2, timesOf2)
        return int(f)


obj = Solution()
print(obj.cuttingRope(0))
print(obj.cuttingRope(1))
print(obj.cuttingRope(2))
print(obj.cuttingRope(3))
print(obj.cuttingRope(10))
print(obj.maxProfuctAfterCutting2(10))

