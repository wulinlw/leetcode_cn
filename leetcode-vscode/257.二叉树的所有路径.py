#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#
# https://leetcode-cn.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (62.27%)
# Likes:    219
# Dislikes: 0
# Total Accepted:    27.6K
# Total Submissions: 44.2K
# Testcase Example:  '[1,2,3,null,5]'
#
# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 
# 输入:
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# 输出: ["1->2->5", "1->3"]
# 
# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
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
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:return []
        re = []
        def dfs(root, tmp):
            if not root.left and not root.right:
                re.append("->".join(tmp[:]+[str(root.val)]))
                return 
            tmp.append(str(root.val))
            if root.left:
                dfs(root.left, tmp)
            if root.right:
                dfs(root.right,tmp)
            tmp.pop()
        dfs(root, [])
        return re
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
print(o.binaryTreePaths(root))
