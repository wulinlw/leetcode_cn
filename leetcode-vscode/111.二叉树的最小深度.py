#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (41.64%)
# Likes:    221
# Dislikes: 0
# Total Accepted:    56.4K
# Total Submissions: 135.2K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最小深度。
# 
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回它的最小深度  2.
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
    def minDepth(self, root: TreeNode) -> int:
        if not root:return 0 
        def dfs(root):
            if not root:return 0
            if not root.left and not root.right :return 1
            l = dfs(root.left)
            r = dfs(root.right)
            if not l or not r:  #没有左或右子树
                return l+r+1
            return min(l,r)+1
        return dfs(root)
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
# print(o.levelOrder(root))

# root = TreeNode(0)
o = Solution()
print(o.minDepth(root))