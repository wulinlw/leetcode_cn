#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (62.63%)
# Likes:    551
# Dislikes: 0
# Total Accepted:    144.5K
# Total Submissions: 226.4K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 
# 示例 1:
# 
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 
# 
# 示例 2:
# 
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
# 
# 说明: 
# 
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
# 
#
from typing import List
import heapq
# @lc code=start
class Solution:
    # 和剑指offer——40题：最小的k个数 一样
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        if k>len(nums) or k<=0:return []
        start = 0
        end = len(nums)-1
        index = self.partition(nums, start, end)
        # print(index, nums)
        while index != k-1:
            if index > k-1:                 #索引需要的值，往左缩小范围
                end = index-1
            if index < k-1:
                start = index+1             #不够K个数，继续往右扩大范围，由于前面的都排好了，这里index+1设为新的开始排序点
            index = self.partition(nums, start, end)
        return nums[k-1]

    def partition(self, nums, start, end):
        i = start-1
        pivot = nums[end]
        for j in range(start, end):
            if nums[j] > pivot:             #这里变成大于，排序是从大到小
                i += 1
                nums[i],nums[j] = nums[j],nums[i]
        nums[i+1],nums[end] = nums[end],nums[i+1]
        # print(nums, i+1)
        return i+1
    
    #堆排序
    def findKthLargest(self, nums, k):
        re = []
        for i in nums:
            heapq.heappush(re, i) 
            if len(re)>k:
                heapq.heappop(re)
        # print(re)
        return re[0]
# @lc code=end
nums = [3,2,1,5,6,4]
k = 2
# nums = [3,2,3,1,2,4,5,5,6]
# k = 4
o = Solution()
print(o.findKthLargest2(nums, k))
