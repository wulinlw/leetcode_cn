#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
# https://leetcode-cn.com/problems/permutations-ii/description/
#
# algorithms
# Medium (57.13%)
# Likes:    243
# Dislikes: 0
# Total Accepted:    44.3K
# Total Submissions: 77.1K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
# 
# 示例:
# 
# 输入: [1,1,2]
# 输出:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
#
from typing import List
# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        re = []
        def backtrack(nums, tmp):
            if len(nums)==0:
                re.append(tmp[:])
                return
            for i in range(len(nums)):
                if i>0 and nums[i-1]==nums[i]:continue
                # tmp.append(nums[i])                           #这种写法也行
                # backtrack(nums[:i]+nums[i+1:], tmp)
                # tmp.pop()
                backtrack(nums[:i]+nums[i+1:], [nums[i]]+tmp)   #这里主要是拿了这个元素后，需要从备选中剔除，不然就重复了
        
        nums.sort()
        backtrack(nums, [])
        return re

# @lc code=end

nums = [1,1,2]
o = Solution()
print(o.permuteUnique(nums))