#
# @lc app=leetcode.cn id=897 lang=python3
#
# [897] 递增顺序查找树
#
# https://leetcode-cn.com/problems/increasing-order-search-tree/description/
#
# algorithms
# Easy (65.76%)
# Likes:    58
# Dislikes: 0
# Total Accepted:    8K
# Total Submissions: 12.1K
# Testcase Example:  '[5,3,6,2,4,null,8,1,null,null,null,7,9]'
#
# 给定一个树，按中序遍历重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。
# 
# 
# 
# 示例 ：
# 
# 输入：[5,3,6,2,4,null,8,1,null,null,null,7,9]
# 
# ⁠      5
# ⁠     / \
# ⁠   3    6
# ⁠  / \    \
# ⁠ 2   4    8
# /        / \ 
# 1        7   9
# 
# 输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
# 
# ⁠1
# \
# 2
# \
# 3
# \
# 4
# \
# 5
# \
# 6
# \
# 7
# \
# 8
# \
# ⁠                9  
# 
# 
# 
# 提示：
# 
# 
# 给定树中的结点数介于 1 和 100 之间。
# 每个结点都有一个从 0 到 1000 范围内的唯一整数值。
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
    # 中序遍历 + 构造新的树
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:return None
        re = []
        def dfs(root):
            nonlocal re
            if not root:return None
            dfs(root.left)
            re.append(root.val)
            dfs(root.right)
            return root
        dfs(root)
        ans = p = TreeNode(0)
        for i in re:
            p.right = TreeNode(i)
            p = p.right
        return ans.right

    # 中序遍历 + 更改树的连接方式
    def increasingBST2(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right

# @lc code=end

t1 = TreeNode(5)
t2 = TreeNode(3)
t3 = TreeNode(6)
t4 = TreeNode(2)
t5 = TreeNode(4)
t6 = TreeNode(8)
root = t1
root.left = t2
root.right = t3
t2.left = t4
t2.right = t5
t3.right = t6
o = Solution()
t = o.increasingBST(root)
# print(o.increasingBST(root))
re = []
while t:
    re.append(t.val)
    t = t.right
print(re)