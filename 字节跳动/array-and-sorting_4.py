#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/bytedance/243/array-and-sorting/1035/
# 最长连续递增序列
# 给定一个未经排序的整数数组，找到最长且连续的的递增序列。

# 示例 1:
# 输入: [1,3,5,4,7]
# 输出: 3
# 解释: 最长连续递增序列是 [1,3,5], 长度为3。
# 尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。 

# 示例 2:
# 输入: [2,2,2,2,2]
# 输出: 1
# 解释: 最长连续递增序列是 [2], 长度为1。
# 注意：数组长度不会超过10000。

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划
        # 用Dp[i]来保存从0 - i的数组的最长递增子序列的长度。
        # 如上数组Dp[0] = 1, Dp[1] = 1, Dp[2] = 1, Dp[3] = 2, Dp[4] = 2。。。
        # 计算Dp[i]的值可以对Dp[i]之前数值进行遍历，如果nums[i] > nums[j], 则Dp[i] = max(Dp[i], Dp[j] + 1)。
        # 复杂度为O(n)
        length = len(nums)
        if length <= 1:
            return length
        dp = [1] * length
        for i in range(1,length):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
        return max(dp)

    def findLengthOfLCIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        l = len(nums)
        res = 0
        tmp = nums[0] - 1
        count = 0
        for x in range(l):
            if nums[x] > tmp:
                count += 1
                if count > res:
                    res = count
            else:
                count = 1
            tmp = nums[x]
        return res


nums = [1,3,5,4,7]
s = Solution()
n = s.findLengthOfLCIS(nums)
print(n)











