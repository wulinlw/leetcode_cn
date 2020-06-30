#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
# https://leetcode-cn.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (42.58%)
# Likes:    327
# Dislikes: 0
# Total Accepted:    51.5K
# Total Submissions: 119.5K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s
# 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。
# 
# 示例: 
# 
# 输入: s = 7, nums = [2,3,1,2,4,3]
# 输出: 2
# 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
# 
# 
# 进阶:
# 
# 如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
# 
#
from typing import List
# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:return 0
        n = len(nums)
        re = n + 1
        l, r = 0, 0
        allsum = 0
        while r < n:
            allsum += nums[r]
            while allsum >= s:
                re = min(re, r-l+1)
                allsum -= nums[l]
                l += 1
            r += 1
        return 0 if re == n+1 else re
# @lc code=end

s = 7
nums = [2,3,1,2,4,3]
o = Solution()
print(o.minSubArrayLen(s, nums))