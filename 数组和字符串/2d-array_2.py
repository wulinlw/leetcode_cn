#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/featured/card/array-and-string/199/introduction-to-2d-array/774/
# 对角线遍历
# 给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。
# 示例:
# 输入:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]

# 输出:  [1,2,4,7,5,3,6,8,9]
# 解释:

# 说明:
# 给定矩阵中的元素总数不会超过 100000 。
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 0 and 0 答案是 0，此处避免 matrix 为 [] 时导致报错
        # 按照从右上角到左下角的顺序遍历 matrix 的所有对角线并放入列表 temp
        # 如果 对角线元素个数 是奇数数则应该把 temp 反转
        # 把 temp 加入结果 r
        m, n, r = len(matrix), len(matrix) and len(matrix[0]), []
        for l in range(m + n - 1):
            print(l,max(0, l+1 - n), min(l+1, m))
            # 写法就是第二种解法的简化
            temp = [matrix[i][l - i] for i in range(max(0, l+1 - n), min(l+1, m))]
            print(temp)
            r += temp if l % 2 else temp[::-1]
        return r

    # https://leetcode-cn.com/problems/diagonal-traverse/solution/dui-jiao-xian-bian-li-gui-lu-xiang-xi-jie-xi-by-ji/
    def findDiagonalOrder2(self, matrix):
        if len(matrix) == 0:
            return []
        M, N, result = len(matrix), len(matrix[0]), []
        # 所以对角线的总数为　行数 + 列数　- 1
        for curve_line in range(M + N - 1):
            # 在对角线小于等于列数的时候，观察到始终是从第 ０ 行开始。
            # 超过了列数后，每超过一条，起始行数也要加一。
            # 超过后的起始即 curve_line + 1 - Ｎ。
            # row_begin,row_end理解为对角线起始和结尾
            row_begin = 0 if curve_line + 1 <= N else curve_line + 1 - N
            row_end = M - 1 if curve_line + 1 >= M else curve_line
            # print(curve_line,row_begin,row_end + 1)
            if curve_line % 2 == 1:
                for i in range(row_begin,row_end + 1):
                    result.append(matrix[i][curve_line - i])
            else:#则当对角线的序号为偶数时，对角线是向右上的。
                for i in range(row_end,row_begin - 1,-1):
                    result.append(matrix[i][curve_line - i])
        return result




matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
s = Solution()
n = s.findDiagonalOrder2(matrix)
print(n)       