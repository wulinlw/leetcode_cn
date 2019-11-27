#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/featured/card/array-and-string/201/two-pointer-technique/784/
# 数组拆分 I
# 给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，
# 使得从1 到 n 的 min(ai, bi) 总和最大。

# 示例 1:
# 输入: [1,4,3,2]
# 输出: 4
# 解释: n 等于 2, 最大总和为 4 = min(1, 2) + min(3, 4).
# 提示:

# n 是正整数,范围在 [1, 10000].
# 数组中的元素范围在 [-10000, 10000].

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[::2])

    # 排序后取偶数的和  
    def arrayPairSum2(self, nums):
        nums.sort()
        res = []
        i = 0
        while i<=len(nums)-2:
            min_i = min(nums[i],nums[i+1])
            res.append(min_i)
            i += 2
        return sum(res)


nums = [1,4,3,2]
s = Solution()
n = s.arrayPairSum(nums)
print(n)