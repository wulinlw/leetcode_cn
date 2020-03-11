#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
#
# https://leetcode-cn.com/problems/binary-tree-tilt/description/
#
# algorithms
# Easy (53.09%)
# Likes:    54
# Dislikes: 0
# Total Accepted:    8.9K
# Total Submissions: 16.7K
# Testcase Example:  '[1,2,3]'
#
# 给定一个二叉树，计算整个树的坡度。
# 
# 一个树的节点的坡度定义即为，该节点左子树的结点之和和右子树结点之和的差的绝对值。空结点的的坡度是0。
# 
# 整个树的坡度就是其所有节点的坡度之和。
# 
# 示例:
# 
# 
# 输入: 
# ⁠        1
# ⁠      /   \
# ⁠     2     3
# 输出: 1
# 解释: 
# 结点的坡度 2 : 0
# 结点的坡度 3 : 0
# 结点的坡度 1 : |2-3| = 1
# 树的坡度 : 0 + 0 + 1 = 1
# 
# 
# 注意:
# 
# 
# 任何子树的结点的和不会超过32位整数的范围。
# 坡度的值不会超过32位整数的范围。
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
    def findTilt(self, root: TreeNode) -> int:
        if not root:return 0
        tilt=0
        def findTiltHelp(root):
            nonlocal tilt
            if not root:return 0
            l = findTiltHelp(root.left)
            r = findTiltHelp(root.right)
            tilt += abs(l-r)                #每个节点的坡度
            return l+r+root.val             #每个节点的左，根，右的和
        findTiltHelp(root)
        return tilt
# @lc code=end

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)

root = t1
root.left = t2
root.right = t3


o = Solution()
# print(o.levelOrder(t))
print(o.findTilt(root))