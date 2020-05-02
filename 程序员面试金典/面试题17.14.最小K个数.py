# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题17.14.最小K个数
# 
# https://leetcode-cn.com/problems/smallest-k-lcci/
# 
# 设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。
# 示例：
# 
# 输入： arr = [1,3,5,7,2,4,6,8], k = 4
# 输出： [1,2,3,4]
# 
# 
# 提示：
# 
# 
# 	0 <= len(arr) <= 100000
# 	0 <= k <= min(100000, len(arr))
# 
# 
# 
# Medium 55.0%
# Testcase Example: [1,2,3]
# 0
# 
# 提示:
# 实际上有几种方法。动脑筋想一想。从简单的方法开始也没问题。
# 考虑以某种方式重新组织数据或者使用其他数据结构。
# 你能把这些数字排序吗?
# 使用堆或某种树怎么样?
# 如果你选了一个任意的元素，那么需要多长时间才能算出它的元素的排序（比它大或比它小的元素的个数）?
# 如果你选择一个任意的元素，平均来说，就会得到一个在第50百分位数附近的元素（一半的元素比它大，一半的元素比它小）。如果反复这样做呢?
# 回想一下前面的提示，特别是与快速排序相关的提示。
# 如果当你选择一个元素时，你交换周围的元素（就像在快速排序中所做的那样），使它所有下方的元素都位于上方的元素之前，那会怎么样？如果你重复做这个，能找到最小的一百万个数吗？
# 
# 
from typing import List
class Solution:
    def smallestK(self, nums: List[int], k: int) -> List[int]:
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
        return nums[:k]

    def partition(self, nums, start, end):
        i = start-1
        pivot = nums[end]
        for j in range(start, end):
            if nums[j] < pivot:
                i += 1
                nums[i],nums[j] = nums[j],nums[i]
        nums[i+1],nums[end] = nums[end],nums[i+1]
        # print(nums, i+1)
        return i+1

arr = [1,3,5,7,2,4,6,8]
k = 4
o = Solution()
print(o.smallestK(arr, k))