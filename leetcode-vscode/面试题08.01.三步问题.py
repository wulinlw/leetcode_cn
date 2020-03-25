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
    def waysToStep(self, n: int) -> int:
        if n<=2:return n
        dp1,dp2,dp3 = 1,2,4 #1,2,3的情况
        for _ in range(4,n+1):
            tmp = dp3
            dp3 = (dp1+dp2+dp3) % 1000000007    #在这里就处理大数问题，
            dp1 = dp2 
            dp2 = tmp
        return dp3                              #只在这里处理%超级慢



o = Solution()
print(o.waysToStep(5))
print(o.waysToStep(900750))
# 111
# 12
# 21
# 3