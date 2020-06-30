#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
# https://leetcode-cn.com/problems/jump-game-ii/description/
#
# algorithms
# Hard (33.23%)
# Likes:    424
# Dislikes: 0
# Total Accepted:    39.8K
# Total Submissions: 117.9K
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个非负整数数组，你最初位于数组的第一个位置。
# 
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
# 
# 示例:
# 
# 输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
# 从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
# 
# 
# 说明:
# 
# 假设你总是可以到达数组的最后一个位置。
# 
#
from typing import List
# @lc code=start
class Solution:
    # 贪心算法
    # 每一步可以跳到n个位置，在这n个位置中找到最大的跳过去，以这个起点在跳下一步
    # 这样每一步都是最优解
    # https://leetcode-cn.com/problems/jump-game-ii/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-10/
    def jump(self, nums: List[int]) -> int:
        end = 0                                 #当前能跳到的最远位置，即走到这才算一步
        maxJump = 0
        re = 0
        for i in range(len(nums)-1):
            maxJump = max(maxJump, i+nums[i])
            if i == end:                        #每次走到边界时，更新下一个落脚点，步数+1
                end = maxJump
                re += 1
        return re

# @lc code=end
nums = [2,3,1,1,4]
o = Solution()
print(o.jump(nums))