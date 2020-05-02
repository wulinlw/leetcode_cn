# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题16.04.井字游戏
# 
# https://leetcode-cn.com/problems/tic-tac-toe-lcci/
# 
# 设计一个算法，判断玩家是否赢了井字游戏。输入是一个 N x N 的数组棋盘，由字符" "，"X"和"O"组成，其中字符" "代表一个空位。
# 以下是井字游戏的规则：
# 
# 
# 	玩家轮流将字符放入空位（" "）中。
# 	第一个玩家总是放字符"O"，且第二个玩家总是放字符"X"。
# 	"X"和"O"只允许放置在空位中，不允许对已放有字符的位置进行填充。
# 	当有N个相同（且非空）的字符填充任何行、列或对角线时，游戏结束，对应该字符的玩家获胜。
# 	当所有位置非空时，也算为游戏结束。
# 	如果游戏结束，玩家不允许再放置字符。
# 
# 
# 如果游戏存在获胜者，就返回该游戏的获胜者使用的字符（"X"或"O"）；如果游戏以平局结束，则返回 "Draw"；如果仍会有行动（游戏未结束），则返回 "Pending"。
# 
# 示例 1：
# 
# 输入： board = ["O X"," XO","X O"]
# 输出： "X"
# 
# 
# 示例 2：
# 
# 输入： board = ["OOX","XXO","OXO"]
# 输出： "Draw"
# 解释： 没有玩家获胜且不存在空位
# 
# 
# 示例 3：
# 
# 输入： board = ["OOX","XXO","OX "]
# 输出： "Pending"
# 解释： 没有玩家获胜且仍存在空位
# 
# 
# 提示：
# 
# 
# 	1 <= board.length == board[i].length <= 100
# 	输入一定遵循井字棋规则
# 
# 
# 
# Medium 46.6%
# Testcase Example: ["OX ","OX ","O  "]
# 
# 提示:
# 如果多次调用hasWon，你的解决方案可能会发生什么变化？
# 如果你正在为N×N的大小进行计算，你的解决方案可能会发生什么变化？
# 
# 
from typing import List
class Solution:
    def tictactoe(self, board: List[str]) -> str:
        n = len(board)
        def check(c):
            #行
            for i in range(n):
                status = True
                for j in range(n):
                    if board[i][j] != c:
                        status = False
                if status:
                    return True
            
            #列
            for j in range(n):
                status = True
                for i in range(n):
                    if board[i][j] != c:
                        status = False
                if status:
                    return True
            
            #左斜线
            status = True
            for i in range(n):
                if board[i][i] != c:
                    status = False
            if status:
                return True
            
            #右斜线
            status = True
            for i in range(n):
                if board[n-i-1][i] != c:
                    status = False
            if status:
                return True
        
        if check('X'):return 'X'
        if check('O'):return 'O'
        for i in range(n):
            for j in range(n):
                if board[i][j] == ' ':
                    return 'Pending'
        return 'Draw'



board = ["O X",
         " XO",
         "X O"
        ]
board = ["OOX","XXO","OXO"]
board = ["OOX","XXO","OX "]
o = Solution()
print(o.tictactoe(board))