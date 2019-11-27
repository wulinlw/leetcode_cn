#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/featured/card/array-and-string/201/two-pointer-technique/788/
# 最大连续1的个数
# 给定一个二进制数组， 计算其中最大连续1的个数。

# 示例 1:

# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
# 注意：

# 输入的数组只包含 0 和1。
# 输入数组的长度是正整数，且不超过 10,000。

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = 0#最大长度
        c = 0#当前处理过程中的最大长度
        for n in nums:
            if n:
                c += 1
            else:
                r = max(r, c)
                c = 0
        return max(r, c)



nums = [1,1,0,1,1,1]
s = Solution()
n = s.findMaxConsecutiveOnes(nums)
print(n)       