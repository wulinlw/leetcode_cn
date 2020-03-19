#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
# https://leetcode-cn.com/problems/subsets-ii/description/
#
# algorithms
# Medium (59.25%)
# Likes:    170
# Dislikes: 0
# Total Accepted:    25.2K
# Total Submissions: 42.6K
# Testcase Example:  '[1,2,2]'
#
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: [1,2,2]
# 输出:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
#
from typing import List
# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        re = []
        def backtrack(nums, idx, tmp):
            if idx >len(nums):return 
            re.append(tmp[:])
            for i in range(idx, len(nums)):
                if i>idx and nums[i-1]==nums[i]:continue    #在同一层循环中，和前一个相同的跳过,注意i>idx，数组中有重复的没有影响（i==idx时）
                tmp.append(nums[i])
                backtrack(nums, i+1, tmp)
                tmp.pop()
        nums.sort()
        backtrack(nums, 0, [])
        return re
# @lc code=end

nums = [1,2,2]
o = Solution()
print(o.subsetsWithDup(nums))