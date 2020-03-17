#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#
# https://leetcode-cn.com/problems/sudoku-solver/description/
#
# algorithms
# Hard (59.80%)
# Likes:    345
# Dislikes: 0
# Total Accepted:    21.5K
# Total Submissions: 35.7K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# 编写一个程序，通过已填充的空格来解决数独问题。
# 
# 一个数独的解法需遵循如下规则：
# 
# 
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
# 
# 
# 空白格用 '.' 表示。
# 
# 
# 
# 一个数独。
# 
# 
# 
# 答案被标成红色。
# 
# Note:
# 
# 
# 给定的数独序列只包含数字 1-9 和字符 '.' 。
# 你可以假设给定的数独只有唯一解。
# 给定数独永远是 9x9 形式的。
# 
# 
#
# @lc code=start
import sys
from typing import List
from collections import defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        #判断当前坐标能不能填 d 这个数
        #不能出现在rows, columns, boxes中，重复的返回false
        #要填的数 d , 坐标 row,col
        def could_place(d, row, col):
            return not (d in rows[row] or d in columns[col] or \
                    d in boxes[box_index(row, col)])
        
        #放置一个数 d 到坐标 row,col
        #同时记录出现的信息到rows, columns, boxes中
        def place_number(d, row, col):
            rows[row][d] += 1
            columns[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)
        
        #撤销一个放置的数字，并在记录中删除 rows, columns, boxes中
        def remove_number(d, row, col):
            del rows[row][d]
            del columns[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = '.'    
            
        #回溯跑下一个格子，
        #注意行列判断， 最后一个格子代表结束
        def place_next_numbers(row, col):
            if col == N - 1 and row == N - 1:           #已经跑到最后一个了，返回True
                nonlocal sudoku_solved
                sudoku_solved = True  
            else:
                if col == N - 1:                        #最后一列了，跑下一行row+1, 0
                    backtrack(row + 1, 0)
                else:                                   #没到最后一列，往右走
                    backtrack(row, col + 1)
                
        #回溯
        def backtrack(row = 0, col = 0):
            if board[row][col] == '.':
                for d in range(1, 10):                  #依次填入1-9
                    if could_place(d, row, col):
                        place_number(d, row, col)       #填入数字 d 到坐标
                        place_next_numbers(row, col)
                        # if sudoku is solved, there is no need to backtrack
                        # since the single unique solution is promised
                        if not sudoku_solved:           #如果没有完成，就要撤销放置的这个数，说明放了这个数后，后面的路走不通
                            remove_number(d, row, col)  #注意这里的if判断，完成了是不需要撤销的
            else:
                place_next_numbers(row, col)            #有数字的跳过
                    
        
        n = 3                                           #小九宫格宽度
        N = n * n                                       #整个的宽度
        box_index = lambda row, col: (row // n ) * n + col // n #lambda 匿名函数计算小九宫格索引 0-9
        
        # 初始化 行、列、小九宫格
        rows = [defaultdict(int) for i in range(N)]
        columns = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]
        for i in range(N):                              #已出现过的数字，记录到rows,columns,boxes
            for j in range(N):
                if board[i][j] != '.': 
                    d = int(board[i][j])
                    place_number(d, i, j)
        
        sudoku_solved = False
        backtrack()                                     #开始回溯

        # 作者：LeetCode
        # 链接：https://leetcode-cn.com/problems/sudoku-solver/solution/jie-shu-du-by-leetcode/
        # 来源：力扣（LeetCode）
        # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# @lc code=end
board =[["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
        ]
o = Solution()
o.solveSudoku(board)
print(board)