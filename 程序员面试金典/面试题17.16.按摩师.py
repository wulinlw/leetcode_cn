#!/usr/bin/python
#coding:utf-8


# 面试题 17.16. 按摩师
# 一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。

# 注意：本题相对原题稍作改动
# 示例 1：
# 输入： [1,2,3,1]
# 输出： 4
# 解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。
# 示例 2：
# 输入： [2,7,9,3,1]
# 输出： 12
# 解释： 选择 1 号预约、 3 号预约和 5 号预约，总时长 = 2 + 9 + 1 = 12。
# 示例 3：
# 输入： [2,1,4,5,3,1,1,3]
# 输出： 12
# 解释： 选择 1 号预约、 3 号预约、 5 号预约和 8 号预约，总时长 = 2 + 4 + 3 + 3 = 12。
# https://leetcode-cn.com/problems/the-masseuse-lcci/

from typing import List
class Solution:
    #打家劫舍 同类型题
    # dp[i] = max(dp[i-2]+nums[i], dp[i-1])  今天接（前天+今天），今天不接（和昨天一样）
    def massage2(self, nums: List[int]) -> int:
        if not nums:return 0 
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            # dp[i-2]+nums[i]       前2个+当前，空出前一个了
            # dp[i-1]               取前一个，当前不取
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]

    # 这个思路需要注意
    def massage(self, nums: List[int]) -> int:
        if not nums:return 0 
        dp = [[0,0] for i in range(len(nums))]
        dp[0][1] = nums[0]          #0代表不选，1代表选
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i-1][1], dp[i-1][0])          #当前不选，取前一个最大值
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]+nums[i])  #当前选择，当前+昨天没选的（dp[i-1][0]+nums[i]）
        print(dp)
        return max(dp[-1][0], dp[-1][1])

nums = [1,2,3,1]
nums = [2,1,4,5,3,1,1,3]
o = Solution()
print(o.massage(nums))
