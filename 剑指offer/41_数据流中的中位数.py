#!/usr/bin/python
#coding:utf-8

# // 面试题41：数据流中的中位数
# // 题目：如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么
# // 中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，
# // 那么中位数就是所有数值排序之后中间两个数的平均值。
import heapq
class Solution:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # 初始化大顶堆和小顶堆
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):# 先加到大顶堆，再把大堆顶元素加到小顶堆
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))
        else:  # 先加到小顶堆，再把小堆顶元素加到大顶堆
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return self.min_heap[0]


    # 作者：z1m
    # 链接：https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/solution/you-xian-dui-lie-by-z1m/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
#数据理解
# 1           max -1
#             min

# 1,2         max -1
#             min 2

# 1,2,3       max -2,-1
#             min 3

# 1,2,3,4     max -2,-1
#             min 3,4

# 1,2,3,4,5   max -3,-2,-1
#             min 4,5

# 1,2,3,4,5,6 max -3,-1,-2
#             min 4,5,6



1,2,3,4,5,6     

obj = Solution()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
obj.addNum(4)
obj.addNum(5)
print(obj.findMedian())
