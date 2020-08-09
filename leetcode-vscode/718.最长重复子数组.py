#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#
# https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (50.11%)
# Likes:    194
# Dislikes: 0
# Total Accepted:    14.5K
# Total Submissions: 28.4K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
# 
# 示例 1:
# 
# 
# 输入:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出: 3
# 解释: 
# 长度最长的公共子数组是 [3, 2, 1]。
# 
# 
# 说明:
# 
# 
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    #动态规划
    # dp[i][j]表示 A[i:] 和 B[j:] 的最长公共前缀
    # dp[i][j] = dp[i+1][j+1] + 1
    def findLength(self, A: List[int], B: List[int]) -> int:
        n, m  = len(A), len(B)
        dp = [[0]* (m+1) for i in range(n+1)]
        re = 0
        for i in range(n-1, -1, -1):                #dp[i][j]从dp[i+1][j+1]计算来，所以倒推
            for j in range(m-1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = 0
                re = max(re, dp[i][j])
        return re
    
    #滑动窗口
    def findLength2(self, A: List[int], B: List[int]) -> int:
        #返回a,b相同字符的长度
        def maxLength(addA: int, addB: int, length: int) -> int:
            ret = k = 0
            for i in range(length):
                if A[addA + i] == B[addB + i]:
                    k += 1
                    ret = max(ret, k)
                else:
                    k = 0
            return ret
        
        n, m = len(A), len(B)
        ret = 0
        for i in range(n):                          #滑动A，和B的第0位对齐
            length = min(m, n - i)                  #剩下的最长长度
            ret = max(ret, maxLength(i, 0, length))
        for i in range(m):                          #滑动B
            length = min(n, m - i)
            ret = max(ret, maxLength(0, i, length))
        return ret


# @lc code=end
A = [1,2,3,2,1]
B = [3,2,1,4,7]
o = Solution()
print(o.findLength(A, B))
