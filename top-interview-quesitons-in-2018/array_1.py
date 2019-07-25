#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/featured/card/top-interview-quesitons-in-2018/264/array/1126/
# 乘积最大子序列
# 给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

# 示例 1:

# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 示例 2:

# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 在第i个元素时，我们能够取到的子序列的最大乘积可能来自：
        # （1）nums[i]本身
        # （2）nums[i-1]能够取到的最大子序列的乘积
        # （3）包含nums[i-1]的最大连乘值 * nums[i] (两个部分均为正数)
        # （4）包含nums[i-1]的最小连乘值 * nums[i] (两个部分均为负数)
        # 因此对于第i个元素，我们需要记录的值有三个：
        # （1）能够取到的子序列的最大乘积
        # （2）包含当前位置的最大连乘值
        # （3）包含当前位置的最小连乘值

        #temp记录整个数组的子序列最大连乘积
        temp = nums[0]
        length = len(nums)
        
        #M数组记录包含当前位置的最大连乘值
        M = [0] * length
        #m数组记录包含当前位置的最小连乘值
        m = [0] * length#负数的时候，当前值也是负数，则负负得正，dp就便变大了
        
        M[0] = m[0] = nums[0]
        for i in range(1,length):
            #包含当前位置的最大连乘值从：当前位置和到第i-1个元素的最大连乘值的乘积、当前元素中选出
            M[i] = max(max(M[i-1]*nums[i],m[i-1]*nums[i]), nums[i])
            m[i] = min(min(M[i-1]*nums[i],m[i-1]*nums[i]), nums[i])
            temp = max(temp,M[i])
        return temp


nums = [2,3,-2,4]
s = Solution()
res = s.maxProduct(nums)
print(res)


