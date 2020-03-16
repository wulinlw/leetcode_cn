#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (76.55%)
# Likes:    493
# Dislikes: 0
# Total Accepted:    69.2K
# Total Submissions: 90.1K
# Testcase Example:  '[1,2,3]'
#
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: nums = [1,2,3]
# 输出:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#
from typing import List
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        re = []
        def backtrack(nums, idx, tmp):
            if idx >len(nums):return 
            re.append(tmp[:])
            for i in range(idx, len(nums)):
                tmp.append(nums[i])
                backtrack(nums, i+1, tmp)
                tmp.pop()
        nums.sort()
        backtrack(nums, 0, [])
        return re




# @lc code=end

nums = [1,2,3]
o = Solution()
print(o.subsets(nums))