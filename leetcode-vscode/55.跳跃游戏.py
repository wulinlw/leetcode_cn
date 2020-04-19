#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
# https://leetcode-cn.com/problems/jump-game/description/
#
# algorithms
# Medium (38.16%)
# Likes:    566
# Dislikes: 0
# Total Accepted:    85K
# Total Submissions: 217.2K
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 
# 判断你是否能够到达最后一个位置。
# 
# 示例 1:
# 
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
# 
# 
# 示例 2:
# 
# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # 贪心算法
    def canJump(self, nums: List[int]) -> bool:
        maxJump = 0                                 #最大能跳到的地方
        for i in range(len(nums)):
            if i <= maxJump:                        #大于maxJump的，不能到达
                maxJump = max(maxJump, i+nums[i])   #更新能跳到的最远位置
                if maxJump >= len(nums)-1:          #超过数组长度，直接返回
                    return True
        return False

    # 简化
    def canJump2(self, nums: List[int]) -> bool: 
        maxJump = 0 
        for i in range(len(nums)):
            if i > maxJump:return False
            maxJump = max(maxJump, i+nums[i])
        return True

# @lc code=end
nums = [2,3,1,1,4]
nums = [3,2,1,0,4]
o = Solution()
print(o.canJump(nums))