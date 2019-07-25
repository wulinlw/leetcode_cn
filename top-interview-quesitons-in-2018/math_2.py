#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/featured/card/top-interview-quesitons-in-2018/274/math/1187/
# 直线上最多的点数
# 给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。
# 示例 1:
# 输入: [[1,1],[2,2],[3,3]]
# 输出: 3
# 解释:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4
# 示例 2:
# 输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# 输出: 4
# 解释:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        import numpy
        l = len(points)
        m = 0
        for i in range(l):
            dic = {'i': 1}
            same = 0
            for j in range(i+1, l):
                tx, ty = points[j][0], points[j][1]
                if tx == points[i][0] and ty == points[i][1]: #坐标一样的点
                    same += 1
                    continue
                if points[i][0] == tx: slope = 'i'#横坐标一样，斜率是1（垂直于x轴的竖线）
                else:slope = numpy.float128(points[i][1]-ty) /(points[i][0]-tx)#y/x  斜率
                if slope not in dic: dic[slope] = 1#新的斜率，放入dic
                dic[slope] += 1
            m = max(m, max(dic.values()) + same)#取最大的，dp
        return m


points = [[1,1],[2,2],[3,3]]
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
s = Solution()
res = s.maxPoints(points)
print(res)
