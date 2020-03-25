#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] 完全平方数
#
# https://leetcode-cn.com/problems/perfect-squares/description/
#
# algorithms
# Medium (54.07%)
# Likes:    337
# Dislikes: 0
# Total Accepted:    44.6K
# Total Submissions: 81.2K
# Testcase Example:  '12'
#
# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
# 
# 示例 1:
# 
# 输入: n = 12
# 输出: 3 
# 解释: 12 = 4 + 4 + 4.
# 
# 示例 2:
# 
# 输入: n = 13
# 输出: 2
# 解释: 13 = 4 + 9.
# 
#
import math
# @lc code=start
class Solution:
    # [322] 零钱兑换 一样的
    def numSquares(self, n: int) -> int:
        arr = [i*i for i in range(1, int(math.sqrt(n)+1))]
        # print(arr)
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        for i in range(len(dp)):
            for j in arr: 
                if i-j<0:continue 
                dp[i] = min(dp[i], dp[i-j]+1)
        # print(dp)
        return dp[-1]
                


# @lc code=end

o = Solution()
print(o.numSquares(12))
print(o.numSquares(13))