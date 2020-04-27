#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#
# https://leetcode-cn.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (63.50%)
# Likes:    183
# Dislikes: 0
# Total Accepted:    29.1K
# Total Submissions: 45.4K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
# 
# 示例:
# 
# 输入: [1,2,3,null,5,null,4]
# 输出: [1, 3, 4]
# 解释:
# 
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
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
from typing import List
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:return []
        def dfs(root, level):           #level层数
            if not root:return
            if len(re) == level:        #层数==长度就添加，会先从右边添加，右边没有时就会选中左边了
                re.append(root.val)
            dfs(root.right, level + 1)  #先右后左，是一起往下走的
            dfs(root.left, level + 1)
        re = []
        dfs(root, 0)
        return re


# @lc code=end
#   1
#  2  3
#   5   4
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t5 = TreeNode(5)
t4 = TreeNode(4)

root = t1
root.left = t2
root.right = t3
t2.right = t5
t3.right = t4
o = Solution()
print(o.rightSideView(t1))