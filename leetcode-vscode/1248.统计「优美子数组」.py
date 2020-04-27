#
# @lc app=leetcode.cn id=1248 lang=python3
#
# [1248] 统计「优美子数组」
#
# https://leetcode-cn.com/problems/count-number-of-nice-subarrays/description/
#
# algorithms
# Medium (47.01%)
# Likes:    47
# Dislikes: 0
# Total Accepted:    6.7K
# Total Submissions: 13K
# Testcase Example:  '[1,1,2,1,1]\n3'
#
# 给你一个整数数组 nums 和一个整数 k。
# 
# 如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
# 
# 请返回这个数组中「优美子数组」的数目。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,1,2,1,1], k = 3
# 输出：2
# 解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
# 
# 
# 示例 2：
# 
# 输入：nums = [2,4,6], k = 1
# 输出：0
# 解释：数列中不包含任何奇数，所以不存在优美子数组。
# 
# 
# 示例 3：
# 
# 输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# 输出：16
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 50000
# 1 <= nums[i] <= 10^5
# 1 <= k <= nums.length
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # https://leetcode-cn.com/problems/count-number-of-nice-subarrays/solution/tong-ji-you-mei-zi-shu-zu-by-leetcode-solution/
    def numberOfSubarrays2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        odd = [-1]
        re = 0
        for i in range(n):
            if nums[i] & 1 == 1:
                odd.append(i)
        odd.append(n)
        for i in range(1, len(odd)-k):
            re += (odd[i] - odd[i-1]) * (odd[i+k] - odd[i+k-1])
        return re
    
    # 前缀和 & hash
    # 和leetcode 560一样
    # https://leetcode-cn.com/problems/count-number-of-nice-subarrays/solution/1248-tong-ji-you-mei-zi-shu-zu-by-bu-jue-jian-yi-b/
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):      #奇数记为1，偶数记为0，题目变为 “找和为K的子数组”
            if nums[i]&1 == 1:
                nums[i] = 1
            else:
                nums[i] = 0
        re = 0
        sum = 0
        dic = {}
        dic[0] = 1                      #当出现sum-k==0时，res需要+1
        for i in range(len(nums)):
            sum += nums[i]
            if sum-k in dic: 
                re += dic[sum-k]
            dic[sum] = dic.get(sum, 0) + 1
        return re




# @lc code=end

nums = [1,1,2,1,1]
k = 3
nums = [2,4,6]
k = 1
nums = [2,2,2,1,2,2,1,2,2,2]
#             3   5 6
k = 2
o = Solution()
print(o.numberOfSubarrays(nums, k))