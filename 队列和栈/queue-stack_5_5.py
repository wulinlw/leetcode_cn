#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/learn/card/queue-stack/220/conclusion/892/
# 01 矩阵
# 给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

# 两个相邻元素间的距离为 1 。
# 示例 1:
# 输入:
# 0 0 0
# 0 1 0
# 0 0 0
# 输出:
# 0 0 0
# 0 1 0
# 0 0 0

# 示例 2:
# 输入:
# 0 0 0
# 0 1 0
# 1 1 1
# 输出:
# 0 0 0
# 0 1 0
# 1 2 1
# 注意:

# 给定矩阵的元素个数不超过 10000。
# 给定矩阵中至少有一个元素是 0。
# 矩阵中的元素只在四个方向上相邻: 上、下、左、右。
class Solution(object):
    # 其实就是遍历两次就可以了。
    # 每个非0点到0的距离，跟它上下左右到0的距离有关，所以第一次遍历先将左上两个位置的非0点最小者加1更改。
    # 这样就是从左上往右下看，非0点到0的最短距离，但是这样还不知道从右下到左上看的最短距离。
    # 所以再从右下到左上遍历，注意这次更新除了要取右下两个点的最短距离之外，还要跟当前位置的点做一次最小值比较，因为右下可能距离更远。
    def updateMatrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                l,t= 10001,10001
                if matrix[i][j] != 0:
                    if i > 0: 
                        t = matrix[i - 1][j] #上一行的
                    if j > 0:
                        l = matrix[i][j - 1] #左边的
                    matrix[i][j] = min(l,t) + 1
        # print(matrix)
        for i in range(len(matrix) - 1, -1 ,-1):
            for j in range(len(matrix[0]) - 1, -1, -1):
                r,b = 10001,10001
                if matrix[i][j] != 0:
                    if i < len(matrix) - 1: 
                        b = matrix[i + 1][j]   #下面一个
                    if j < len(matrix[0]) - 1:
                        r = matrix[i][j + 1]    #右边一个
                    matrix[i][j] = min(matrix[i][j], min(r,b) + 1)
        return matrix

# 作者：jimmy00745
# 链接：https://leetcode-cn.com/problems/01-matrix/solution/pao-ding-jie-niu-yi-bu-yi-bu-xiang-jie-01ju-zhen-1/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

matrix = [
    [0,0,0],
    [0,1,0],
    [0,0,1]]
ss = Solution()
re = ss.updateMatrix(matrix)
print(re)





