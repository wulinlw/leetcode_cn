#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/orignial/card/all-about-lockup-table/239/learn-to-use-keys/1001/
# 回旋镖的数量
# 给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。
# 找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。

# 示例:
# 输入:
# [[0,0],[1,0],[2,0]]

# 输出:
# 2
# 解释:
# 两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
import collections
class Solution(object):
    # 外层遍历每个点 i，内层遍历并计算其他点 j 到 i 的距离并通过 Map 保存相等距离的频次
    # 计算距离公式不用开根号
    # 计算排列组合公式 n * (n - 1)
    def dis(self, p1, p2):
        return (p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1])
    
    def numberOfBoomerangs(self, points):
        res = 0
        for i in points:
            freqMap = {}
            for j in points:
                if j != i:
                    d = self.dis(i, j)
                    freqMap[d] = freqMap[d] + 1 if d in freqMap else 1
            
            for v in freqMap.values():
                res += v * (v - 1)
        
        return res

points = [[0,0],[1,0],[2,0]]
ss = Solution()
re = ss.numberOfBoomerangs(points)
print(re)

