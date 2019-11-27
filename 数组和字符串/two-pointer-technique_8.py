#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/featured/card/array-and-string/201/two-pointer-technique/789/
# 长度最小的子数组
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

# 示例: 
# 输入: s = 7, nums = [2,3,1,2,4,3]
# 输出: 2
# 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
# 进阶:
# 如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # 双指针+滑动窗口 O(n)
        if sum(nums) == s:
            return len(nums)
        if sum(nums) < s:
            return 0
        sum_temp = left = 0
        min_len = len(nums)
        for right in range(len(nums)):
            sum_temp += nums[right]
            # 滑动窗口
            # 当找到》s的数后，不能确定是不是最短的，因为左边已经有很多值加进来了，所以向右滑动left
            # 剪掉这些值，才能找到最短的
            while sum_temp >= s:
                min_len = min(min_len, right-left+1)
                sum_temp -= nums[left]#减去第一个元素
                left += 1#做指针右移一位
        return min_len

    # 思路二：前缀和 + 二分搜索
    # 时间复杂度：O(nlogn)O(nlogn)
    def minSubArrayLen2(self, s: int, nums):
        import bisect
        if not nums : return 0
        # 求前缀和
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        #print(nums)
        # 总和都小于 s 时候
        if nums[-1] < s: return 0
        res = float("inf")
        nums = [0] + nums
        for i in range(1, len(nums)):
            if nums[i] - s >= 0:
                # 二分查找
                loc = bisect.bisect_left(nums, nums[i] - s)
                if nums[i] - nums[loc] >= s:
                    res = min(res, i - loc)
                    continue
                if loc > 0:
                    res = min(res, i - loc + 1)
        return res 


        
s = 7
nums = [2,3,1,2,4,3]
S = Solution()
n = S.minSubArrayLen(s, nums)
print(n)       