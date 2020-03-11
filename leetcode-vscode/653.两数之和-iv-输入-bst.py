#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#
# https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/description/
#
# algorithms
# Easy (54.00%)
# Likes:    116
# Dislikes: 0
# Total Accepted:    12.1K
# Total Submissions: 22.4K
# Testcase Example:  '[5,3,6,2,4,null,7]\n9'
#
# 给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
# 
# 案例 1:
# 
# 
# 输入: 
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
# 
# Target = 9
# 
# 输出: True
# 
# 
# 
# 
# 案例 2:
# 
# 
# 输入: 
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
# 
# Target = 28
# 
# 输出: False
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
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:return False
        m = {}
        def dfs(root):
            if not root:return
            if k-root.val in m:
                return True
            else:
                m[root.val] = 1
            l = dfs(root.left)
            r = dfs(root.right)
            return l or r
        return dfs(root)
        
# @lc code=end
t1 = TreeNode(5)
t2 = TreeNode(3)
t3 = TreeNode(6)
t4 = TreeNode(2)
t5 = TreeNode(4)
t6 = TreeNode(7)
root = t1
root.left = t2
root.right = t3
t2.left = t4
t2.right = t5
t3.right = t6


o = Solution()
print(o.findTarget(root, 9))
