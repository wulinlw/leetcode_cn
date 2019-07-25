#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/featured/card/top-interview-quesitons-in-2018/264/array/1135/
# 除自身以外数组的乘积
# 给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

# 示例:
# 输入: [1,2,3,4]
# 输出: [24,12,8,6]
# 说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

# 进阶：
# 你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）


# https://blog.csdn.net/qq_39241986/article/details/83960209
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1    # 原始数据下标
        n = len(nums)  # 原始列表长度
        output = []  # 返回列表
        for i in range(0,n):
            # 第一个for循环，实现求前n位数的乘积,并把结果存储在output列表
            output.append(p)
            p = p * nums[i]
        p = 1  # 回到最原始数据下标
        for i in range(n-1,-1,-1):
            print i 
	        # 第二个for循环，倒序遍历，实现题目要求,并把结果存储在output列表
            output[i] = output[i] * p
            p = p * nums[i] # 求后n-i位的积
        return output



nums = [1,2,3,4]
s = Solution()
res = s.productExceptSelf(nums)
print(res)
