#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (50.22%)
# Likes:    796
# Dislikes: 0
# Total Accepted:    146.8K
# Total Submissions: 284.1K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
# 
# 
# 
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# 
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# 进阶：
# 
# 你可以运用递归和迭代两种方法解决这个问题吗？
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 将根节点的左右节点假设成两颗独立的树 
    # 递归调用时，因是对称，所以是左树左节点与右树右节点，左树右节点与右树左节点
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.recursiveTree(root.left, root.right)

    def recursiveTree(self, left, right):
        if not left and not right:
            return True
        if not left or not right:#有一遍是空的，不对称
            return False
        if left.val == right.val:
            return self.recursiveTree(left.left, right.right) and self.recursiveTree(left.right, right.left)
        return False
        
# @lc code=end

