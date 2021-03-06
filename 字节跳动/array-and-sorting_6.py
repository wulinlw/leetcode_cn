#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/bytedance/243/array-and-sorting/1019/
# 最长连续序列
# 给定一个未排序的整数数组，找出最长连续序列的长度。
# 要求算法的时间复杂度为 O(n)。

# 示例:
# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)#去重,重复数字在此题中没有意义
        maxn = 0
        for i in nums:
            if i - 1 not in nums:# 如果前一个数在nums中，说明当前数已经被处理过了
                n = i +1#当前数下一个
                while n in nums:#找到连续的，给到maxn，只留最大的
                    n = n + 1
                maxn = max(maxn, n - i)#n-i 连续数字的长度
            # print(i,maxn)
        return maxn

nums = [100, 4, 200, 1, 3, 2]
nums = [1,3,5,4,7]
s = Solution()
n = s.longestConsecutive(nums)
print(n)












