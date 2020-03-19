#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#
# https://leetcode-cn.com/problems/n-queens-ii/description/
#
# algorithms
# Hard (77.35%)
# Likes:    101
# Dislikes: 0
# Total Accepted:    18K
# Total Submissions: 23.2K
# Testcase Example:  '4'
#
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 
# 
# 
# 上图为 8 皇后问题的一种解法。
# 
# 给定一个整数 n，返回 n 皇后不同的解决方案的数量。
# 
# 示例:
# 
# 输入: 4
# 输出: 2
# 解释: 4 皇后问题存在如下两个不同的解法。
# [
# [".Q..",  // 解法 1
# "...Q",
# "Q...",
# "..Q."],
# 
# ["..Q.",  // 解法 2
# "Q...",
# "...Q",
# ".Q.."]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
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
        return len(output)
# @lc code=end

