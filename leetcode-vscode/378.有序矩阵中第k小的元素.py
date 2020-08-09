#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第K小的元素
#
# https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
#
# algorithms
# Medium (59.44%)
# Likes:    286
# Dislikes: 0
# Total Accepted:    28.8K
# Total Submissions: 47.1K
# Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
#
# 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
# 请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。
# 
# 
# 
# 示例：
# 
# matrix = [
# ⁠  [ 1,  5,  9],
# ⁠  [10, 11, 13],
# ⁠  [12, 13, 15]
# ],
# k = 8,
# 
# 返回 13。
# 
# 
# 
# 
# 提示：
# 你可以假设 k 的值永远是有效的，1 ≤ k ≤ n^2 。
# 
#
from typing import List
import heapq
# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        pq = [(matrix[i][0], i, 0) for i in range(n)]           #记录第一列value，x轴向右递增,
        print(pq)
        heapq.heapify(pq)

        ret = 0
        for i in range(k - 1):                                  #堆中弹出k-1次后，堆顶就是第k个
            num, x, y = heapq.heappop(pq)                       #最小的被弹出，然后放他右侧的值
            if y != n - 1:                                      #不是每行最后一个就继续放入堆
                heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))#横着放，被弹出的右侧的值
        
        return heapq.heappop(pq)[0]

    # https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/solution/you-xu-ju-zhen-zhong-di-kxiao-de-yuan-su-by-leetco/
    def kthSmallest2(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        # 如果数量不多于 kk，那么说明最终答案 xx 不小于 midmid；
        # 如果数量少于 kk，那么说明最终答案 xx 大于 midmid。
        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        
        return left




# @lc code=end
matrix = [
    [ 1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 8
o = Solution()
print(o.kthSmallest(matrix, k))