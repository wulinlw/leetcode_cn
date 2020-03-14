#
# @lc app=leetcode.cn id=908 lang=python3
#
# [908] 最小差值 I
#
# https://leetcode-cn.com/problems/smallest-range-i/description/
#
# algorithms
# Easy (67.71%)
# Likes:    45
# Dislikes: 0
# Total Accepted:    9.5K
# Total Submissions: 14K
# Testcase Example:  '[1]\n0'
#
# 给定一个整数数组 A，对于每个整数 A[i]，我们可以选择任意 x 满足 -K <= x <= K，并将 x 加到 A[i] 中。
# 
# 在此过程之后，我们得到一些数组 B。
# 
# 返回 B 的最大值和 B 的最小值之间可能存在的最小差值。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：A = [1], K = 0
# 输出：0
# 解释：B = [1]
# 
# 
# 示例 2：
# 
# 输入：A = [0,10], K = 2
# 输出：6
# 解释：B = [2,8]
# 
# 
# 示例 3：
# 
# 输入：A = [1,3,6], K = 3
# 输出：0
# 解释：B = [3,3,3] 或 B = [4,4,4]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 10000
# 0 <= A[i] <= 10000
# 0 <= K <= 10000
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # 假设 A 是原始数组，B 是修改后的数组，
    # 我们需要最小化 max(B) - min(B)
    # max(B) 最小可能为 max(A) - K，因为 max(A) 不可能再变得更小。
    # min(B) 最大可能为 min(A) + K。
    # 所以结果 max(B) - min(B) 至少为 ans = (max(A) - K) - (min(A) + K)。
    #                                   =max(A) - min(A) - 2*K
    def smallestRangeI(self, A: List[int], K: int) -> int:
        return max(0, max(A) - min(A) - 2*K)


# @lc code=end
A = [1]
K = 0
A = [0,10]
K = 2
A = [1,3,9]
K = 3
o = Solution()
print(o.smallestRangeI(A, K))
