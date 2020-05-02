# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题04.06.后继者
# 
# https://leetcode-cn.com/problems/successor-lcci/
# 
# 设计一个算法，找出二叉搜索树中指定节点的&ldquo;下一个&rdquo;节点（也即中序后继）。
# 如果指定节点没有对应的&ldquo;下一个&rdquo;节点，则返回null。
# 
# 示例 1:
# 
# 输入: root = [2,1,3], p = 1
# 
#   2
#  / \
# 1   3
# 
# 输出: 2
# 
# 示例 2:
# 
# 输入: root = [5,3,6,2,4,null,null,1], p = 6
# 
#       5
#      / \
#     3   6
#    / \
#   2   4
#  /   
# 1
# 
# 输出: null
# 
# 
# Medium 57.9%
# Testcase Example: [2,1,3]
# 1
# 
# 提示:
# 想想中序遍历是如何工作的，并尝试对其进行“逆向工程”。
# 这只是逻辑方法中的一步：一个特定节点的后继节点是右子树的最左节点。如果没有右子树呢？
# 
# 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        flag,re = None,None
        def inorder(root):
            nonlocal flag,re
            if not root: return None
            inorder(root.left)
            if flag:
                re = root
                flag = False
            if root == p:
                flag = True
            inorder(root.right)
        inorder(root)
        return re




o = Solution()
#  2
# 1 3
t1 = TreeNode(2)
t2 = TreeNode(None)
t3 = TreeNode(3)
root = t1
root.left = t2
root.right = t3
p = t1
print(o.inorderSuccessor(root, p))

#    5
#  3  6
# 2 4  
#1
# t1 = TreeNode(5)
# t2 = TreeNode(3)
# t3 = TreeNode(6)
# t4 = TreeNode(2)
# t5 = TreeNode(4)
# t6 = TreeNode(1)

# root = t1
# root.left = t2
# root.right = t3
# t2.left = t4
# t2.right = t5
# t4.left = t6
# p = t3
# print(o.inorderSuccessor(root, p))

