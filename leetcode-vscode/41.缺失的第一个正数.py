#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
# https://leetcode-cn.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (37.61%)
# Likes:    487
# Dislikes: 0
# Total Accepted:    48.5K
# Total Submissions: 127.1K
# Testcase Example:  '[1,2,0]'
#
# 给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
# 
# 
# 
# 示例 1:
# 
# 输入: [1,2,0]
# 输出: 3
# 
# 
# 示例 2:
# 
# 输入: [3,4,-1,1]
# 输出: 2
# 
# 
# 示例 3:
# 
# 输入: [7,8,9,11,12]
# 输出: 1
# 
# 
# 
# 
# 提示：
# 
# 你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。
# 
#
from typing import List
# @lc code=start
class Solution:
    # 鸽巢原理
    # 剑指offer3 数组中重复的数字
    # 3 应该放在索引为 2 的地方
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i]-1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1


    def firstMissingPositive2(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):                          #1、将小于0的设为n+1，不影响后面的处理
            if nums[i] <= 0:
                nums[i] = n + 1
        
        for i in range(n):                          #2、将当前数字对应的索引所在值，标为负数，和鸽巢原理一样
            num = abs(nums[i])                      #   没有标记的就是没有出现过的
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])
        
        for i in range(n):                          #3、大于0的那个索引+1，就是没有出现的，都出现过就返回n+1
            if nums[i] > 0:
                return i + 1
        
        return n + 1


# @lc code=end
nums = [1,2,0]
nums = [3,4,-1,1]
o = Solution()
print(o.firstMissingPositive(nums))