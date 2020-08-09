#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#
# https://leetcode-cn.com/problems/recover-binary-search-tree/description/
#
# algorithms
# Hard (57.19%)
# Likes:    271
# Dislikes: 0
# Total Accepted:    24.1K
# Total Submissions: 41.1K
# Testcase Example:  '[1,3,null,null,2]'
#
# 二叉搜索树中的两个节点被错误地交换。
# 
# 请在不改变其结构的情况下，恢复这棵树。
# 
# 示例 1:
# 
# 输入: [1,3,null,null,2]
# 
# 1
# /
# 3
# \
# 2
# 
# 输出: [3,1,null,null,2]
# 
# 3
# /
# 1
# \
# 2
# 
# 
# 示例 2:
# 
# 输入: [3,1,4,null,null,2]
# 
# ⁠ 3
# ⁠/ \
# 1   4
# /
# 2
# 
# 输出: [2,1,4,null,null,3]
# 
# ⁠ 2
# ⁠/ \
# 1   4
# /
# ⁠ 3
# 
# 进阶:
# 
# 
# 使用 O(n) 空间复杂度的解法很容易实现。
# 你能想出一个只使用常数空间的解决方案吗？
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.firstNode = None
        self.secondNode = None
        self.preNode = TreeNode(float("-inf"))

        def in_order(root):
            if not root:
                return
            in_order(root.left)
            if self.firstNode == None and self.preNode.val >= root.val:
                self.firstNode = self.preNode
            if self.firstNode and self.preNode.val >= root.val:
                self.secondNode = root
            self.preNode = root
            in_order(root.right)

        in_order(root)
        self.firstNode.val, self.secondNode.val = self.secondNode.val, self.firstNode.val

# 作者：powcai
# 链接：https://leetcode-cn.com/problems/recover-binary-search-tree/solution/zhong-xu-bian-li-by-powcai/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        
# @lc code=end

