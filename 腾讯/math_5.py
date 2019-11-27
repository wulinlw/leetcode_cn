#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/tencent/223/math-and-numbers/942/
# 2的幂
# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

# 示例 1:
# 输入: 1
# 输出: true
# 解释: 20 = 1
# 示例 2:

# 输入: 16
# 输出: true
# 解释: 24 = 16
# 示例 3:

# 输入: 218
# 输出: false


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # https://leetcode-cn.com/problems/power-of-two/solution/power-of-two-er-jin-zhi-ji-jian-by-jyd/
        # 一定满足 n > 0。
        # 恒有 n & (n - 1) == 0，这是因为：
        # n 二进制最高位为 1，其余所有位为 0；
        # n−1 二进制最高位为 0，其余所有位为 1；
        # 这样相与的时候就都是0了
        return n > 0 and n & (n - 1) == 0








n = 121
s = Solution()
n = s.isPowerOfTwo(n)
print(n)       