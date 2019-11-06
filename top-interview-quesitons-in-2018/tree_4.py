#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/featured/card/top-interview-quesitons-in-2018/269/tree/1168/
# 天际线问题
# 城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。现在，假设您获得了城市风光照片（图A）上显示的所有建筑物的位置和高度，请编写一个程序以输出由这些建筑物形成的天际线（图B）。

# Buildings Skyline Contour
# 每个建筑物的几何信息用三元组 [Li，Ri，Hi] 表示，其中 Li 和 Ri 分别是第 i 座建筑物左右边缘的 x 坐标，Hi 是其高度。可以保证 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX 和 Ri - Li > 0。您可以假设所有建筑物都是在绝对平坦且高度为 0 的表面上的完美矩形。
# 例如，图A中所有建筑物的尺寸记录为：[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] 。
# 输出是以 [ [x1,y1], [x2, y2], [x3, y3], ... ] 格式的“关键点”（图B中的红点）的列表，它们唯一地定义了天际线。关键点是水平线段的左端点。请注意，最右侧建筑物的最后一个关键点仅用于标记天际线的终点，并始终为零高度。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。
# 例如，图B中的天际线应该表示为：[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]。
# 说明:
# 任何输入列表中的建筑物数量保证在 [0, 10000] 范围内。
# 输入列表已经按左 x 坐标 Li  进行升序排列。
# 输出列表必须按 x 位排序。
# 输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...] 是不正确的答案；三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        import heapq
        events = sorted([(L,-H,R) for L,R,H in buildings] + list({(R,0,None) for _,R,_ in buildings}))
        #res是最终结果，hp表示“现在需要考虑的线段们”
        res , hp = [[0,0]] , [(0,float("inf"))]
        
        #对所有的线条进行遍历
        for x, negH, R in events:
            #当一个线条的左边界大于hp中线条的右边界时，说明这个线条已经没有任何作用了，可以删去
            while x >= hp[0][1]:
                heapq.heappop(hp)
            #如果这是一个非零线段，我们把它放入hp中
            if negH:
                heapq.heappush(hp,(negH , R))
            #这里需要注意，heapq保证列表中的第一个元素一定是最小元素，取相反数也就是目前最高元素。
            #res[-1][1]是结果中最后一个元素的高度，hp[0][0]是目前最高那个元素的高度，如果不相等，就需要更新res。
            #为什么我们只考虑dp中第一个元素？首先，这个元素在dp里面，所以它是有影响的，其次，它是最高的，当前我们只要最高的元素，至于比它低的元素，都被覆盖了
            if res[-1][1] + hp[0][0]:
                res.append([x,-hp[0][0]])
                
        return res[1:]

buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
s = Solution()
res = s.getSkyline(buildings)
print(res)


