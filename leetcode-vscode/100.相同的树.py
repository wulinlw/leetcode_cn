#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#
# https://leetcode-cn.com/problems/same-tree/description/
#
# algorithms
# Easy (56.54%)
# Likes:    318
# Dislikes: 0
# Total Accepted:    68K
# Total Submissions: 120K
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# 给定两个二叉树，编写一个函数来检验它们是否相同。
# 
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
# 
# 示例 1:
# 
# 输入:       1         1
# ⁠         / \       / \
# ⁠        2   3     2   3
# 
# ⁠       [1,2,3],   [1,2,3]
# 
# 输出: true
# 
# 示例 2:
# 
# 输入:      1          1
# ⁠         /           \
# ⁠        2             2
# 
# ⁠       [1,2],     [1,null,2]
# 
# 输出: false
# 
# 
# 示例 3:
# 
# 输入:       1         1
# ⁠         / \       / \
# ⁠        2   1     1   2
# 
# ⁠       [1,2,1],   [1,1,2]
# 
# 输出: false
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def dfs(p, q):
            if not p and not q:return True
            if not p or not q:return False
            if p.val !=q.val:return False
            l = dfs(p.left, q.left)
            r = dfs(p.right, q.right)
            return l and r
        return dfs(p, q)
# @lc code=end

#   1
#  2  3
# 4 5
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)

root = t1
root.left = t2
root.right = t3
t2.left = t4
t2.right = t5
roor1 = root

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)

root = t1
root.left = t2
root.right = t3
t2.left = t4
t2.right = t5
roor2 = root
# print(o.levelOrder(root))
print(o.isSameTree(root1, root2))