#!/usr/bin/python
#coding:utf-8

# // 面试题41：数据流中的中位数
# // 题目：如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么
# // 中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，
# // 那么中位数就是所有数值排序之后中间两个数的平均值。
import heapq
class Solution:
    def test(self, nums, k):
        max_heap = []
        min_heap = []
        while True:
            x = input()
            if x == '':
                if len(min_heap) == 0 and len(max_heap) == 0:
                    return

                mid = None

                if (len(min_heap) + len(max_heap)) & 1 == 0:
                    mid = (heapq.heappop(min_heap) - heapq.heappop(max_heap)) / 2
                else:
                    mid = heapq.heappop(max_heap) * -1

                print("中位数：%d" % mid)
                return

            x = int(x)
            if (len(min_heap) + len(max_heap)) & 1 == 0:
                if len(min_heap) > 0:
                    heapq.heappush(min_heap, x)
                    x = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -1 * x)
            else:
                if len(max_heap) > 0:
                    heapq.heappush(max_heap, -1 * x)
                    x = -1 * heapq.heappop(max_heap)
                heapq.heappush(min_heap, x)



obj = Solution()
