#!/usr/bin/python
#coding:utf-8

# 面试题 17.23. 最大黑方阵
# 给定一个方阵，其中每个单元(像素)非黑即白。设计一个算法，找出 4 条边皆为黑色像素的最大子方阵。
# 返回一个数组 [r, c, size] ，其中 r, c 分别代表子方阵左上角的行号和列号，size 是子方阵的边长。若有多个满足条件的子方阵，返回 r 最小的，若 r 相同，返回 c 最小的子方阵。若无满足条件的子方阵，返回空数组。
# 示例 1:
# 输入:
# [
#    [1,0,1],
#    [0,0,1],
#    [0,0,1]
# ]
# 输出: [1,0,2]
# 解释: 输入中 0 代表黑色，1 代表白色，标粗的元素即为满足条件的最大子方阵
# 示例 2:
# 输入:
# [
#    [0,1,1],
#    [1,0,1],
#    [1,1,0]
# ]
# 输出: [0,0,1]
# 提示：
# matrix.length == matrix[0].length <= 200
# https://leetcode-cn.com/problems/max-black-square-lcci/

from typing import List
class Solution:
    # 动态规划
    # 获取每个节点的最大黑边行和列
    # mxrow[r,c]为当前点往右的最大黑边行
    # mxcol[r,c]为当前点往下的最大黑边列
    # 从右下角开始遍历得到它们, 这样能利用之前得到的结果
    # 计算最大方阵
    # 从左上角开始遍历, 针对黑节点, 找其黑边行和列的较小值, 作为size的最大值
    # 然后递减size遍历, 如果找到一个符合条件的(右顶点和下顶点的边长度>=cursize)就break
    # 注意一个优化操作是循环遍历到当前res size+1为止, 因为如果等于当前res size的话一定不满足要求了
    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        from collections import defaultdict
        if not matrix:
            return []
        mxrow = defaultdict(int)
        mxcol = defaultdict(int)
        rows, cols = len(matrix), len(matrix[0])
        res = []
        for r in range(rows)[::-1]:
            for c in range(cols)[::-1]:
                if matrix[r][c] == 0:                       #右下角倒推黑边长度
                    mxrow[r, c] = 1 + mxrow[r, c + 1]
                    mxcol[r, c] = 1 + mxcol[r + 1, c]
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:                       #从左上角开始看，如果是黑点
                    mxsize = min(mxrow[r, c], mxcol[r, c])  #找最小黑边
                    cursize = 0 if not res else res[2]
                    for size in range(mxsize, cursize, -1):
                        if mxcol[r, c + size - 1] >= size and mxrow[r + size - 1, c] >= size:
                            res = [r, c, size]
                            break
        return res

matrix = [
   [1,0,1],
   [0,0,1],
   [0,0,1]
]
o = Solution()
print(o.findSquare(matrix))
# print(o.numberOf2sInRange2(1125))






