#
# @lc app=leetcode.cn id=523 lang=python3
#
# [523] 连续的子数组和
#
# https://leetcode-cn.com/problems/continuous-subarray-sum/description/
#
# algorithms
# Medium (22.81%)
# Likes:    88
# Dislikes: 0
# Total Accepted:    8.9K
# Total Submissions: 38.7K
# Testcase Example:  '[23,2,4,6,7]\n6'
#
# 给定一个包含非负数的数组和一个目标整数 k，编写一个函数来判断该数组是否含有连续的子数组，其大小至少为 2，总和为 k 的倍数，即总和为 n*k，其中 n
# 也是一个整数。
# 
# 示例 1:
# 
# 输入: [23,2,4,6,7], k = 6
# 输出: True
# 解释: [2,4] 是一个大小为 2 的子数组，并且和为 6。
# 
# 
# 示例 2:
# 
# 输入: [23,2,6,4,7], k = 6
# 输出: True
# 解释: [23,2,6,4,7]是大小为 5 的子数组，并且和为 42。
# 
# 
# 说明:
# 
# 
# 数组的长度不会超过10,000。
# 你可以认为所有数字总和在 32 位有符号整数范围内。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # 前缀和，hash
    # 类似 leetcode 560
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        m = {}
        m[0] = -1
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if k != 0:                  #要求是k的倍数，这里统一取余,同余处理
                sum = sum % k
            if sum in m:                
                if i - m[sum] > 1:      #当前i距离上一个至少有2个
                    return True
            else:
                m[sum] = i              #这里存的是索引
        return False
        
# @lc code=end
nums = [23,2,4,6,7]
k = 6
o = Solution()
print(o.checkSubarraySum(nums, k))