#!/usr/bin/python
#coding:utf-8

# 最大子序和
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

# 示例:
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 进阶:

# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

# https://blog.csdn.net/weixin_41958153/article/details/81131379
# https://blog.csdn.net/yangfengyougu/article/details/81807950
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)  
        for i in range(1,length):  
            #当前值的大小与前面的值之和比较，若当前值更大，则取当前值，舍弃前面的值之和  
            subMaxSum=max(nums[i]+nums[i-1],nums[i])  
            nums[i]=subMaxSum#将当前和最大的赋给nums[i]，新的nums存储的为和值  
        return max(nums)

    #遍历法 ，非动态规划，仅供参考
    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        MaxSum = nums[0]
        for i in range(len(nums)):
            sum += nums[i]
            MaxSum = max(sum, MaxSum)
            if sum < 0:
                sum = 0
        return MaxSum

n = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
re = s.maxSubArray(n)
print("deep:",re)

        














