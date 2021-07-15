#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        if node in self.visited:            # 如果该节点已经被访问过了，则直接从哈希表中取出对应的克隆节点返回
            return self.visited[node]

        clone_node = Node(node.val, [])     # 克隆节点，注意到为了深拷贝我们不会克隆它的邻居的列表
        self.visited[node] = clone_node     # 哈希表存储

        if node.neighbors:                  # 遍历该节点的邻居并更新克隆节点的邻居列表
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node

# @lc code=end



adjList = [[2,4],[1,3],[2,4],[1,3]]
s = Solution()
# print(s.cloneGraph())