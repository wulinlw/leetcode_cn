#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/53/math/113/
#  阶乘后的零
# 给定一个整数 n，返回 n! 结果尾数中零的数量。

# 示例 1:
# 输入: 3
# 输出: 0
# 解释: 3! = 6, 尾数中没有零。

# 示例 2:
# 输入: 5
# 输出: 1
# 解释: 5! = 120, 尾数中有 1 个零.
# 说明: 你算法的时间复杂度应为 O(log n) 。

# https://blog.csdn.net/qq_34364995/article/details/80544147
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 求0也就是求其中2*5的个数，也就是5的个数，因为每一个偶数都含2，只要有5肯定有2。遍历求能不能被5整除
        r = 0
        while n >= 5:
            n = n // 5
            r+=n
        return r




nums = 3
s = Solution()
n = s.trailingZeroes(nums)
print(n)









