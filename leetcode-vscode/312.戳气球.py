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
    # https://www.bilibili.com/video/av45180542
    # 状态转移方程 def( i, j ) = max { def( i , k ) + def( k , j )+nums[ i ][ j ][ k ] }   i<k<j
    # 链接：https://leetcode-cn.com/problems/burst-balloons/solution/chao-xiang-xi-hui-su-dao-fen-zhi-dao-dp-by-niu-you/
    def maxCoins(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = [1] + nums + [1]                 #创建虚拟边界
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 2, -1, -1):          #长度递减，不计算虚拟边界 i是begin，j是end,k为在i、j区间划分子问题时的边界
            for j in range(i + 2, n):           #
                maxn = 0                        #维护一个最大值；如果i、j相邻，值为0
                for k in range(i + 1, j):
                    temp = dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j]
                    if temp > maxn:
                        maxn = temp
                dp[i][j] = maxn                 #选择区间最大值
        # print(dp)
        return dp[0][n - 1]
# @lc code=end

nums = [3,1,5,8]
o = Solution()
print(o.maxCoins(nums))