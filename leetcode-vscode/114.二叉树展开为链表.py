#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#
# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (67.68%)
# Likes:    281
# Dislikes: 0
# Total Accepted:    30.1K
# Total Submissions: 44.4K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# 给定一个二叉树，原地将它展开为链表。
# 
# 例如，给定二叉树
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   5
# ⁠/ \   \
# 3   4   6
# 
# 将其展开为：
# 
# 1
# ⁠\
# ⁠ 2
# ⁠  \
# ⁠   3
# ⁠    \
# ⁠     4
# ⁠      \
# ⁠       5
# ⁠        \
# ⁠         6
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
    # 我们采用后序遍历的方式，也就是 左节点-右节点-打印根节点 这个顺序遍历二叉树。
    # 当遍历到根节点后，我们对根节点的左右子树做一些调整。
    #     1
    #    / \
    #   2   3
    # 将右节点挂到左节点的最右边
    #     1
    #    / 
    #   2   
    #    \   
    #     3   
    # 再将整个左子树挂到根节点的右边，这样就可以将整棵树变成链表结构了。
    #     1
    #      \
    #       2
    #        \
    #         3
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre = None
        def dfs(root):
            nonlocal pre
            if not root:return None
            dfs(root.left)
            dfs(root.right)
            if root.left: # 后序遍历
                pre = root.left # 令 pre 指向左子树
                while pre.right: 
                    pre = pre.right # 找到左子树中的最右节点
                pre.right = root.right # 令左子树中的最右节点的右子树 指向 根节点的右子树
                root.right = root.left # 令根节点的右子树指向根节点的左子树
                root.left = None # 置空根节点的左子树
            root = root.right # 令当前节点指向下一个节点
        dfs(root)
        return pre
    
    # 前序遍历
    # 前序遍历是:打印根节点-左节点-右节点 这样的顺序，如果是:右节点-左节点-打印根节点 这样完全相反的顺序遍历呢？
    # 这样遍历完之后，正好跟前序遍历是相反的。
    # 前序遍历完是1,2,3,4,5,6，按照这种新的方式遍历其结果是:6,5,4,3,2,1。
    # 既然得到了反向的顺序，那么就可以把前后节点串联起来，当遍历到根节点1的时候，整个串联就完成了，二叉树就变成了链表。
    # null<-6<-5<-4<-3<-2<-1
    def flatten2(self, root):
        pre = None
        def dfs(root):
            nonlocal pre
            if not root:
                return None
            # 右节点-左节点-根节点 这种顺序正好跟前序遍历相反
            # 用pre节点作为媒介，将遍历到的节点前后串联起来
            dfs(root.right)
            dfs(root.left)
            root.left = None
            root.right = pre
            pre = root
        dfs(root)
        return pre
    
    # 与下面这题类似 二叉搜索树转链表
    # 面试题 17.12. BiNode 
    # https://leetcode-cn.com/problems/binode-lcci/

    # 897.递增顺序查找树
    # 也是二叉搜索树转链表
    # https://leetcode-cn.com/problems/increasing-order-search-tree/description/



# @lc code=end


#     1
#   2  5
#  3 4  6
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(5)
t4 = TreeNode(3)
t5 = TreeNode(4)
t6 = TreeNode(6)
root = t1
root.left = t2
root.right = t3
t2.left = t4
t2.right = t5
t3.right = t6

o = Solution()
# print(o.levelOrder(t))
o.flatten(root)
re = []
while root:
    re.append(root.val)
    root = root.right
print(re)