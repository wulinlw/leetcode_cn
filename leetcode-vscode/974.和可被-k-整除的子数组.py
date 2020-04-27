#
# @lc app=leetcode.cn id=974 lang=python3
#
# [974] 和可被 K 整除的子数组
#
# https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/description/
#
# algorithms
# Medium (37.50%)
# Likes:    59
# Dislikes: 0
# Total Accepted:    3.8K
# Total Submissions: 10K
# Testcase Example:  '[4,5,0,-2,-3,1]\n5'
#
# 给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。
# 
# 
# 
# 示例：
# 
# 输入：A = [4,5,0,-2,-3,1], K = 5
# 输出：7
# 解释：
# 有 7 个子数组满足其元素之和可被 K = 5 整除：
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2,
# -3]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 30000
# -10000 <= A[i] <= 10000
# 2 <= K <= 10000
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # 前缀和，hash
    # 类似 leetcode 523
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        m = {}
        m[0] = 1
        sum = 0
        re = 0
        for x in A:
            sum += x
            sum = sum % K       #同余处理
            if sum in m:
                re += m[sum]
                m[sum] += 1
            else:
                m[sum] = 1
        # print(m)
        return re

        
# @lc code=end
A = [4,5,0,-2,-3,1]
K = 5
o = Solution()
print(o.subarraysDivByK(A, K))