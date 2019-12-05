#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/51/dynamic-programming/107/
# Longest Increasing Subsequence
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。

# 示例:
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4 
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
# 说明:

# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n2) 。
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-2/
        # dp[i]表示当前位置的最长子序列长度，
        # 遍历num[i]之前的数并更新dp[i]的值
        # 此算法的复杂度为n2
        dp=[1]*len(nums)
        if len(nums)==0:
            return 0
        for i in range(1,len(nums)):
            for j in range(0,i):
                if(nums[i]>nums[j]):
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)

    # 此算法的复杂度为O(n log n)
    # tails存排序，规则如下
    # 当前遍历值大于最后一位，则放在tails后面
    # 小于最后一位，就替换到他应该插入的位置
    # tails的有效长度就是结果

    #看视频
    # https://www.bilibili.com/video/av38184838
    def lengthOfLIS2(self, nums):
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:            # while就是在找当前值需要插入到哪里，
                m = (i + j) // 2
                if tails[m] < num: 
                    i = m + 1       # 往后插入
                else: 
                    j = m           # 往前插入
            tails[i] = num
            # print(tails,i,j,res)
            if j == res:            # 插入到最后，说明连续增长的数+1
                res += 1
        return res

# 作者：jyd
# 链接：https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

nums = [10,9,2,5,3,7,101,18]
s = Solution()
r = s.lengthOfLIS2(nums)
print(r)




