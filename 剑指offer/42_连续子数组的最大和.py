#!/usr/bin/python
#coding:utf-8

# // 面试题42：连续子数组的最大和
# // 题目：输入一个整型数组，数组里有正数也有负数。数组中一个或连续的多个整
# // 数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为O(n)。
import heapq
class Solution:
    def FindGreatestSumOfSubArray(self, nums):
        n = len(nums)
        dp = [float('-inf')] * n
        maxSubSum = float('-inf')
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i]=max(nums[i], dp[i-1]+nums[i])
            maxSubSum = max(maxSubSum, dp[i])
        # print(dp)
        return maxSubSum
        
    def FindGreatestSumOfSubArray2(self, nums):
        sum = nums[0]
        maxSum = 0
        for i in nums:
            if sum>0:
                sum += i
            else:
                sum = i
            maxSum = max(maxSum, sum)
        return maxSum


nums = [1,-2,3,10,-4,7,2,-5]

obj = Solution()
re = obj.FindGreatestSumOfSubArray2(nums)
print(re)
