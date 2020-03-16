#!/usr/bin/python
#coding:utf-8

# 面试题 08.12. 八皇后
# 设计一种算法，打印 N 皇后在 N × N 棋盘上的各种摆法，其中每个皇后都不同行、不同列，也不在对角线上。这里的“对角线”指的是所有的对角线，不只是平分整个棋盘的那两条对角线。

# 注意：本题相对原题做了扩展
# 示例:
#  输入：4
#  输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
#  解释: 4 皇后问题存在如下两个不同的解法。
# [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# https://leetcode-cn.com/problems/eight-queens-lcci/


from typing import List
class Solution:
    # https://leetcode-cn.com/problems/eight-queens-lcci/solution/php-hui-su-jie-fa-by-zzpwestlife-4/
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


o = Solution()
print(o.solveNQueens(4))