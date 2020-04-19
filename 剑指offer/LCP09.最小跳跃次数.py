# LCP 09. 最小跳跃次数
# 为了给刷题的同学一些奖励，力扣团队引入了一个弹簧游戏机。游戏机由 N 个特殊弹簧排成一排，编号为 0 到 N-1。初始有一个小球在编号 0 的弹簧处。若小球在编号为 i 的弹簧处，通过按动弹簧，可以选择把小球向右弹射 jump[i] 的距离，或者向左弹射到任意左侧弹簧的位置。也就是说，在编号为 i 弹簧处按动弹簧，小球可以弹向 0 到 i-1 中任意弹簧或者 i+jump[i] 的弹簧（若 i+jump[i]>=N ，则表示小球弹出了机器）。小球位于编号 0 处的弹簧时不能再向左弹。

# 为了获得奖励，你需要将小球弹出机器。请求出最少需要按动多少次弹簧，可以将小球从编号 0 弹簧弹出整个机器，即向右越过编号 N-1 的弹簧。

# 示例 1：

# 输入：jump = [2, 5, 1, 1, 1, 1]

# 输出：3

# 解释：小 Z 最少需要按动 3 次弹簧，小球依次到达的顺序为 0 -> 2 -> 1 -> 6，最终小球弹出了机器。

# 限制：

# 1 <= jump.length <= 10^6
# 1 <= jump[i] <= 10000

# https://leetcode-cn.com/problems/zui-xiao-tiao-yue-ci-shu/

import collections
from typing import List
class Solution:
    # bfs
    def minJump(self, jump: List[int]) -> int:
        inq_min = 0                             #上一跳的起点
        dis = [None] * len(jump)                #记录到达这个位置最少需要几步
        dis[0] = 0                              #初始化，第0个位置需要0步
        q = collections.deque([0])
        while q:
            u = q.popleft()                     #当前坐标
            for v in range(inq_min + 1, u):     #遍历可以回头的位置，记录步数，bfs
                if dis[v] is None:
                    dis[v] = dis[u] + 1
                    q.append(v)
            inq_min = u
            idx = u + jump[u]                   #当前能到的最远距离
            if idx >= len(jump):                #跳出，在倒数第二步基础上+1
                print(dis)
                return dis[u] + 1
            if dis[idx] is None:
                dis[idx] = dis[u] + 1           #在上一步基础上+1
                q.append(idx)                   #下次从这个位置跳
            



jump = [2, 5, 1, 1, 1, 1]
# jump = [2, 5, 1, 1, 1,3, 1,1,1]
jump = [3,7,6,1,4,3,7,8,1,2,8,5,9,8,3,2,7,5,1,1] #0-3-2-8-7-15-13-21
       #          5         0         5       9
# jump = [1]
o = Solution()
print(o.minJump(jump))