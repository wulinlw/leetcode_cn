#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/featured/card/array-and-string/198/introduction-to-array/771/
# 至少是其他数字两倍的最大数
# 在一个给定的数组nums中，总是存在一个最大元素 。

# 查找数组中的最大元素是否至少是数组中每个其他数字的两倍。
# 如果是，则返回最大元素的索引，否则返回-1。
# 示例 1:

# 输入: nums = [3, 6, 1, 0]
# 输出: 1
# 解释: 6是最大的整数, 对于数组中的其他整数,
# 6大于数组中其他元素的两倍。6的索引是1, 所以我们返回1.
 
# 示例 2:
# 输入: nums = [1, 2, 3, 4]
# 输出: -1
# 解释: 4没有超过3的两倍大, 所以我们返回 -1.
 
# 提示:
# nums 的长度范围在[1, 50].
# 每个 nums[i] 的整数范围在 [0, 100].

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = float('-inf')
        max_index = 0
        second_max_num = float('-inf')
        
        # 找出最大数和第二大数
        for i in range(len(nums)):
            n = nums[i]
            if n > max_num:
                second_max_num = max_num
                max_num = n
                max_index = i
            else:
                if n > second_max_num:
                    second_max_num = n
        
        if max_num >= second_max_num * 2:
            return max_index
        else:
            return -1

    def dominantIndex2(self, nums):
        m = max(nums)
        # all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。
        if all(m >= 2*x for x in nums if x != m):
            return nums.index(m)
        return -1

nums = [1, 7, 3, 6, 5, 6]
s = Solution()
n = s.dominantIndex2(nums)
print(n)       