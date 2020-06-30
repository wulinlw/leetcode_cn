#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子序列
#
# https://leetcode-cn.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (37.38%)
# Likes:    530
# Dislikes: 0
# Total Accepted:    58.6K
# Total Submissions: 150.4K
# Testcase Example:  '[2,3,-2,4]'
#
# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
# 
# 
# 
# 示例 1:
# 
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 
# 
# 示例 2:
# 
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
# 
#
from typing import List
# @lc code=start
class Solution:
    # 标签：动态规划
    # 遍历数组时计算当前最大值，不断更新
    # 令imax为当前最大值，则当前最大值为 imax = max(imax * nums[i], nums[i])
    # 由于存在负数，那么会导致最大的变最小的，最小的变最大的。因此还需要维护当前最小值imin，imin = min(imin * nums[i], nums[i])
    # 当负数出现时则imax与imin进行交换再进行下一步计算
    # 时间复杂度：O(n)O(n)
    def maxProduct2(self, nums: List[int]) -> int:
        maxval = float('-inf')
        imax, imin = 1, 1
        for i in range(len(nums)):
            if nums[i] < 0:                         #当前是负数时，大正数*负数变得最小，交换最大值和最小值
                imax, imin = imin, imax
            imax = max(imax * nums[i], nums[i])
            imin = min(imin * nums[i], nums[i])
            maxval = max(maxval, imax)
        return maxval

    # 非常适合动态规划教学的思路
    # https://leetcode-cn.com /problems/maximum-product-subarray/solution/dong-tai-gui-hua-li-jie-wu-hou-xiao-xing-by-liweiw/
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:return 0
        dp = [[0,0] for i in range(n)]

        dp[0][0] = nums[0]
        dp[0][1] = nums[0]
        re = nums[0]
        for i in range(1, n):
            if nums[i] >= 0:
                dp[i][0] = min(nums[i], dp[i-1][0] * nums[i])
                dp[i][1] = max(nums[i], dp[i-1][1] * nums[i])
            else:
                dp[i][0] = min(nums[i], dp[i-1][1] * nums[i])
                dp[i][1] = max(nums[i], dp[i-1][0] * nums[i])
            re = max(re, dp[i][1])
        return re

# @lc code=end
nums = [2,3,-2,4]
nums = [-4,-3]
o = Solution()
print(o.maxProduct(nums))
