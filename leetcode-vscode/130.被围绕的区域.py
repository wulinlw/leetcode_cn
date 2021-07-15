#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#
from typing import List
# @lc code=start
class Solution:
    # 对于每一个边界上的 O，我们以它为起点，标记所有与它直接或间接相连的字母 O；
    # 最后我们遍历这个矩阵，对于每一个字母：
    # 如果该字母被标记过，则该字母为没有被字母 X 包围的字母 O，我们将其还原为字母 O；
    # 如果该字母没有被标记过，则该字母为被字母 X 包围的字母 O，我们将其修改为字母 X。
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        n, m = len(board), len(board[0])

        def dfs(x, y):
            if not 0 <= x < n or not 0 <= y < m or board[x][y] != 'O':
                return
            
            board[x][y] = "A"
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        # 每行的第一和最后一个，也就是边界，相邻的O都标记为A，最后这些挨着边框的O还是O，不会变动
        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)
        # 每一列的嘴上和最下边，界
        for i in range(m - 1):
            dfs(0, i)
            dfs(n - 1, i)
        
        # 最后替换，标记的不变的A为O，其他的需要变的O变成X
        for i in range(n):
            for j in range(m):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

# @lc code=end

