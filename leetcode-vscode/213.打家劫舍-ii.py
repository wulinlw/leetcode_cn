#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#
# https://leetcode-cn.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (36.59%)
# Likes:    216
# Dislikes: 0
# Total Accepted:    26.1K
# Total Submissions: 70.3K
# Testcase Example:  '[2,3,2]'
#
# 
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
# 
# 示例 1:
# 
# 输入: [2,3,2]
# 输出: 3
# 解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
# 
# 
# 示例 2:
# 
# 输入: [1,2,3,1]
# 输出: 4
# 解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
# 偷窃到的最高金额 = 1 + 3 = 4 。
# 
#
from typing import List
# @lc code=start
class Solution:
    # 收尾相连，则只能偷一个，分解成子问题
    # 1、偷第一个，不偷最后一个
    # 2、偷最后一个，不偷第一个
    # 最后看那个收益大
    def rob(self, nums: List[int]) -> int:
        #198题代码
        # dp[i] = max(dp[i-2]+num[i], dp[i-1])
        def rob198(nums):
            if len(nums)==1:return nums[0]
            dp = [0] * (len(nums))
            maxval = 0
            for i in range(len(nums)):
                dp[i] = max(dp[i-2]+nums[i], dp[i-1])
                maxval = max(maxval, dp[i])
            return maxval

        if len(nums)==1:return nums[0]
        return max(rob198(nums[:-1]), rob198(nums[1:]))





# @lc code=end

# nums = [2,3,2]
# nums = [1,2,3,1]
# nums = [1,2]
nums = [1,2,1,1]

o = Solution()
print(o.rob(nums))