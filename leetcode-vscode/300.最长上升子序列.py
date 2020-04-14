#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#
# https://leetcode-cn.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (44.15%)
# Likes:    629
# Dislikes: 0
# Total Accepted:    85.6K
# Total Submissions: 193.9K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
# 
# 示例:
# 
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4 
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
# 
# 说明:
# 
# 
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n^2) 。
# 
# 
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
# 
#
from typing import List
# @lc code=start
class Solution:
    # 二分 O(n*log(n))
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:return 0
        re = [nums[0]]                          #结果保存队列
        for i in range(1, len(nums)):           #每个元素插入re，如果遇到的比re都大，会插入队尾，如果在中间，就替换第N大的元素
            l, r = 0, len(re)-1
            while l<=r:
                mid = (l + r) // 2
                if nums[i] > re[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            if l>=len(re):
                re.append(nums[i])
            else:
                re[l] = nums[i]                 #这里会直接替换原位置的值
        return len(re)
    #和bisect_left的区别是，bisect_left是在idx前插入，这题是替换

    #动态规划 O(n^2)
    def lengthOfLIS2(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0:return 0 
        dp = [1] * n 
        maxLen = 0
        for i in range(n):
            for  j in range(i):
                if nums[j] < nums[i]:
                  dp[i] = max(dp[i], dp[j]+1)
            maxLen = max(maxLen, dp[i])
        return maxLen


# @lc code=end

nums = [10,9,2,5,3,7,101,18]
o = Solution()
print(o.lengthOfLIS(nums))