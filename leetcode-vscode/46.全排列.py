#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (74.17%)
# Likes:    567
# Dislikes: 0
# Total Accepted:    89.9K
# Total Submissions: 120.8K
# Testcase Example:  '[1,2,3]'
#
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
# 
# 示例:
# 
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
#
from typing import List
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        re = []
        def backtrack(nums, tmp):
            if len(nums)==0:
                re.append(tmp[:])
                return 
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:], [nums[i]]+tmp)
        backtrack(nums, [])
        return re

    def permute2(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, idx):
            if idx == len(nums)-1:
                re.append(nums[:])
                return
            for i in range(idx, len(nums)):
                nums[i],nums[idx] = nums[idx],nums[i]
                backtrack(nums, idx+1)
                nums[i],nums[idx] = nums[idx],nums[i]
        re = []
        backtrack(nums, 0)
        return re
# @lc code=end

nums = [1,2,3]
o = Solution()
print(o.permute(nums))
