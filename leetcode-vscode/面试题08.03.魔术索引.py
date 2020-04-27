# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题08.03.魔术索引
# 
# https://leetcode-cn.com/problems/magic-index-lcci/
# 
# 魔术索引。 在数组A[0...n-1]中，有所谓的魔术索引，满足条件A[i] = i。给定一个有序整数数组，编写一种方法找出魔术索引，若有的话，在数组A中找出一个魔术索引，如果没有，则返回-1。若有多个魔术索引，返回索引值最小的一个。
# 示例1:
# 
#  输入：nums = [0, 2, 3, 4, 5]
#  输出：0
#  说明: 0下标的元素为0
# 
# 
# 示例2:
# 
#  输入：nums = [1, 1, 1]
#  输出：1
# 
# 
# 提示:
# 
# 
# 	nums长度在[1, 1000000]之间
# 
# 
# 
# Easy 65.5%
# Testcase Example: [0, 2, 3, 4, 5]
# 
# 提示:
# 先试试蛮力算法。
# 蛮力算法的运行时间可能为O(N)。如果试图击败那个运行时间，你认为会得到什么运行时间。什么样的算法具有该运行时间？
# 你能以O(log N)的时间复杂度来解决这个问题吗？
# 二分查找有O(log n)的运行时间。你能在这个问题中应用二分查找吗？
# 给定一个特定的索引和值，你能确定魔术索引是在它之前还是之后吗？
# 
# 
from typing import List
class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        if not nums:return -1
        n = len(nums)
        i = 0
        while i<n:
            if nums[i] == i:
                return i
            if nums[i] > i:
                i = nums[i]
            else:
                i += 1
        return -1


nums = [0, 2, 3, 4, 5]
nums = [1, 1, 1]
nums = [0, 0, 2]
nums = [1,2,6,7,8,9,10]
o = Solution()
print(o.findMagicIndex(nums))