#
# @lc app=leetcode.cn id=201 lang=python3
#
# [201] 数字范围按位与
#
# https://leetcode-cn.com/problems/bitwise-and-of-numbers-range/description/
#
# algorithms
# Medium (46.87%)
# Likes:    159
# Dislikes: 0
# Total Accepted:    18.8K
# Total Submissions: 39.3K
# Testcase Example:  '5\n7'
#
# 给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。
# 
# 示例 1: 
# 
# 输入: [5,7]
# 输出: 4
# 
# 示例 2:
# 
# 输入: [0,1]
# 输出: 0
# 
#

# @lc code=start
class Solution:
    # 给定两个整数，我们要找到它们对应的二进制字符串的公共前缀。
    # 我们的想法是将两个数字不断向右移动，直到数字相等，即数字被缩减为它们的公共前缀。
    # 然后，通过将公共前缀向左移动，将零添加到公共前缀的右边以获得最终结果。
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0   
        # 找到公共前缀
        while m < n:
            m = m >> 1      #m，n同时右移，知道找到公共前缀，这时就就相等了，
            n = n >> 1
            shift += 1      #shift就是右移的位数，最后在左移shift，右边就自动补齐了0
        return m << shift

    # Brian Kernighan 算法
    # 我们每次对 number 和 number−1 之间进行按位与运算后，number 中最右边的 1 会被抹去变成 0。
    # 基于上述技巧，我们可以用它来计算两个二进制字符串的公共前缀。
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            # 抹去最右边的 1
            n = n & (n - 1)
        return n


# @lc code=end

