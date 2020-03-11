#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/description/
#
# algorithms
# Easy (68.27%)
# Likes:    75
# Dislikes: 0
# Total Accepted:    17.6K
# Total Submissions: 25.7K
# Testcase Example:  '[1,null,3,2,4,null,5,6]\r'
#
# 给定一个 N 叉树，找到其最大深度。
# 
# 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
# 
# 例如，给定一个 3叉树 :
# 
# 
# 
# 
# 
# 
# 
# 我们应返回其最大深度，3。
# 
# 说明:
# 
# 
# 树的深度不会超过 1000。
# 树的节点总不会超过 5000。
# 
#

# @lc code=start
""""""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    
    def maxDepth(self, root: 'Node') -> int:
        def dfs(root):
            if not root:return 0
            if root.children == []:return 1
            tmp = []
            for i in root.children:
                tmp.append(self.maxDepth(i))
            return max(tmp)+1
        return dfs(root)
# @lc code=end

t1 = Node(1,[])
t2 = Node(3,[])
t3 = Node(2,[])
t4 = Node(4,[])
t5 = Node(5,[])
t6 = Node(6,[])
root = t1
root.children.extend([t2,t3,t4])
t2.children.extend([t5,t6])

o = Solution()
print(o.maxDepth(root))