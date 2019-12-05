#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/featured/card/array-and-string/199/introduction-to-2d-array/775/
# 螺旋矩阵
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

# 示例 1:

# 输入:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
# 示例 2:

# 输入:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 取一行，逆时针反转90度，刚好竖着的最后一列变成第一行
        # print(list(list(zip(*matrix)))[::-1])
        # print(list(map(list, zip(*matrix)))[::-1])
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(map(list, zip(*matrix)))[::-1]
            # matrix = list(list(zip(*matrix)))[::-1]#和上面一样
        return res

    # 假设数组有 R 行 C 列，seen[r][c] seen[r][c] 表示第 r 行第 c 列的单元格之前已经被访问过了。
    # 当前所在位为 (r, c)(r, c)，前进方向是 di。我们希望访问所有 R x C 个单元格。
    # 当我们遍历整个矩阵，下一步候选移动位置是 (cr, cc)(cr, cc)。
    # 如果这个候选位置在矩阵范围内并且没有被访问过，那么它将会变成下一步移动的位置；
    # 否则，我们将前进方向顺时针旋转之后再计算下一步的移动位置。
    def spiralOrder2(self, matrix):
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/spiral-matrix/solution/luo-xuan-ju-zhen-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
s = Solution()
n = s.spiralOrder(matrix)
print(n)       