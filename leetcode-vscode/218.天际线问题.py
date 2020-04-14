#
# @lc app=leetcode.cn id=218 lang=python3
#
# [218] 天际线问题
#
# https://leetcode-cn.com/problems/the-skyline-problem/description/
#
# algorithms
# Hard (40.68%)
# Likes:    166
# Dislikes: 0
# Total Accepted:    6.1K
# Total Submissions: 14.8K
# Testcase Example:  '[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]'
#
# 
# 城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。现在，假设您获得了城市风光照片（图A）上显示的所有建筑物的位置和高度，请编写一个程序以输出由这些建筑物形成的天际线（图B）。
# 
# ⁠   
# 
# 每个建筑物的几何信息用三元组 [Li，Ri，Hi] 表示，其中 Li 和 Ri 分别是第 i 座建筑物左右边缘的 x 坐标，Hi 是其高度。可以保证 0
# ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX 和 Ri - Li > 0。您可以假设所有建筑物都是在绝对平坦且高度为 0
# 的表面上的完美矩形。
# 
# 例如，图A中所有建筑物的尺寸记录为：[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] 。
# 
# 输出是以 [ [x1,y1], [x2, y2], [x3, y3], ... ]
# 格式的“关键点”（图B中的红点）的列表，它们唯一地定义了天际线。关键点是水平线段的左端点。请注意，最右侧建筑物的最后一个关键点仅用于标记天际线的终点，并始终为零高度。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。
# 
# 例如，图B中的天际线应该表示为：[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0]
# ]。
# 
# 说明:
# 
# 
# 任何输入列表中的建筑物数量保证在 [0, 10000] 范围内。
# 输入列表已经按左 x 坐标 Li  进行升序排列。
# 输出列表必须按 x 位排序。
# 输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...]
# 是不正确的答案；三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]
# 
# 
#
from typing import List
import heapq
# @lc code=start
class Solution:
    # 扫描线（最大堆）sweep line
    # 使用扫描线，从左向右扫过，如果遇到左端点，将高度入堆；如果遇到右端点，将高度从堆中删除。
    # 这样做有什么意义呢？
    # 因为高度入堆的时候，获取这个堆的最大值，判断一下最大值是否和前一关键点的当前高度是否相等，如果不相等，说明这是一个拐点，也是天际线的关键点，然后更新当前高度，即当前高度等于最大值；
    # 高度出堆的时候，将这个高度从堆中删除，接着获取这个堆中的最大值，判断一下这个最大值和前一关键点的当前高度是否相等，如果不相等，说明这也是一个拐点。
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        #思路：最大堆，每次在判断关键点的时候，移除所有右端点≤当前点的堆顶。
        if not buildings:return []
        points = []
        heap = [[0, float('inf')]]          #最大堆，（高度，右上角x坐标）
        res = [[0, 0]]

        #1.将所有端点加入到点集中(每个建筑物的左右端点)
        for l, r, h in buildings:
            points.append((l, -h, r))       #大楼左上角，-值，变为最大堆
            points.append((r, h, 0))        #大楼右上角，知道大楼结尾，跑出线段时弹出最高楼

        #2.将端点从小到大排序
        points.sort()                       #按横坐标排序
        print(points)

        #3.遍历每一个点
        for l, h, r in points:
            while l >= heap[0][1]:          #这里的l是右上角x坐标，最高的楼已经走完了，需要把它弹出去，这时候堆顶的高度变化，在和最后一个结果对比，不一样就加入结果
                heapq.heappop(heap)
            if h < 0:                       #左上角都加入堆中，但是放的是（高度，右上角），堆顶是最高楼
                heapq.heappush(heap, [h, r])
            if res[-1][1] != -heap[0][0]:   #最后的高度 != 堆顶的高度  ，当前高度和之前一个楼一样，那当前楼的左上角就不会露出来，高或矮才可以有轮廓
                res.append([l, -heap[0][0]])#x, y（高度） l可能是左上角，也可能是右上角
        return res[1:]

    # https://leetcode-cn.com/problems/the-skyline-problem/solution/fen-er-zhi-zhi-er-fen-fa-dui-by-powcai/

    # 线段树
    # https://leetcode-cn.com/problems/the-skyline-problem/solution/xian-duan-shu-hao-xiang-shi-yong-de-ren-bu-duo-by-/
# @lc code=end
buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
o = Solution()
print(o.getSkyline(buildings))