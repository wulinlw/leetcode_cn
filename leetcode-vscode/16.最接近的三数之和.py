#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (44.24%)
# Likes:    477
# Dislikes: 0
# Total Accepted:    119.6K
# Total Submissions: 264.7K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
# 
# 
# 
# 示例：
# 
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
# 
# 
# 
# 
# 提示：
# 
# 
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = 10**7
        
        for i in range(n):                                  # 枚举 a
            if i > 0 and nums[i] == nums[i - 1]:            # 保证和上一次枚举的元素不相等
                continue
            j, k = i + 1, n - 1                             # 使用双指针枚举 b 和 c
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return target
                if abs(s - target) < abs(best - target):    #当前最小时，更新
                    best = s
                if s > target:                              # 如果和大于 target，移动 c 对应的指针
                    k0 = k - 1
                    while j < k0 and nums[k0] == nums[k]:   # 移动到下一个不相等的元素
                        k0 -= 1
                    k = k0
                else:                                       # 如果和小于 target，移动 b 对应的指针
                    j0 = j + 1
                    while j0 < k and nums[j0] == nums[j]:
                        j0 += 1
                    j = j0
        return best


# @lc code=end

nums = [-1,2,1,-4]
target = 1
s = Solution()
print(s.threeSumClosest(nums, target))