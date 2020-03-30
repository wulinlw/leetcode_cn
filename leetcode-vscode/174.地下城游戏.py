#
# @lc app=leetcode.cn id=174 lang=python3
#
# [174] 地下城游戏
#
# https://leetcode-cn.com/problems/dungeon-game/description/
#
# algorithms
# Hard (39.99%)
# Likes:    177
# Dislikes: 0
# Total Accepted:    8K
# Total Submissions: 19.8K
# Testcase Example:  '[[-2,-3,3],[-5,-10,1],[10,30,-5]]'
#
# 
# table.dungeon, .dungeon th, .dungeon td {
# ⁠ border:3px solid black;
# }
# 
# ⁠.dungeon th, .dungeon td {
# ⁠   text-align: center;
# ⁠   height: 70px;
# ⁠   width: 70px;
# }
# 
# 
# 一些恶魔抓住了公主（P）并将她关在了地下城的右下角。地下城是由 M x N
# 个房间组成的二维网格。我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。
# 
# 骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。
# 
# 有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；其他房间要么是空的（房间里的值为
# 0），要么包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。
# 
# 为了尽快到达公主，骑士决定每次只向右或向下移动一步。
# 
# 
# 
# 编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。
# 
# 例如，考虑到如下布局的地下城，如果骑士遵循最佳路径 右 -> 右 -> 下 -> 下，则骑士的初始健康点数至少为 7。
# 
# 
# ⁠
# -2 (K) 
# -3 
# 3 
# ⁠
# ⁠
# -5 
# -10 
# 1 
# ⁠
# ⁠
# 10 
# 30 
# -5 (P) 
# ⁠
# 
# 
# 
# 
# 
# 说明:
# 
# 
# 
# 骑士的健康点数没有上限。
# 
# 任何房间都可能对骑士的健康点数造成威胁，也可能增加骑士的健康点数，包括骑士进入的左上角房间以及公主被监禁的右下角房间。
# 
#
from typing import List
# @lc code=start
class Solution:
    # dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
    # 从右下角到左上角，每次取右，下，较小的 - 当前值，小于0的要设置为1点血
    # 为什么是减法，反过来思考，因为最小角是最大血，走到左上角的时候位1点血
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        r = len(dungeon)
        c = len(dungeon[0])
        dp = [[0 for i in range(c)] for i in range(r)]
        dp[-1][-1] = max(1, 1-dungeon[-1][-1])                  #右下角初始化，<=1的，最低要为1
        for i in range(r-2, -1, -1):
            dp[i][c-1] = max(1, dp[i+1][c-1]-dungeon[i][c-1])   #最右列，从下往上
        for i in range(c-2, -1, -1):
            dp[r-1][i] = max(1, dp[r-1][i+1]-dungeon[r-1][i])   #最下行，从右向左
        for i in range(r-2, -1, -1):
            for j in range(c-2, -1, -1):
                dpmin = min(dp[i+1][j], dp[i][j+1])             #右，下，取小的
                dp[i][j] = max(1, dpmin-dungeon[i][j])          #最小是1，负血死亡
        return dp[0][0]

# @lc code=end
dungeon = [
    [-2, -3,  3],
    [-5, -10, 1],
    [10, 30, -5]
]
o = Solution()
print(o.calculateMinimumHP(dungeon))