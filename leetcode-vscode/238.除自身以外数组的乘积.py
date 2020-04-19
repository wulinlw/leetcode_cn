#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#
# https://leetcode-cn.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (66.55%)
# Likes:    363
# Dislikes: 0
# Total Accepted:    35.5K
# Total Submissions: 52.6K
# Testcase Example:  '[1,2,3,4]'
#
# 给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i]
# 之外其余各元素的乘积。
# 
# 
# 
# 示例:
# 
# 输入: [1,2,3,4]
# 输出: [24,12,8,6]
# 
# 
# 
# 提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。
# 
# 说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
# 
# 进阶：
# 你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
# 
#
from typing import List
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        re = [0] * len(nums)
        k = 1
        for i in range(len(nums)):          #从左到右
            re[i] = k
            k = k * nums[i]                 #此时数组存储的是除去当前元素左边的元素乘积
        k = 1
        for i in range(len(nums)-1, -1, -1):#从右到左
            re[i] *= k                      #k为该数右边的乘积
            k = k * nums[i]                 #左 * 右
        return re






# @lc code=end
nums = [1,2,3,4]
o = Solution()
print(o.productExceptSelf(nums))