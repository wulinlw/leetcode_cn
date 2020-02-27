#!/usr/bin/python
#coding:utf-8

# 矩阵中的路径
# 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
# 路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
# 如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
# 例如 [[a b c e], [s f c s], [a d e e]] 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，
# 因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。

class Solution:
    def hasPath(self, matrix, word):
        m = len(matrix)
        n = len(matrix[0])
        visited = [[False for i in  range(n)] for i in range(m)] #注意这里，外层用行数，否则第二个例子不过
        # print(visited)
        for i in range(m):
            for j in range(n):
                if self.find(matrix, word, 0, i, j, visited):
                    return True
        return False

    def find(self, board, word, cur, i, j, visited):
        if cur == len(word):
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or visited[i][j] or board[i][j]!=word[cur]:
            return False
        visited[i][j] = True
        result = self.find(board, word, cur + 1, i + 1, j, visited) or\
                 self.find(board, word, cur + 1, i - 1, j, visited) or\
                 self.find(board, word, cur + 1, i, j + 1, visited) or\
                 self.find(board, word, cur + 1, i, j - 1, visited)         
        visited[i][j] = False
        return result
        

matrix = [
    ["a","b","t","g"],
    ["c","f","c","s"],
    ["j","d","e","h"]
]
obj = Solution()
print(obj.hasPath(matrix, "bfce"))
print(obj.hasPath([["a","a"]], "aa"))
