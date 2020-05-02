# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题04.01.节点间通路
# 
# https://leetcode-cn.com/problems/route-between-nodes-lcci/
# 
# 节点间通路。给定有向图，设计一个算法，找出两个节点之间是否存在一条路径。
# 示例1:
# 
#  输入：n = 3, graph = [[0, 1], [0, 2], [1, 2], [1, 2]], start = 0, target = 2
#  输出：true
# 
# 
# 示例2:
# 
#  输入：n = 5, graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]], start = 0, target = 4
#  输出 true
# 
# 
# 提示：
# 
# 
# 	节点数量n在[0, 1e5]范围内。
# 	节点编号大于等于 0 小于 n。
# 	图中可能存在自环和平行边。
# 
# 
# 
# Medium 53.2%
# Testcase Example: 3
# [[0, 1], [0, 2], [1, 2], [1, 2]]
# 0
# 2
# 
# 提示:
# 有两个众所周知的算法可以做到这一点。其利弊是什么？
# 
# 
from typing import List
import collections
class Solution:
    # dfs
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        def dfs(start, visited):
            if start == target:
                return True
            if visited[start]:                      #防止死循环
                return False
            visited[start] = True
            for i in index[start]:
                if dfs(i, visited):
                    return True
            return False

        visited = [False] * n                       #访问过的记录，防止死循环
        index = collections.defaultdict(list)
        for i in graph:                             #构建邻接表
            index[i[0]].append(i[1])
        return dfs(start, visited)
    
    #bfs
    def findWhetherExistsPath2(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        # 构建邻接表
        link_table = [[] for _ in range(n)]
        for i, j in graph:
            link_table[i].append(j)
        visted = [0] * n # 访问数组
        # BFS
        que = [start]
        while que:
            cur_node = que.pop()
            if target in link_table[cur_node]: return True
            for node in link_table[cur_node]:
                if visted[node]==0:
                    que.insert(0,node)
            visted[cur_node] = 1
        return False




n = 3   #N个点
graph = [[0, 1], [0, 2], [1, 2], [1, 2]]
start = 0
target = 2
n = 5
graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [1, 3], [2, 3], [3, 4]]
start = 0
target = 4
o = Solution()
print(o.findWhetherExistsPath(n, graph, start, target))
