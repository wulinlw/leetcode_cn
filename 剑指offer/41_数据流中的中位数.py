#!/usr/bin/python
#coding:utf-8

# // 面试题41：数据流中的中位数
# // 题目：如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么
# // 中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，
# // 那么中位数就是所有数值排序之后中间两个数的平均值。
import heapq
class Solution:
    # 创建一个最大堆，一个最小堆
    # 总数是偶数时，新数据写入最大堆，都是负数
    # 总数是奇数时，新数据写入最小堆，都是正数
    # 为保证2个堆中数据一样多，写入前需做处理
    # 2个堆的和为偶数时，若对小堆有值，线放入最小堆，弹出堆顶（最小）写入最大堆
    # 2个堆的和为奇数时，若对大堆有值，线放入最大堆，弹出堆顶（最小）写入最大堆， 最大堆都是负数，所以堆顶转成正数就是最大的

    # 返回结果是
    # 总数是偶数时，中位数 =（最小堆的堆顶 + 最大堆中的堆顶)/2
    # 总数是奇数时，中位数 = 最大堆的堆顶/2

    # python3 41_数据流中的中位数.py  测试可以看下效果，协助理解2个堆桌面存储数据
    def test(self):
        max_heap = []
        min_heap = []
        while True:
            x = input("input num ")
            if x == '':
                if len(min_heap) == 0 and len(max_heap) == 0:
                    return

                mid = None

                print(max_heap)
                print(min_heap)
                if (len(min_heap) + len(max_heap)) & 1 == 0:
                    mid = (heapq.heappop(min_heap) - heapq.heappop(max_heap)) / 2
                else:
                    mid = heapq.heappop(max_heap) * -1

                
                print("中位数：%d" % mid)
                return

            x = int(x)
            if (len(min_heap) + len(max_heap)) & 1 == 0:    #和为偶数
                if len(min_heap) > 0:
                    heapq.heappush(min_heap, x)             #插入最小堆
                    x = heapq.heappop(min_heap)             #并从最小堆中弹出最顶值（最小）
                heapq.heappush(max_heap, -1 * x)            #写入最大堆
            else:
                if len(max_heap) > 0:
                    heapq.heappush(max_heap, -1 * x)        #写入最大堆
                    x = -1 * heapq.heappop(max_heap)        #弹出最大堆中的最顶值（最小）
                heapq.heappush(min_heap, x)                 #写入最小堆

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
obj.test()
