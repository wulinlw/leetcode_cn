#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (40.49%)
# Likes:    514
# Dislikes: 0
# Total Accepted:    46.2K
# Total Submissions: 112K
# Testcase Example:  '[1,2,3]'
#
# 给定一个非空二叉树，返回其最大路径和。
# 
# 本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
# 
# 示例 1:
# 
# 输入: [1,2,3]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# 输出: 6
# 
# 
# 示例 2:
# 
# 输入: [-10,9,20,null,null,15,7]
# 
# -10
# / \
# 9  20
# /  \
# 15   7
# 
# 输出: 42
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
    def maxPathSum(self, root: TreeNode) -> int:
        self.curr_max = float('-inf')
        def getMax(root):
            if root == None:
                return 0
            left = max(0,getMax(root.left))
            right = max(0,getMax(root.right))
            self.curr_max = max(self.curr_max , left + right + root.val)
            return max(left, right)+root.val
        getMax(root)
        return self.curr_max
# @lc code=end
root = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
root.left = t2
root.right = t3

s = Solution()
print(s.maxPathSum(root))
