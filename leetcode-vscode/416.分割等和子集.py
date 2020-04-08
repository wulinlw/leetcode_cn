#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
# https://leetcode-cn.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (45.42%)
# Likes:    236
# Dislikes: 0
# Total Accepted:    24.4K
# Total Submissions: 52.6K
# Testcase Example:  '[1,5,11,5]'
#
# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
# 
# 注意:
# 
# 
# 每个数组中的元素不会超过 100
# 数组的大小不会超过 200
# 
# 
# 示例 1:
# 
# 输入: [1, 5, 11, 5]
# 
# 输出: true
# 
# 解释: 数组可以分割成 [1, 5, 5] 和 [11].
# 
# 
# 
# 
# 示例 2:
# 
# 输入: [1, 2, 3, 5]
# 
# 输出: false
# 
# 解释: 数组不能分割成两个元素和相等的子集.
# 
# 
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # 动态规划
    # 0-1背包问题  [518] 零钱兑换 II
    # 只是问题变成装一半背包
    # dp[i][j] 前i个物品，背包容量是j时，能不能装满，True ,False
    # dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
    # dp[i-1][j]            第i个不装，和上一个（i-1）一样
    # dp[i-1][j-nums[i-1]]  第i个装入，在上一个基础上，容量减少nums[i-1]是上个物品的重量
    def canPartition(self, nums: List[int]) -> bool:
        sum = 0 
        for i in nums:                                              #计算背包容量
            sum += i
        if sum%2 != 0:return False                                  #如果容量是奇数，就不能完整的装一半
        n = len(nums)
        sum = sum//2                                                #题目是分为两半，即背包装一半
        dp = [[False for i in range(sum+1)] for i in range(n+1)]    #容量，物品
        for i in range(n+1):                                        #容量为0时，默认装满
            dp[i][0] = True
        for i in range(n+1):                                        
            for j in range(1, sum+1):
                if j - nums[i-1] < 0:                               #容量比物品小，继承上一个结果
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]   #装入 or 不装入

            print(dp[i],dp[i-1][j-nums[i-1]])
        return dp[-1][-1] 

    # 状态压缩,一维数组
    # https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/0-1-bei-bao-wen-ti-bian-ti-zhi-zi-ji-fen-ge-by-lab/
    def canPartition2(self, nums: List[int]) -> bool:
        sum = 0 
        for i in nums:                                              #计算背包容量
            sum += i
        if sum%2 != 0:return False                                  #如果容量是奇数，就不能完整的装一半
        n = len(nums)
        sum = sum//2                                                #题目是分为两半，即背包装一半
        dp = [False for i in range(sum+1)]                          #容量
        dp[0] = True
        for i in range(n+1):
            for j in range(sum, -1, -1):                            #这里需要倒着，避免后面的dp[j-nums[i]]变更影响结果
                if j-nums[i-1] > 0:
                    dp[j] = dp[j] or dp[j-nums[i]]
        return dp[-1]



        
# @lc code=end
nums = [1, 5, 11, 5]
# nums = [1, 2, 3, 5]
o = Solution()
print(o.canPartition(nums))