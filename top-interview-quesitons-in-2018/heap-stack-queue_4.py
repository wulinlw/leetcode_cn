#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/featured/card/top-interview-quesitons-in-2018/266/heap-stack-queue/1156/
# 有序矩阵中第K小的元素
# 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
# 请注意，它是排序后的第k小元素，而不是第k个元素。

# 示例:
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,

# 返回 13。
# 说明: 
# 你可以假设 k 的值永远是有效的, 1 ≤ k ≤ n2 。

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import bisect
        # 对于寻找分位数这种还是要用二分法。即设置l，r两个变量采用二分法的办法，每一次数一数有几个数小于中心值，然后循环直到l=r，此时l就是矩阵中存在的第k小数值。
        l = matrix[0][0]
        r = matrix[-1][-1]
        while(l<r):
            m = l+(r-l)//2
            total=sum(bisect.bisect_right(row, m) for row in matrix)
            if total>=k:
                r = m
            else:
                l = m+1
        return l    


matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
s = Solution()
res = s.kthSmallest(matrix, k)
print(res)

