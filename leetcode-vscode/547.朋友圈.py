#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#
# https://leetcode-cn.com/problems/friend-circles/description/
#
# algorithms
# Medium (55.05%)
# Likes:    220
# Dislikes: 0
# Total Accepted:    36.4K
# Total Submissions: 64.8K
# Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]'
#
# 班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C
# 的朋友。所谓的朋友圈，是指所有朋友的集合。
# 
# 给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j
# 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。
# 
# 示例 1:
# 
# 
# 输入: 
# [[1,1,0],
# ⁠[1,1,0],
# ⁠[0,0,1]]
# 输出: 2 
# 说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
# 第2个学生自己在一个朋友圈。所以返回2。
# 
# 
# 示例 2:
# 
# 
# 输入: 
# [[1,1,0],
# ⁠[1,1,1],
# ⁠[0,1,1]]
# 输出: 1
# 说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。
# 
# 
# 注意：
# 
# 
# N 在[1,200]的范围内。
# 对于所有学生，有M[i][i] = 1。
# 如果有M[i][j] = 1，则有M[j][i] = 1。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # dfs
    # 找一个同学，一个挨一个挖下去，并把找过的都在visited标记，
    # 每一轮就是一个朋友圈了
    def findCircleNum2(self, M: List[List[int]]) -> int:
        def dfs(visited, i):
            for j in range(len(M)):     #y坐标从0-n
                if M[i][j] == 1 and visited[j] == 0: #i，j是同学，j还没有dfs过
                    visited[j] = 1      #标记已访问，然后dfs j同学
                    dfs(visited, j)

        visited = [0] * len(M)
        re = 0
        for i in range(len(M)):         #x坐标从0-n
            if visited[i] == 0:         #当前节点没有访问过，dfs下去，结果+1
                dfs(visited, i)
                re += 1
        return re

    # 查并集 union find
    # 不带路径压缩
    def findCircleNum(self, M: List[List[int]]) -> int:
        parent = [-1 for i in range(len(M))]    #默认root设为-1

        def find(parent, i ):
            if parent[i] == -1:                 #找到这个集合中的root了，返回索引
                return i
            return find(parent, parent[i])      #往上找
        
        def union(parent, x, y):
            x_root = find(parent, x)            #找到各自的root，让后关联起来
            y_root = find(parent, y)
            if x_root != y_root:
                parent[y_root] = x_root
        
        for i in range(len(M)):
            for j in range(i, len(M)):
                if M[i][j] == 1 and i != j:     #i，j是同学，关联起来
                    union(parent, i, j)         
        # print(parent)
        re = 0
        for i in range(len(parent)):            #遍历关系表，-1代表root，就是一个独立的合集
            if parent[i] == -1:
                re += 1
        return re

        
# @lc code=end
M = [
    [1,1,0],
    [1,1,0],
    [0,0,1]
    ]
o = Solution()
print(o.findCircleNum(M))