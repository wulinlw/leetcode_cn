#!/usr/bin/python
#coding:utf-8
import sys


class Solution(object):
    # 80ms
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        数字 1-9 在每一行只能出现一次。
        数字 1-9 在每一列只能出现一次。
        数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
        """
        # print(set(board[0]))
        r = range(10)
        c = range(10)
        z = range(10)
        for i in c:
            r[i] = {}
            c[i] = {}
            z[i] = {}
        for i in range(9):
            for j in range(9):
                # x
                if board[i][j] != "." and r[i].has_key(board[i][j]):
                    print('x', i, j, board[i][j])
                    return False
                else:
                    r[i][board[i][j]] = 1

                # y
                if board[j][i] != "." and c[i].has_key(board[j][i]):
                    print('y', i, j, board[j][i])
                    print(c)
                    return False
                else:
                    c[i][board[j][i]] = 1

                # zone
                zone = self.zonePosition(i, j)
                if board[i][j] != "." and z[zone].has_key(board[i][j]):
                    print('z', i, j, board[i][j])
                    return False
                else:
                    z[zone][board[i][j]] = 1

            # print(r)
            # print(c)
            # print("\r\n")
            # sys.exit(0)
        # print(c)
        # sys.exit(0)
        return True

    def zonePosition(self, x, y):
        if x < 3:
            if y < 3:
                return 1
            elif y >= 3 and y <= 5:
                return 4
            else:
                return 7
        elif x >= 3 and x <= 5:
            if y < 3:
                return 2
            elif y >= 3 and y <= 5:
                return 5
            else:
                return 8
        else:
            if y < 3:
                return 3
            elif y >= 3 and y <= 5:
                return 6
            else:
                return 9

    # 56ms
    def isValidSudoku_best(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        (row, block)            x轴重复
        (block, col)            y轴重复
        (row/3, col/3, block)   块重复
        """
        exist = []
        for row, rows in enumerate(board):
            for col, block in enumerate(rows):
                if block != ".":
                    exist.extend([(row, block), (block, col),(row / 3, col / 3, block)])
        return len(exist) == len(set(exist))


# board = [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# board = [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
board = [
    [".", ".", "4", ".", ".", ".", "6", "3","."], 
    [".", ".", ".", ".", ".", ".", ".", ".","."], 
    ["5", ".", ".", ".", ".", ".", ".", "9","."], 
    [".", ".", ".", "5", "6", ".", ".", ".", "."],
    ["4", ".", "3", ".", ".", ".", ".", ".","1"],
    [".", ".", ".", "7", ".", ".", ".", ".","."],
    [".", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".","."], 
    [".", ".", ".", ".", ".", ".", ".", ".", "."]
]
# 3，5  5，4  3/3,4/3,5
# 3, 5  5,6   3/3,6/3,5
s = Solution()
n = s.isValidSudoku_best(board)
print('return', n)
