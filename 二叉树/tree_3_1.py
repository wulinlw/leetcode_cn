#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/learn/card/data-structure-binary-tree/4/conclusion/15/
# 从中序与后序遍历序列构造二叉树
# 根据一棵树的中序遍历与后序遍历构造二叉树。

# 注意:
# 你可以假设树中没有重复的元素。

# 例如，给出
# 中序遍历 inorder = [9,3,15,20,7]
# 后序遍历 postorder = [9,15,7,20,3]
# 返回如下的二叉树：

#     3
#    / \
#   9  20
#     /  \
#    15   7

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            # 这里要返回结点，而不是返回具体的数
            return TreeNode(inorder[0])
        # 后序遍历的最后一个结点就是根结点
        root = TreeNode(postorder[-1])
        # 在中序遍历中找到根结点的索引，得到左右子树的一个划分
        pos = inorder.index(postorder[-1])
        # 这里的列表切片使用的是复制值，使用了一些空间，因此空间复杂度是 O(N)
        root.left = self.buildTree(inorder[:pos], postorder[:pos])
        root.right = self.buildTree(inorder[pos + 1:], postorder[pos:-1])
        return root

    def buildTree2(self, inorder, postorder) :
        size = len(inorder)

        self.inorder = inorder
        self.postorder = postorder
        return self.__dfs(0, size - 1, 0, size - 1)

    # 在递归方法中，有一个数组的边界索引，得通过计算得到，
    # 计算的依据是递归方法传入的“中序遍历数组”（的子数组）和“后序遍历数组”（的子数组）的长度是一样的。
    # 我的办法是解方程计算未知数。
    # 具体需要计算哪个参数我在下面的代码中已经注明了。
    def __dfs(self, in_l, in_r, post_l, post_r):
        if in_l > in_r or post_l > post_r:
            return None

        val = self.postorder[post_r]
        # 后序遍历的最后一个结点就是根结点
        root = TreeNode(val)
        # 在中序遍历中找到根结点的索引，得到左右子树的一个划分
        pos = self.inorder.index(val)

        # 注意：第 4 个参数是计算出来的，依据：两边区间长度相等
        root.left = self.__dfs(in_l, pos - 1, post_l, pos - 1 - in_l + post_l)
        # 注意：第 3 个参数是计算出来的，依据：两边区间长度相等
        root.right = self.__dfs(pos + 1, in_r, post_r - in_r + pos, post_r - 1)
        return root



nums = [7,2,5,10,8]
m = 2
ss = Solution()
re = ss.splitArray(nums,m)
print(re)

