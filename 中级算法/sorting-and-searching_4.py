#!/usr/bin/python
#coding:utf-8


# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/50/sorting-and-searching/99/
# 寻找峰值
# 峰值元素是指其值大于左右相邻值的元素。

# 给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

# 数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

# 你可以假设 nums[-1] = nums[n] = -∞。

# 示例 1:

# 输入: nums = [1,2,3,1]
# 输出: 2
# 解释: 3 是峰值元素，你的函数应该返回其索引 2。
# 示例 2:

# 输入: nums = [1,2,1,3,5,6,4]
# 输出: 1 或 5 
# 解释: 你的函数可以返回索引 1，其峰值元素为 2；
#      或者返回索引 5， 其峰值元素为 6。
# 说明:

# 你的解法应该是 O(logN) 时间复杂度的。


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 标准二分法查找
        left = 0
        right = len(nums)-1
        while left <= right:
            print(left, right)
            if left == right:
                return left
            mid = (right +left) // 2 
            # 如果中间小于右边，那么一定在右边
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            # 左边不小于右边，那么直接把右边弄到中间
            else:
                # right不可以是mid-1，万一正好是mid，就跳过了，因为并没有比对mid的值
                right = mid

nums = [1,2,1,3,5,6,4]
s = Solution()
r = s.findPeakElement(nums)
print(r)




