#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/featured/card/top-interview-quesitons-in-2018/272/dynamic-programming/1178/
# 完全平方数
# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

# 示例 1:
# 输入: n = 12
# 输出: 3 
# 解释: 12 = 4 + 4 + 4.
# 示例 2:

# 输入: n = 13
# 输出: 2
# 解释: 13 = 4 + 9.

# https://blog.csdn.net/qq_17550379/article/details/80875782
# https://blog.csdn.net/weixin_43730955/article/details/88102249
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 转化为完全背包dp
        from math import sqrt
        ans = n
        maxn = int(sqrt(n))
        print maxn
        dp = [_ for _ in range(n + 1)]#[1,2,3...n]
        print dp
        for i in range(1, maxn + 1):
            for j in range(i * i, n + 1):
                dp[j] = min(dp[j], dp[j - i * i] + 1)
        return dp[n]

    def numSquares2(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math 
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        for a in range(0, int(math.sqrt(n) + 1)): 
            b = int(math.sqrt(n - a * a))
            if a * a + b * b == n:
                if a != 0 and b != 0:
                    return 2
                else:
                    return 1
        
        return 3

n = 12
s = Solution()
res = s.numSquares(n)
print(res)
