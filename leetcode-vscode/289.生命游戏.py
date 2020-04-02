#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#
# https://leetcode-cn.com/problems/game-of-life/description/
#
# algorithms
# Medium (69.04%)
# Likes:    132
# Dislikes: 0
# Total Accepted:    15.8K
# Total Submissions: 22K
# Testcase Example:  '[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]'
#
# 根据 百度百科 ，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。
# 
# 给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0
# 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：
# 
# 
# 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
# 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
# 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
# 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
# 
# 
# 
# 根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。
# 
# 
# 
# 示例：
# 
# 输入： 
# [
# [0,1,0],
# [0,0,1],
# [1,1,1],
# [0,0,0]
# ]
# 输出：
# [
# [0,0,0],
# [1,0,1],
# [0,1,1],
# [0,1,0]
# ]
# 
# 
# 
# 进阶：
# 
# 
# 你可以使用原地算法解决本题吗？请注意，面板上所有格子需要同时被更新：你不能先更新某些格子，然后使用它们的更新后的值再更新其他格子。
# 本题中，我们使用二维数组来表示面板。原则上，面板是无限的，但当活细胞侵占了面板边界时会造成问题。你将如何解决这些问题？
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def gameOfLife2(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        forword = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1)]#上右下左 ，左上，右上，右下，坐下
        rows = len(board)
        cols = len(board[0])
        for r in range(rows):
            for c in range(cols):
                cnt = 0                                                                 #记录附近有几个活细胞
                for i in forword:                                                       #遍历8个相邻的细胞
                    newx, newy = r + i[0], c + i[1]
                    if 0<=newx<rows and 0<=newy<cols and abs(board[newx][newy])==1:     #巧妙的abs，下方需要死去的标记为-1了，这里abs后还是1，不会影响后面判断
                        cnt += 1
                if board[r][c] == 1 and (cnt<2 or cnt>3):                               #规则1，3，当前活细胞标记为死去 1 -> -1
                    board[r][c] = -1
                if board[r][c] == 0 and cnt == 3:                                       #规则4，当前死亡细胞标记为复活 0 -> 2
                    board[r][c] = 2
        
        for r in range(rows):                                                           #更新状态，2->1 -1->0
            for c in range(cols):
                if board[r][c] > 0:
                    board[r][c] = 1 
                else:
                    board[r][c] = 0


    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        forword = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1)]#上右下左 ，左上，右上，右下，坐下
        rows = len(board)
        cols = len(board[0])
        for r in range(rows):
            for c in range(cols):
                cnt = 0                                                                 #记录附近有几个活细胞
                for i in forword:                                                       #遍历8个相邻的细胞
                    newx, newy = r + i[0], c + i[1]
                    if 0<=newx<rows and 0<=newy<cols :                                  
                        cnt += board[newx][newy] & 1                                    # &1 是1的就+1
                if board[r][c] == 1 and (cnt in [2, 3]):                                #规则2，用第二位标记还活着
                    board[r][c] |= 2
                if board[r][c] == 0 and cnt == 3:                                       #规则4，用第二位标记还活着
                    board[r][c] |= 2
        
        for r in range(rows):                                                           #更新状态，第二位标记的是活的，右移一位即可
            for c in range(cols):
                board[r][c] >>= 1




# @lc code=end
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
o = Solution()
print(o.gameOfLife(board))
print(board)