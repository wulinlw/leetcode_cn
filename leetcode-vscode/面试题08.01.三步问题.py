#!/usr/bin/python
#coding:utf-8


# 面试题 08.01. 三步问题
# 三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。

# 示例1:
#  输入：n = 3 
#  输出：4
#  说明: 有四种走法

# 示例2:
#  输入：n = 5
#  输出：13
# 提示:

# n范围在[1, 1000000]之间
# https://leetcode-cn.com/problems/three-steps-problem-lcci/


class Solution:
    #迭代，自底向上
    def waysToStep(self, n: int) -> int:
        if n<=2:return n
        dp1,dp2,dp3 = 1,2,4 #1,2,3的情况
        for _ in range(4,n+1):
            tmp = dp3
            dp3 = (dp1+dp2+dp3) % 1000000007    #在这里就处理大数问题，
            dp1 = dp2 
            dp2 = tmp
        return dp3                              #只在这里处理%超级慢

    # 递归法，太大会超过限制maximum recursion
    def waysToStep2(self, n: int) -> int:
        if n<2:return n
        return self.waysToStep(n-1) + self.waysToStep(n-2) + self.waysToStep(n-3)

    # n阶台阶，你一次性可以走1步、2步、3步、n步。一共有多少种走法。
    def waysAnyStep(self, n):
        step = 0
        if n<=1:return 1
        for i in range(1, n+1):
            step += self.waysAnyStep(n-i)
        return step

    #迭代，自底向上
    # f(n) = f(n-1)+f(n-2)+...+f(n-(n-1)) + f(n-n) 
    #       => f(0) + f(1) + f(2) + f(3) + ... + f(n-1)
    # f(n-1) => f(0) + f(1) + f(2) + f(3) + ... + f(n-2)
    # f(n) = { f(0) + f(1) + f(2) + f(3) + ... + f(n-2) } + f(n-1) 
    #      = f(n-1) + f(n-1)
    #      = 2 * f(n-1)
    def waysAnyStep2(self, n):
        if n==1:return 1
        num = 1
        for _ in range(2, n+1):
            num = 2 * num
        return num




o = Solution()
print(o.waysToStep(5))
print(o.waysToStep(900750))
print(o.waysAnyStep(23))
print(o.waysAnyStep2(23))

# 111
# 12
# 21
# 3