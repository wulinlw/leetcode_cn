#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#
# https://leetcode-cn.com/problems/n-queens/description/
#
# algorithms
# Hard (67.99%)
# Likes:    355
# Dislikes: 0
# Total Accepted:    30.2K
# Total Submissions: 44.1K
# Testcase Example:  '4'
#
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 
# 
# 
# 上图为 8 皇后问题的一种解法。
# 
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
# 
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
# 
# 示例:
# 
# 输入: 4
# 输出: [
# ⁠[".Q..",  // 解法 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
# 
# ⁠["..Q.",  // 解法 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # 面试题 08.12. 八皇后
    # 和这题代码一样
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [['.' for i in range(n)] for i in range(n)]
        # print(grid)
        re = []
        def backtrack(n, grid, row):
            nonlocal re
            if row == n: 
                tmp = []
                for i in range(len(grid)):
                    tmp.append("".join(grid[i]))
                re.append(tmp)
                return 

            # 当前行 遍历每一列
            for col in range(n):
                if not vaild(n, grid, row, col):
                    continue
                grid[row][col] = 'Q'                #回溯，设置状态
                backtrack(n, grid, row+1)
                grid[row][col] = '.'                #撤销改变，继续下一轮

        # 横竖、左斜线，右斜线看看有没有Q，右返回False
        def vaild(n, grid, row, col):    
            # // 同一行，无需考虑
            # // 左下和右下，遍历到这里时还是空的，无需考虑

            # // 同一列
            for i in range(n):
                if grid[i][col] == 'Q':return False
            
            # // 左上
            i = row-1 
            j = col-1
            while i>=0 and j>=0:
                if grid[i][j] == 'Q':return False
                i-=1 
                j-=1 

            # // 右上
            i = row-1 
            j = col+1
            while i>=0 and j<n:
                if grid[i][j] == 'Q':return False
                i-=1 
                j+=1
            return True 


        backtrack(n, grid, 0)
        return re

    # [37] 解数独
    # 和解数独一样的算法框架
    def solveNQueens2(self, n: int) -> List[List[str]]:
        # 是否可以放置，已存在坐标，左斜线，右斜线
        # hill_diagonals[row - col] 右斜线，在这条线上的所有格子，row-col相等
        # dale_diagonals[row + col] 左斜线
        def could_place(row, col):
            return not (cols[col] + hill_diagonals[row - col] + dale_diagonals[row + col])
        
        #是否可以放置
        def place_queen(row, col):
            queens.add((row, col))
            cols[col] = 1
            hill_diagonals[row - col] = 1
            dale_diagonals[row + col] = 1
        
        #撤销放置
        def remove_queen(row, col):
            queens.remove((row, col))
            cols[col] = 0
            hill_diagonals[row - col] = 0
            dale_diagonals[row + col] = 0
        
        # 添加结果 .*col + Q + .*剩下的col
        def add_solution():
            solution = []
            for _, col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            output.append(solution)
        
        #回溯
        def backtrack(row = 0):
            for col in range(n):                #每行只能放一个，这行放了就去下一行
                if could_place(row, col):
                    place_queen(row, col)
                    if row + 1 == n:            #结束了放入结果，没到这里的都是被回溯撤销路径了
                        add_solution()
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)      #撤销
        
        cols = [0] * n
        hill_diagonals = [0] * (2 * n - 1)      #右斜线
        dale_diagonals = [0] * (2 * n - 1)      #左斜线
        queens = set()                          #放置皇后的坐标
        output = []
        backtrack()
        return output

# @lc code=end

o = Solution()
print(o.solveNQueens(4))