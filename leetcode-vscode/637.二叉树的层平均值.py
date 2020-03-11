#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#
# https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/description/
#
# algorithms
# Easy (63.16%)
# Likes:    98
# Dislikes: 0
# Total Accepted:    14.5K
# Total Submissions: 22.9K
# Testcase Example:  '[3,9,20,15,7]'
#
# 给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.
# 
# 示例 1:
# 
# 输入:
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 输出: [3, 14.5, 11]
# 解释:
# 第0层的平均值是 3,  第1层是 14.5, 第2层是 11. 因此返回 [3, 14.5, 11].
# 
# 
# 注意：
# 
# 
# 节点值的范围在32位有符号整数范围内。
# 
# 
#
from typing import List
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:return []
        stack = [root]
        re = []
        while stack:
            cursum, cnt = 0,0
            for _ in range(len(stack)):
                n = stack.pop(0)
                cursum += n.val
                cnt += 1
                if n.left:
                    stack.append(n.left)
                if n.right:
                    stack.append(n.right)
            re.append(cursum/cnt)
        return re
# @lc code=end

#   1
#  2  3
# 4 5
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)

root = t1
root.left = t2
root.right = t3
t2.left = t4
t2.right = t5
o = Solution()
# print(o.levelOrder(t))
print(o.averageOfLevels(root))