#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
# https://leetcode-cn.com/problems/next-permutation/description/
#
# algorithms
# Medium (32.89%)
# Likes:    436
# Dislikes: 0
# Total Accepted:    52.8K
# Total Submissions: 159.7K
# Testcase Example:  '[1,2,3]'
#
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
# 
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
# 
# 必须原地修改，只允许使用额外常数空间。
# 
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#
from typing import List
# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-2
        while i>=0 and nums[i] >= nums[i+1]:    #从右往左找到第一个正序的位置，nums[i]是第一个比较小的数
            i -= 1
        if i >= 0:                              
            j = n-1
            while j>=0 and nums[j] <= nums[i]:  #从右往左找到第一个比nums[i]大的，交换这2个位置，从右往左的高位变的最大了，但整体还不一定是大于原来的树中最小的那个
                j-=1
            nums[i],nums[j] = nums[j],nums[i]
        # print(i,j)
        nums[i+1:] = nums[i+1:][::-1]           #nums[i]后面的升序排列才最小，逆序下




# @lc code=end
nums = [1,2,3]
# nums = [3,2,1]
# nums = [1,1,5]
nums = [7,8,4,3,1]  #[8,7,4,3,1]  ->  [8,1,3,4,7]  #先交换右侧的大-小位置，在把右侧排序 
# nums = [1,2]
o = Solution()
print(o.nextPermutation(nums))
print(nums)