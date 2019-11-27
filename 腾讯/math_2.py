#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/tencent/223/math-and-numbers/939/
# 回文数
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

# 示例 1:

# 输入: 121
# 输出: true
# 示例 2:

# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 示例 3:

# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
# 进阶:

# 你能不将整数转为字符串来解决这个问题吗？

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0) or (x != 0 and x % 10 == 0):
            return False
        cmp_num = 0
        while x > cmp_num:
            cmp_num = cmp_num * 10 + x % 10#从右往左取数 + 处理的位数的10倍，最后一样的话x == cmp_num成立
            x //= 10
            # print(x,cmp_num)
        # print(x,cmp_num)
        return x == cmp_num or x == cmp_num // 10#x == cmp_num // 10  ，这个是多*10的情况









n = 121
s = Solution()
n = s.isPalindrome(n)
print(n)       