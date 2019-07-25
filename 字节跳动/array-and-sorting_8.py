#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/bytedance/243/array-and-sorting/1036/
# 朋友圈
# 班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。
# 给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。

# 示例 1:
# 输入: 
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# 输出: 2 
# 说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
# 第2个学生自己在一个朋友圈。所以返回2。
# 示例 2:

# 输入: 
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# 输出: 1
# 说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。
# 注意：

# N 在[1,200]的范围内。
# 对于所有学生，有M[i][i] = 1。
# 如果有M[i][j] = 1，则有M[j][i] = 1。

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        """
        算法：DFS
        思路：
            可以将题目转换为是在一个图中求连通子图的问题，给出的N*N的矩阵就是邻接矩阵，建立N个节点的visited数组，
            从not visited的节点开始深度优先遍历，遍历就是在邻接矩阵中去遍历，如果在第i个节点的邻接矩阵那一行中的第j
            个位置处M[i][j]==1 and not visited[j]，就应该dfs到这个第j个节点的位置，
        复杂度分析：
            时间：ON2?遍历所有节点
            空间：ON，visited数组
        """
        if M == [] or M[0] == []:
            return 0
        n = len(M)
        visited = [False] * n
    
        def dfs(i):
            visited[i] = True
            for j in range(n):
                if M[i][j] == 1 and not visited[j]:
                    dfs(j)
    
        counter = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                counter += 1
        return counter



M = [[1,1,0],
 [1,1,0],
 [0,0,1]]
s = Solution()
n = s.findCircleNum(M)
print(n)


