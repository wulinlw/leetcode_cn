#!/usr/bin/python
#coding:utf-8

# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
# 例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]
# 示例 1:

# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
# 示例 2:

# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
#  
# 说明:
# 所有节点的值都是唯一的。
# p、q 为不同节点且均存在于给定的二叉树中。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 由于lowestCommonAncestor(root, p, q)的功能是找出以root为根节点的两个节点p和q的最近公共祖先。 我们考虑：
    # 如果p和q分别是root的左右节点，那么root就是我们要找的最近公共祖先
    # 如果root是None，说明我们在这条寻址线路没有找到，我们返回None表示没找到
    # 我们继续在左右子树执行相同的逻辑。
    # 如果左子树没找到，说明在右子树，我们返回lowestCommonAncestor(root.right, p , q)
    # 如果右子树没找到，说明在左子树，我们返回lowestCommonAncestor(root.left, p , q)
    # 如果左子树和右子树分别找到一个，我们返回root
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:return None
        if root.val == p.val or root.val == q.val: return root
        l = self.lowestCommonAncestor(root.left,  p , q)
        r = self.lowestCommonAncestor(root.right,  p , q)
        if l and r:
            return root
        else:
            return l or r



# 测试树
#        6
#    2     8
#  1  4   7 9                
t1 = TreeNode(1)
t2 = TreeNode(2)
t4 = TreeNode(4)
t6 = TreeNode(6)
t7 = TreeNode(7)
t8 = TreeNode(8)
t9 = TreeNode(9)

root = t6
root.left = t2
root.right = t8
t2.left = t1
t2.right = t4
t8.left = t7
t8.right = t9

S = Solution()
print(S.lowestCommonAncestor(root, t1,t4).val)

