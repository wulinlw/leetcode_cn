#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# https://leetcode-cn.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (60.37%)
# Likes:    216
# Dislikes: 0
# Total Accepted:    44.7K
# Total Submissions: 73.7K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的每个数字在每个组合中只能使用一次。
# 
# 说明：
# 
# 
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
# 示例 2:
# 
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
# [1,2,2],
# [5]
# ]
# 
#
from typing import List
# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        re = []
        # idx当前索引，tmp记录路径
        def backtrack(arr, target, idx, tmp):
            if target < 0:return            #剪枝
            if target == 0:
                re.append(tmp[:])
                return
            for i in range(idx, len(arr)):
                if candidates[i] > target:break
                if i>idx and candidates[i-1] == candidates[i]:      #和前一个相同的跳过,注意i>idx 注意这是在同一层循环里才可以生效，而不影响candidates中重复的元素
                    continue
                tmp.append(candidates[i])
                backtrack(candidates, target-candidates[i], i+1, tmp)   
                tmp.pop()
        candidates.sort()#配合剪枝
        backtrack(candidates, target, 0, [])
        return re





# @lc code=end

candidates = [10,1,2,7,6,1,5]
target = 8
candidates = [2,5,2,1,2]
target = 5
o = Solution()
print(o.combinationSum2(candidates, target))