#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#
# https://leetcode-cn.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (70.45%)
# Likes:    89
# Dislikes: 0
# Total Accepted:    15.8K
# Total Submissions: 22.4K
# Testcase Example:  '3\n7'
#
# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
# 
# 说明：
# 
# 
# 所有数字都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
# 
# 
# 示例 2:
# 
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        re = []
        def backtrack(nums, n, idx, tmp):
            if n==0 and len(tmp)==k:
                re.append(tmp[:])
                return 
            for i in range(idx, len(nums)):
                tmp.append(nums[i])
                backtrack(nums, n-nums[i], i+1, tmp)
                tmp.pop()
        nums = list(range(1,10))
        backtrack(nums, n, 0, [])
        return re




# @lc code=end

k = 3
n = 7
k = 3
n = 9
o = Solution()
print(o.combinationSum3(k, n))
