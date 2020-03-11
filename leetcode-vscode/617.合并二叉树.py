#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#
# https://leetcode-cn.com/problems/merge-two-binary-trees/description/
#
# algorithms
# Easy (75.00%)
# Likes:    310
# Dislikes: 0
# Total Accepted:    37.5K
# Total Submissions: 49.9K
# Testcase Example:  '[1,3,2,5]\n[2,1,3,null,4,null,7]'
#
# 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
# 
# 你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL
# 的节点将直接作为新二叉树的节点。
# 
# 示例 1:
# 
# 
# 输入: 
# Tree 1                     Tree 2                  
# ⁠         1                         2                             
# ⁠        / \                       / \                            
# ⁠       3   2                     1   3                        
# ⁠      /                           \   \                      
# ⁠     5                             4   7                  
# 输出: 
# 合并后的树:
# 3
# / \
# 4   5
# / \   \ 
# 5   4   7
# 
# 
# 注意: 合并必须从两个树的根节点开始。
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
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:return t2 
        if not t2:return t1
        def dfs(r1, r2):
            if not r1 and not r2:return None
            if not r1:return r2
            if not r2:return r1 
            r1.val += r2.val
            r1.left = dfs(r1.left, r2.left)
            r1.right = dfs(r1.right, r2.right)
            return r1
        dfs(t1, t2)
        return t1
# @lc code=end


t1 = TreeNode(1)
t2 = TreeNode(3)
t3 = TreeNode(2)
t4 = TreeNode(5)
root1 = t1
root1.left = t2
root1.right = t3
t2.left = t4

t1 = TreeNode(2)
t2 = TreeNode(1)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(7)
root2 = t1
root2.left = t2
root2.right = t3
t2.right = t4
t3.right = t5

o = Solution()
# print(o.levelOrder(t))
t = o.mergeTrees(root1,root2)
# print(o.levelOrder(t))