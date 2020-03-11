#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (64.45%)
# Likes:    194
# Dislikes: 0
# Total Accepted:    45.1K
# Total Submissions: 69.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
# 
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回其自底向上的层次遍历为：
# 
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
# 
# 
#
from typing import List
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        stack = [root]
        re = []
        while stack:
            tmp = []
            for i in range(len(stack)):
                node = stack.pop(0)
                tmp.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            re.append(tmp)
        return re[::-1]
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
print(o.levelOrderBottom(root))