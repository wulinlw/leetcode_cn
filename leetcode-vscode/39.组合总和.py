#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# https://leetcode-cn.com/problems/combination-sum/description/
#
# algorithms
# Medium (68.50%)
# Likes:    554
# Dislikes: 0
# Total Accepted:    72.5K
# Total Submissions: 105.8K
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 
# candidates 中的数字可以无限制重复被选取。
# 
# 说明：
# 
# 
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
# 
# 
# 示例 1:
# 
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# 示例 2:
# 
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
# 
#
from typing import List
# @lc code=start
class Solution:
    #这里用都减法，也可以用加法
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        re = []
        # idx当前索引，tmp记录路径
        def backtrack(arr, target, idx, tmp):
            if target < 0:return            #剪枝
            if target == 0:
                re.append(tmp[:])
                return
            for i in range(idx, len(arr)):#下面会设置start，每次递归的时候只在candidates中当前及之后的数字中选择。
                tmp.append(candidates[i])
                backtrack(candidates, target-candidates[i], i, tmp) #注意i没有+1，这样就可以重复选择同一个数
                tmp.pop()
        backtrack(candidates, target, 0, [])
        return re




# @lc code=end

candidates = [2,3,6,7]
target = 7
# candidates = [2,3,5]
# target = 8
o = Solution()
print(o.combinationSum(candidates, target))