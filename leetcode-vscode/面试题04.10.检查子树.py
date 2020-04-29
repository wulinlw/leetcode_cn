# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题04.10.检查子树
# 
# https://leetcode-cn.com/problems/check-subtree-lcci/
# 
# 检查子树。你有两棵非常大的二叉树：T1，有几万个节点；T2，有几万个节点。设计一个算法，判断 T2 是否为 T1 的子树。
# 如果 T1 有这么一个节点 n，其子树与 T2 一模一样，则 T2 为 T1 的子树，也就是说，从节点 n 处把树砍断，得到的树与 T2 完全相同。
# 
# 示例1:
# 
#  输入：t1 = [1, 2, 3], t2 = [2]
#  输出：true
# 
# 
# 示例2:
# 
#  输入：t1 = [1, null, 2, 4], t2 = [3, 2]
#  输出：false
# 
# 
# 提示：
# 
# 
# 	树的节点数目范围为[0, 20000]。
# 
# 
# 
# Medium 71.5%
# Testcase Example: [1, 2, 3]
# [2]
# 
# 提示:
# 如果T2是T1的子树，它的中序遍历将如何与T1的比较？它的前序和后序遍历如何？
# 中序遍历无法告诉我们更多。毕竟，每个具有相同值的二叉搜索树（不管结构如何）将具有相同的中序遍历。这也就是中序遍历的含义：内容是有序的（如果它在二叉搜索树这种特定情况下不起作用，那么对于一般二叉树来说它肯定不起作用）。然而，前序遍历更具指示性。
# 你可能得出结论，如果T2.preorderTraversal()是T1.preorderTraversal()的子字符串，则T2是T1的子树。这几乎是事实，除非树可能有重复的值。假设T1和T2具有所有重复值，但结构不同。即使T2不是T1的子树，前序遍历看起来也是一样的。你如何处理这样的情况？
# 尽管问题似乎源于重复的值，但不止如此。问题是，前序遍历是相同的，只是因为我们跳过了空节点（因为它们是空的）。考虑在访问到空节点时往前序遍历的字符串中插入一个占位符。把空节点记录为一个“真正的”节点，你就可以区分出不同的结构了。
# 或者用递归法处理这个问题。给定一个特殊节点T1，可以检查它的子树是否匹配T2吗？
# 
# 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t1 or not t2:return False
        return self.comp(t1,t2) or self.checkSubTree(t1.left, t2) or self.checkSubTree(t1.right, t2)

    def comp(self, t1, t2):
        if not t2:return True
        if not t1:return False
        return t1.val == t2.val and self.comp(t1.left, t2.left) and self.comp(t1.right, t2.right)



#  1
# 2 3
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
root = t1
root.left = t2
root.right = t3

o = Solution()
print(o.checkSubTree(t1, t3))
