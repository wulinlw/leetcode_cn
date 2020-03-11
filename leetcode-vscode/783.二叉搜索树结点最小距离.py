#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树结点最小距离
#
# https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/description/
#
# algorithms
# Easy (51.79%)
# Likes:    47
# Dislikes: 0
# Total Accepted:    9.5K
# Total Submissions: 18.2K
# Testcase Example:  '[4,2,6,1,3,null,null]'
#
# 给定一个二叉搜索树的根结点 root，返回树中任意两节点的差的最小值。
# 
# 
# 
# 示例：
# 
# 输入: root = [4,2,6,1,3,null,null]
# 输出: 1
# 解释:
# 注意，root是树结点对象(TreeNode object)，而不是数组。
# 
# 给定的树 [4,2,6,1,3,null,null] 可表示为下图:
# 
# ⁠         4
# ⁠       /   \
# ⁠     2      6
# ⁠    / \    
# ⁠   1   3  
# 
# 最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。
# 
# 
# 
# 注意：
# 
# 
# 二叉树的大小范围在 2 到 100。
# 二叉树总是有效的，每个节点的值都是整数，且不重复。
# 本题与 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/
# 相同
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
    def minDiffInBST(self, root: TreeNode) -> int:
        if not root:return 0
        minval = 0x7FFFFFF
        pre = None
        def dfs(root):
            nonlocal pre,minval
            if not root:return
            dfs(root.left)
            if pre:
                minval = min(minval, abs(root.val-pre.val))
            pre = root
            dfs(root.right)
        dfs(root)
        return minval
# @lc code=end
t1 = TreeNode(4)
t2 = TreeNode(2)
t3 = TreeNode(6)
t4 = TreeNode(1)
t5 = TreeNode(3)
root = t1
root.left = t2
root.right = t3
t2.left = t4
t2.right = t5


o = Solution()
print(o.minDiffInBST(root))
