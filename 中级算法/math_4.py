#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/53/math/115/
# Pow(x, n)
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。

# 示例 1:

# 输入: 2.00000, 10
# 输出: 1024.00000
# 示例 2:

# 输入: 2.10000, 3
# 输出: 9.26100
# 示例 3:

# 输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2-2 = 1/22 = 1/4 = 0.25
# 说明:

# -100.0 < x < 100.0
# n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # 根据奇偶幂分类（递归法，迭代法，位运算法）
        # 如果n为偶数，则pow(x,n) = pow(x^2, n/2)；
        # 如果n为奇数，则pow(x,n) = x*pow(x^2, n-1)。
        if n == 0:
            return 1.0
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2 == 0 :
            return self.myPow(x*x,n//2)
        else:
            return self.myPow(x*x,(n-1)//2)*x
            
    def Power2(self, base, exponent):
        if exponent==0: return 1
        if exponent==1: return base
        re = self.Power2(base, exponent>>1)
        re *= re
        if exponent & 1 == 1:#奇数，需要乘以自己
            re *= base
        return re
x = 2.00000
n = 3
s = Solution()
n = s.myPow(x,n)
print(n)









