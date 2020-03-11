#
# @lc app=leetcode.cn id=872 lang=python3
#
# [872] 叶子相似的树
#
# https://leetcode-cn.com/problems/leaf-similar-trees/description/
#
# algorithms
# Easy (62.23%)
# Likes:    49
# Dislikes: 0
# Total Accepted:    9.7K
# Total Submissions: 15.5K
# Testcase Example:  '[3,5,1,6,2,9,8,null,null,7,4]\n' +
#  '[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]'
#
# 请考虑一颗二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
# 
# 
# 
# 举个例子，如上图所示，给定一颗叶值序列为 (6, 7, 4, 9, 8) 的树。
# 
# 如果有两颗二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。
# 
# 如果给定的两个头结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。
# 
# 
# 
# 提示：
# 
# 
# 给定的两颗树可能会有 1 到 100 个结点。
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
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(root,re):
            if not root :return None
            if not root.left and not root.right:
              re.append(root.val)
            dfs(root.left,re)
            dfs(root.right,re)
            return re
        r1=dfs(root1,[])
        r2=dfs(root2,[])
        return r1==r2
        
# @lc code=end
#     2
#   2  5
# 5  7
t1 = TreeNode(2)
t2 = TreeNode(2)
t3 = TreeNode(5)
t4 = TreeNode(5)
t5 = TreeNode(7)
root = t1
root.left = t2
root.right = t3
t2.left = t4
t2.right = t5
o = Solution()
print(o.leafSimilar(root,root))