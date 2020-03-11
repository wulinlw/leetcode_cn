#
# @lc app=leetcode.cn id=993 lang=python3
#
# [993] 二叉树的堂兄弟节点
#
# https://leetcode-cn.com/problems/cousins-in-binary-tree/description/
#
# algorithms
# Easy (50.31%)
# Likes:    47
# Dislikes: 0
# Total Accepted:    6.3K
# Total Submissions: 12.5K
# Testcase Example:  '[1,2,3,4]\n4\n3'
#
# 在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。
# 
# 如果二叉树的两个节点深度相同，但父节点不同，则它们是一对堂兄弟节点。
# 
# 我们给出了具有唯一值的二叉树的根节点 root，以及树中两个不同节点的值 x 和 y。
# 
# 只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true。否则，返回 false。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,2,3,4], x = 4, y = 3
# 输出：false
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
# 输出：true
# 
# 
# 示例 3：
# 
# 
# 
# 输入：root = [1,2,3,null,4], x = 2, y = 3
# 输出：false
# 
# 
# 
# 提示：
# 
# 
# 二叉树的节点数介于 2 到 100 之间。
# 每个节点的值都是唯一的、范围为 1 到 100 的整数。
# 
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
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:return False
        parents = {}    #父节点
        depths = {}     #层级
        def dfs(root, parent):
            if not root:return
            depths[root.val] = 1+depths[parent.val] if parent else 0 #记录深度
            parents[root.val] = parent                               #记录父节点
            dfs(root.left, root)
            dfs(root.right, root)
        dfs(root,None)
        return depths[x]==depths[y] and parents[x]!=parents[y]
        
# @lc code=end

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
root = t1
root.left = t2
root.right = t3
t2.left = t4


o = Solution()
print(o.isCousins(root,4,2))