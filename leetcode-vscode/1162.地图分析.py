#
# @lc app=leetcode.cn id=1162 lang=python3
#
# [1162] 地图分析
#
# https://leetcode-cn.com/problems/as-far-from-land-as-possible/description/
#
# algorithms
# Medium (38.25%)
# Likes:    53
# Dislikes: 0
# Total Accepted:    11.8K
# Total Submissions: 27.8K
# Testcase Example:  '[[1,0,1],[0,0,0],[1,0,1]]'
#
# 你现在手里有一份大小为 N x N 的『地图』（网格） grid，上面的每个『区域』（单元格）都用 0 和 1 标记好了。其中 0 代表海洋，1
# 代表陆地，你知道距离陆地区域最远的海洋区域是是哪一个吗？请返回该海洋区域到离它最近的陆地区域的距离。
# 
# 我们这里说的距离是『曼哈顿距离』（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个区域之间的距离是 |x0 -
# x1| + |y0 - y1| 。
# 
# 如果我们的地图上只有陆地或者海洋，请返回 -1。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：[[1,0,1],[0,0,0],[1,0,1]]
# 输出：2
# 解释： 
# 海洋区域 (1, 1) 和所有陆地区域之间的距离都达到最大，最大距离为 2。
# 
# 
# 示例 2：
# 
# 
# 
# 输入：[[1,0,0],[0,0,0],[0,0,0]]
# 输出：4
# 解释： 
# 海洋区域 (2, 2) 和所有陆地区域之间的距离都达到最大，最大距离为 4。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= grid.length == grid[0].length <= 100
# grid[i][j] 不是 0 就是 1
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # 和994的腐烂橘子完全是一道同样的题，
    # 所谓的多源广度优先搜索就是假设在当前状态前加一个超级节点罢了，
    # 根据这个思路代码可以是这样样子的：
    # 使用队列做广度优先搜索
    # 访问过的位置就可以置为陆地（1）
    # 事实上可以理解为从将陆地（1）一圈一圈的扩大，直到扩大到没有海洋（0）
    # https://leetcode-cn.com/problems/as-far-from-land-as-possible/solution/zhen-liang-yan-sou-huan-neng-duo-yuan-kan-wan-miao/
    def maxDistance(self, grid: List[List[int]]) -> int:
        # BFS 宽度优先搜索 向外一层层扩散
        N = len(grid)
        land = [[x,y] for x in range(N) for y in range(N) if grid[x][y]]        #记录陆地坐标

        if len(land)==0 or len(land)==N*N:                                      #没有陆地，或全是陆地
            return -1

        direction = [(0,-1),(1,0),(0,1),(-1,0)]
        length = -1                                                             #从-1开始的

        def valid(x,y):                                                         #坐标越界判断
            return -1<x<N and -1<y<N

        while land:
            length+=1                                                           #距离加1
            tem = []                                                            #储存即将检索的海洋坐标
            for i in land:
                for x,y in direction:                                           #每个陆地王四个方向扩张1步
                    newx,newy = i[0]+x,i[1]+y
                    if valid(newx,newy) and grid[newx][newy]==0:                #如果是海洋，设为2
                        grid[newx][newy]=2
                        tem.append((newx,newy))                                 #记录下呗扩张的海洋坐标
            land = list(set(tem))                                               #需要去重，更新land，循环直到没有land，这样走的步数就是海洋离陆地的距离

        return length
# @lc code=end

grid = [
    [1,0,1],
    [0,0,0],
    [1,0,1]
    ]
o = Solution()
print(o.maxDistance(grid))