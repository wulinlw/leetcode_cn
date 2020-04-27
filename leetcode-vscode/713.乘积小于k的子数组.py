#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于K的子数组
#
# https://leetcode-cn.com/problems/subarray-product-less-than-k/description/
#
# algorithms
# Medium (34.66%)
# Likes:    109
# Dislikes: 0
# Total Accepted:    5.8K
# Total Submissions: 16.4K
# Testcase Example:  '[10,5,2,6]\n100'
#
# 给定一个正整数数组 nums。
# 
# 找出该数组内乘积小于 k 的连续的子数组的个数。
# 
# 示例 1:
# 
# 
# 输入: nums = [10,5,2,6], k = 100
# 输出: 8
# 解释: 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
# 需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
# 
# 
# 说明:
# 
# 
# 0 < nums.length <= 50000
# 0 < nums[i] < 1000
# 0 <= k < 10^6
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # 双指针
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        prod = 1
        re = left = 0
        for right, x in enumerate(nums):
            prod *= x
            while prod >= k:
                prod /= nums[left]
                left += 1
            re += right - left + 1
        return re


# @lc code=end

nums = [10,5,2,6]
k = 100
o = Solution()
print(o.numSubarrayProductLessThanK(nums, k))