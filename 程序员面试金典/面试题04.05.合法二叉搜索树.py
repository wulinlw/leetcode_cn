# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题04.05.合法二叉搜索树
# 
# https://leetcode-cn.com/problems/legal-binary-search-tree-lcci/
# 
# 实现一个函数，检查一棵二叉树是否为二叉搜索树。示例 1:输入:    2   / &#92  1   3输出: true示例 2:输入:    5   / &#92  1   4     / &#92    3   6输出: false解释: 输入为: [5,1,4,null,null,3,6]。     根节点的值为 5 ，但是其右子节点值为 4 。
# 
# Medium 35.3%
# Testcase Example: [2,1,3]
# 
# 提示:
# 如果使用前序遍历来遍历树，元素的顺序是正确的，这是否表明树实际上是有序的？有重复元素会发生什么？如果允许重复元素，它们必须位于特定的一边（通常是左边）。
# 作为一个二叉搜索树，并不是说每个节点都满足left.value <= current.value < right就够了。左边的每个节点必须小于当前节点，该节点还必须小于右边的所有节点。
# 如果左边的每个节点必须小于或等于当前节点，那么这就等于左边最大的节点必须小于或等于当前节点。
# 相比于根据leftTree.max和rightTree.min来验证当前节点的值，我们可以翻转逻辑吗？验证左子树的节点以确保其小于current.value。
# 把checkBST函数当作一个递归函数，保证每个节点在允许范围内(最小, 最大)。首先，这个范围是无限的。当我们遍历左边，最小的是负无穷大，最大的是root.value。你能实现这个递归函数，并且随着遍历而适当调整这些范围吗？
# 
# 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(root, small, big):
            if not root:return True
            if small >= root.val or root.val >= big:return False
            return dfs(root.left, small, root.val) and dfs(root.right, root.val, big) 
        return dfs(root, -2**32, 2**32-1)





o = Solution()
#  2
# 1 3
t1 = TreeNode(2)
t2 = TreeNode(1)
t3 = TreeNode(3)
root = t1
root.left = t2
root.right = t3
print(o.isValidBST(root))

#    5
#  1  4
#    3  6
t1 = TreeNode(5)
t2 = TreeNode(1)
t3 = TreeNode(4)
t4 = TreeNode(3)
t5 = TreeNode(6)

root = t1
root.left = t2
root.right = t3
t3.left = t4
t3.right = t5
print(o.isValidBST(root))
