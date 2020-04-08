#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#
# https://leetcode-cn.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (43.94%)
# Likes:    269
# Dislikes: 0
# Total Accepted:    21.9K
# Total Submissions: 49.3K
# Testcase Example:  '[1,1,1]\n2'
#
# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
# 
# 示例 1 :
# 
# 
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
# 
# 
# 说明 :
# 
# 
# 数组的长度为 [1, 20,000]。
# 数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    #哈希表
    #累计和缓存起来，每次查询(累计和-k)是否存在，存在说明符合
    def subarraySum(self, nums: List[int], k: int) -> int:
        cache = {}
        cache[0] = 1                                #key累加和， value是出现的次数，默认1
        sum, count = 0, 0
        for i in range(len(nums)):
            sum += nums[i]                          #累加和
            if sum-k in cache:                      #累加和-k 已存在，那当前也是符合的
                count += cache[sum-k]               
            cache[sum] = cache.get(sum, 0) + 1      #出现的次数+1
        return count


# @lc code=end

nums = [1,1,1]
k = 2
nums = [-1,-1,1]
k = 0
o = Solution()
print(o.subarraySum(nums, k))