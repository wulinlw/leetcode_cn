#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (64.30%)
# Likes:    470
# Dislikes: 0
# Total Accepted:    72.4K
# Total Submissions: 109K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# 根据一棵树的前序遍历与中序遍历构造二叉树。
# 
# 注意:
# 你可以假设树中没有重复的元素。
# 
# 例如，给出
# 
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 
# 返回如下的二叉树：
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder == []: return None
        rootval = preorder[0]
        rootIndex = inorder.index(rootval)
        in_left = inorder[:rootIndex]
        in_right = inorder[rootIndex+1:]

        pre_left = preorder[1:rootIndex+1]
        pre_right = preorder[rootIndex+1:]
        root = TreeNode(rootval)
        root.left = self.buildTree(pre_left, in_left)
        root.right = self.buildTree(pre_right, in_right)
        return root

    # 层次遍历
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 从根开始遍历，每层写入一个新数组
        # 在将left ,right写入下次需要巡皇的数组
        # 循环完成即可得到每层的数组
        queue = [root]
        res = []
        if not root:
            return []
        while queue:
            templist = []#此层的数组
            templen =len(queue)
            for i in range(templen):                
                temp = queue.pop(0)
                templist.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            # print(templist)
            res.append(templist)
        return res


# @lc code=end
#打开TreeNode定义提交有问题
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
o = Solution()
root = o.buildTree(preorder, inorder)
r = o.levelOrder(root)
print(r)