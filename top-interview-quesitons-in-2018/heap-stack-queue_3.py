#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/featured/card/top-interview-quesitons-in-2018/266/heap-stack-queue/1155/
# 数据流的中位数
# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

# 例如，
# [2,3,4] 的中位数是 3
# [2,3] 的中位数是 (2 + 3) / 2 = 2.5
# 设计一个支持以下两种操作的数据结构：
# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。
# 示例：

# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2
# 进阶:

# 如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
# 如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？

# https://blog.csdn.net/weixin_41303016/article/details/88569695
import bisect
class MedianFinder:
    def __init__(self):
        self.nums = []

    def addNum(self, num):
        bisect.insort(self.nums, num)

    def findMedian(self):
        nums = self.nums
        if len(nums) % 2 == 0:
            return (nums[len(nums)/2] + nums[len(nums)/2-1]) / 2.0
        else:
            return nums[len(nums)/2]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()



