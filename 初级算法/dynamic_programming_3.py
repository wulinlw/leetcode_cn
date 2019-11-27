#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/23/dynamic-programming/56/
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
            # 则每一步存储的都是当前步和前一步的最大值  
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

    # 分治法
    # https://leetcode-cn.com/problems/maximum-subarray/solution/bao-li-qiu-jie-by-pandawakaka/
    def maxSubArray3(self, nums):
        n = len(nums)
        mid = n//2
        #递归终止条件
        if n == 1:
            return nums[0]
        else:
            #递归计算左半边最大子序和
            max_left = self.maxSubArray(nums[0:mid])
            #递归计算右半边最大子序和
            max_right = self.maxSubArray(nums[mid:n])
        
        #计算中间的最大子序和，从中到左计算左边的最大子序和，从中到右计算右边的最大子序和，再相加
        max_l = nums[mid - 1]#左边最大值
        tmp = 0
        for i in range(mid - 1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        max_r = nums[mid]#右边最大值
        tmp = 0
        for i in range(mid, n):
            tmp += nums[i]
            max_r = max(tmp, max_r)
        #返回三个中的最大值
        return max(max_right,max_left,max_l+max_r) 



n = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution()
re = s.maxSubArray3(n)
print("deep:",re)

        














