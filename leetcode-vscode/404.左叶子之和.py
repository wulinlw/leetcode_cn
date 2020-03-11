#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#
# https://leetcode-cn.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (53.69%)
# Likes:    129
# Dislikes: 0
# Total Accepted:    18.2K
# Total Submissions: 33.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 计算给定二叉树的所有左叶子之和。
# 
# 示例：
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
# 
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
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:return 0
        stack = [(root,0)]
        leftSum = 0
        while stack:
            for i in range(len(stack)):
                node,child = stack.pop(0)
                if child==1 and not node.left and not node.right:
                    leftSum += node.val
                if node.left:
                    stack.append((node.left, 1))
                if node.right:
                    stack.append((node.right, 0))
        return leftSum
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

o = Solution()
print(o.sumOfLeftLeaves(root))