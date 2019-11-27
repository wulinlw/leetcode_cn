#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/learn/card/data-structure-binary-tree/3/solve-problems-recursively/14/
# 路径总和
# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
# 说明: 叶子节点是指没有子节点的节点。

# 示例: 
# 给定如下二叉树，以及目标和 sum = 22，

#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \      \
#         7    2      1
# 返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root: return False
        stack = [(root.val, root)]
        while stack:
            sum_, node = stack.pop()
            if node.right:
                stack.append((sum_ + node.right.val, node.right))
            if node.left:
                stack.append((sum_ + node.left.val, node.left))
            if not node.left and not node.right and sum_ == sum:
                return True
        return False



nums = [7,2,5,10,8]
m = 2
ss = Solution()
re = ss.splitArray(nums,m)
print(re)

