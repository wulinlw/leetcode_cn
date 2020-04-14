#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] 递增的三元子序列
#
# https://leetcode-cn.com/problems/increasing-triplet-subsequence/description/
#
# algorithms
# Medium (36.93%)
# Likes:    131
# Dislikes: 0
# Total Accepted:    16.6K
# Total Submissions: 43.8K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。
# 
# 数学表达式如下:
# 
# 如果存在这样的 i, j, k,  且满足 0 ≤ i < j < k ≤ n-1，
# 使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
# 
# 说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。
# 
# 示例 1:
# 
# 输入: [1,2,3,4,5]
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: [5,4,3,2,1]
# 输出: false
# 
#
from typing import List
# @lc code=start
class Solution:
    # [300] 最长上升子序列
    # https://leetcode-cn.com/problems/increasing-triplet-subsequence/solution/ji-yu-cde-xian-xing-fu-za-du-suan-fa-de-yu-chun-fe/
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3:return False
        small = mid = float('inf')      #2个变量表示最小的2个数
        for num in nums:
            if num <= small:            #小于倒数第一
                small = num
            elif num <= mid:            #小于倒数第二
                mid = num
            else:
                return True
        return False


# @lc code=end

nums = [1,2,3,4,5]
nums = [5,4,3,2,1]
o = Solution()
print(o.increasingTriplet(nums))