# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题16.13.平分正方形
# 
# https://leetcode-cn.com/problems/bisect-squares-lcci/
# 
# 给定两个正方形及一个二维平面。请找出将这两个正方形分割成两半的一条直线。假设正方形顶边和底边与 x 轴平行。
# 每个正方形的数据square包含3个数值，正方形的左下顶点坐标[X,Y] = [square[0],square[1]]，以及正方形的边长square[2]。所求直线穿过两个正方形会形成4个交点，请返回4个交点形成线段的两端点坐标（两个端点即为4个交点中距离最远的2个点，这2个点所连成的线段一定会穿过另外2个交点）。2个端点坐标[X1,Y1]和[X2,Y2]的返回格式为{X1,Y1,X2,Y2}，要求若X1 != X2，需保证X1 < X2，否则需保证Y1 <= Y2。
# 
# 若同时有多条直线满足要求，则选择斜率最大的一条计算并返回（与Y轴平行的直线视为斜率无穷大）。
# 
# 示例：
# 
# 输入：
# square1 = {-1, -1, 2}
# square2 = {0, -1, 2}
# 输出： {-1,0,2,0}
# 解释： 直线 y = 0 能将两个正方形同时分为等面积的两部分，返回的两线段端点为[-1,0]和[2,0]
# 
# 
# 提示：
# 
# 
# 	square.length == 3
# 	square[2] > 0
# 
# 
# 
# Medium 43.1%
# Testcase Example: [-1,1,3]
# [0,0,5]
# 
# 提示:
# 画一个正方形和一些把它切成两半的线。这些线位于哪里？
# 任何把正方形切成两半的直线都穿过正方形的中心。那你怎么才能找到一条把两个正方形切成两半的线呢？
# 要将两个正方形切成两半，这条线必须穿过这两个正方形的中心。
# 给定一条直线（斜率和y轴截距），你能找到它与另一条直线的交点吗?
# 
# 
from typing import List
class Solution:
    def cutSquares(self, square1: List[int], square2: List[int]) -> List[float]:
        """
        连接两个中心
        利用 y = k * x + b
        k 有四种情况，大于小于 1 或 大于小于 -1，其实可以
        合并为两种情况：abs(k) < 1 和 abs(k) >= 1
        把这两种情况画个图看一下交点在哪即可
        """
        x_1, y_1 = square1[0] + square1[2] / 2, square1[1] + square1[2] / 2 # 两个中点坐标
        x_2, y_2 = square2[0] + square2[2] / 2, square2[1] + square2[2] / 2

        if x_1 == x_2:
            return [x_1, min(square1[1], square2[1]), x_2, max(square1[1] + square1[2], square2[1] + square2[2])]

        k = (y_1 - y_2) / (x_1 - x_2)
        b = y_1 - k * x_1

        if abs(k) <= 1:
            x1 = min(square2[0], square1[0])
            x2 = max(square1[0] + square1[2], square2[0] + square2[2])

            y1 = k * x1 + b
            y2 = k * x2 + b

        else:
            y1 = min(square1[1], square2[1])
            y2 = max(square1[1] + square1[2], square2[1] + square2[2])

            x1 = (y1 - b) / k
            x2 = (y2 - b) / k
        # 按照题目要求处理输出
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        if x1 == x2 and y1 > y2:
            y1, y2 = y2, y1
        return [x1, y1, x2, y2]


o = Solution()
print(o.cutSquares(square1, square2))