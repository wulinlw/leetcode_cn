#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
#
# https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree/description/
#
# algorithms
# Easy (45.43%)
# Likes:    61
# Dislikes: 0
# Total Accepted:    8.5K
# Total Submissions: 18.6K
# Testcase Example:  '[2,2,5,null,null,5,7]'
#
# 给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或
# 0。如果一个节点有两个子节点的话，那么这个节点的值不大于它的子节点的值。 
# 
# 给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。
# 
# 示例 1:
# 
# 
# 输入: 
# ⁠   2
# ⁠  / \
# ⁠ 2   5
# ⁠    / \
# ⁠   5   7
# 
# 输出: 5
# 说明: 最小的值是 2 ，第二小的值是 5 。
# 
# 
# 示例 2:
# 
# 
# 输入: 
# ⁠   2
# ⁠  / \
# ⁠ 2   2
# 
# 输出: -1
# 说明: 最小的值是 2, 但是不存在第二小的值。
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
    # 最小的是root
    # dfs查找，
    # 边界条件是
    #     1.到空节点还没发现比root大的，就是都相等，返回-1 
    #     2.找到立即返回
    # 左边都小于root，那就在右边有大于的
    # 右边都小于root，那就在左边有大于的
    # 左右都大于就返回较小的
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root: return -1 
        minval = root.val
        def dfs(root):
            nonlocal minval
            if not root :return -1
            if root.val>minval:
                return root.val
            l = dfs(root.left)
            r = dfs(root.right)
            if l<0:return r 
            if r<0:return l
            return min(l,r)
        return dfs(root)
# @lc code=end

t1 = TreeNode(2)
t2 = TreeNode(2)
t3 = TreeNode(5)
t4 = TreeNode(5)
t5 = TreeNode(7)
root = t1
root.left = t2
root.right = t3
t3.left = t4
t3.right = t5



o = Solution()
print(o.findSecondMinimumValue(root))