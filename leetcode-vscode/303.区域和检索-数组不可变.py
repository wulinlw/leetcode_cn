#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#
# https://leetcode-cn.com/problems/range-sum-query-immutable/description/
#
# algorithms
# Easy (59.99%)
# Likes:    142
# Dislikes: 0
# Total Accepted:    31.8K
# Total Submissions: 52.5K
# Testcase Example:  '["NumArray","sumRange","sumRange","sumRange"]\n' +
# '[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'
#
# 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
# 
# 示例：
# 
# 给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()
# 
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# 
# 说明:
# 
# 
# 你可以假设数组不可变。
# 会多次调用 sumRange 方法。
# 
# 
#
from typing import List
# @lc code=start
class NumArray:

	def __init__(self, nums: List[int]):
		self.presum = [0]* (len(nums)+1)
		for i in range(1, len(nums)+1):
			self.presum[i] = self.presum[i-1]+nums[i-1]	#计算前缀和，注意向后移了一位
		# print(self.presum)
		# [0, -2, -2, 1, -4, -2, -3] 					#第一位空着，第一位的和在第二位

	def sumRange(self, i: int, j: int) -> int:		
		return self.presum[j+1] - self.presum[i]		#2+3=5  5-2=3


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end

nums = [-2, 0, 3, -5, 2, -1]
o = NumArray(nums)
print(o.sumRange(0,2))
print(o.sumRange(2,5))
print(o.sumRange(0,5))