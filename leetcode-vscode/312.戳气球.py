#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#
# https://leetcode-cn.com/problems/burst-balloons/description/
#
# algorithms
# Hard (57.74%)
# Likes:    220
# Dislikes: 0
# Total Accepted:    8.9K
# Total Submissions: 15.3K
# Testcase Example:  '[3,1,5,8]'
#
# 有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
# 
# 现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的
# left 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
# 
# 求所能获得硬币的最大数量。
# 
# 说明:
# 
# 
# 你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
# 
# 
# 示例:
# 
# 输入: [3,1,5,8]
# 输出: 167 
# 解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
# coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    #O(n^3)
    # https://www.bilibili.com/video/av45180542
    # dp(left, right) = nums[left] * nums[i] * nums[right] + dp(left, i) + dp(i, right)   left<i<right
    # https://leetcode-cn.com/problems/burst-balloons/solution/chuo-qi-qiu-by-leetcode/
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]                         #两边放1，方便计算
        n = len(nums)
        dp = [[0] * n for _ in range(n)]                #dp table

        for left in range(n-2, -1, -1):                 #从最后一个气球开始
            for right in range(left+2, n):              #left+1 == right,2个气球挨着就没得戳了，需要从left+2开始
                # dp[left][right] = max(nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right] for i in range(left+1, right))
                tmpmax = 0
                for i in range(left+1, right):
                    cur = nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right]
                    tmpmax = max(tmpmax, cur)
                dp[left][right] = tmpmax
        return dp[0][n-1]




# @lc code=end

nums = [3,1,5,8]
o = Solution()
print(o.maxCoins(nums))