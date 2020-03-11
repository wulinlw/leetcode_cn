#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#
# https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (55.67%)
# Likes:    91
# Dislikes: 0
# Total Accepted:    10.5K
# Total Submissions: 18.9K
# Testcase Example:  '[1,null,3,2]'
#
# 给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。
# 
# 
# 
# 示例：
# 
# 输入：
# 
# ⁠  1
# ⁠   \
# ⁠    3
# ⁠   /
# ⁠  2
# 
# 输出：
# 1
# 
# 解释：
# 最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
# 
# 
# 
# 
# 提示：
# 
# 
# 树中至少有 2 个节点。
# 本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/
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
    # 中序遍历
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root:return 0 
        pre = None
        minval = 0x7FFFFFF
        def dfs(root):
            nonlocal pre,minval
            if not root:return
            dfs(root.left)
            if pre:
                minval = min(abs(root.val-pre.val), minval)
            pre = root              #记录前一个节点
            dfs(root.right)
        dfs(root)
        return(minval)
# @lc code=end

t1 = TreeNode(1)
t2 = TreeNode(3)
t3 = TreeNode(2)

root = t1
root.right = t2
t2.left = t3


o = Solution()
# print(o.levelOrder(root))
print(o.getMinimumDifference(root))