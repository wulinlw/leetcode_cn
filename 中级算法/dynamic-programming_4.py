#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/51/dynamic-programming/107/
# Longest Increasing Subsequence
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。

# 示例:
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4 
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
# 说明:

# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n2) 。
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # a[i]表示以nums[i]为结尾的最长子序列长度，遍历num[i]之前的数并更新a[i]的值
        # 此算法的复杂度为n2
        a=[1]*len(nums)
        if len(nums)==0:
            return 0
        for i in range(1,len(nums)):
            for j in range(0,i):
                if(nums[i]>nums[j]):
                    a[i]=max(a[i],a[j]+1)
        return max(a)

    # https://blog.csdn.net/qq_17550379/article/details/82871892
    # 此算法的复杂度为O(n log n)
    def lengthOfLIS2(self, nums):
        mem = list()
        len_nums = len(nums)
        for i in range(len_nums):
            low, upper = 0, len(mem)
            while low < upper:
                mid = (upper - low)//2 + low
                if mem[mid] < nums[i]:
                    low = mid + 1
                else:
                    upper = mid

            if upper == len(mem):
                mem.append(nums[i])
            else:
                mem[upper] = nums[i]
        
        return len(mem)

nums = [10,9,2,5,3,7,101,18]
s = Solution()
r = s.lengthOfLIS(nums)
print(r)




