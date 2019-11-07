#!/usr/bin/python
#coding:utf-8
import math
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/25/math/62/
# 3的幂
# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。

# 示例 1:

# 输入: 27
# 输出: true
# 示例 2:

# 输入: 0
# 输出: false
# 示例 3:

# 输入: 9
# 输出: true
# 示例 4:

# 输入: 45
# 输出: false
# 进阶：
# 你能不使用循环或者递归来完成本题吗？


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1

    def isPowerOfThree2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1:
            return True
        if n % 3 == 0:
            return self.isPowerOfThree(n // 3)
        else:
            return False

    def isPowerOfThree3(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return 3 ** round(math.log(n, 3)) == n


n=12
s = Solution()
re = s.isPowerOfThree(n)
print("deep:",re)

