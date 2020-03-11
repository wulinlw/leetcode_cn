#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#
# https://leetcode-cn.com/problems/convert-bst-to-greater-tree/description/
#
# algorithms
# Easy (58.91%)
# Likes:    210
# Dislikes: 0
# Total Accepted:    18.1K
# Total Submissions: 30.6K
# Testcase Example:  '[5,2,13]'
#
# 给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater
# Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。
# 
# 
# 
# 例如：
# 
# 输入: 原始二叉搜索树:
# ⁠             5
# ⁠           /   \
# ⁠          2     13
# 
# 输出: 转换为累加树:
# ⁠            18
# ⁠           /   \
# ⁠         20     13
# 
# 
# 
# 
# 注意：本题和 1038:
# https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/ 相同
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
    # 中序遍历，只不过先从右边走起
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:return None
        sum = 0
        def postorder(root):
            nonlocal sum
            if not root:return
            postorder(root.right)
            sum += root.val
            root.val = sum
            postorder(root.left)
        postorder(root)
        return root
# @lc code=end

t1 = TreeNode(5)
t2 = TreeNode(2)
t3 = TreeNode(13)

root = t1
root.left = t2
root.right = t3


o = Solution()
t=o.convertBST(root)
# print(o.levelOrder(t))
# print(o.convertBST(root))