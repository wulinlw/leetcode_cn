#!/usr/bin/python
#coding:utf-8

# 重建二叉树
# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def reConstructBinaryTree(self, pre, inorder):
        if not pre and not inorder:
            return None
        
        rootIndex = inorder.index(pre[0])
        # 前序遍历的第一个元素是root
        # 从中序遍历中，找到root，然后就知道左边的是left长度，右边的是right长度
        # 前序遍历[root,left个元素，right个元素]
        pre_left = pre[1:rootIndex+1]   #
        pre_right = pre[rootIndex+1:]
    
        in_left = inorder[0:rootIndex]
        in_right = inorder[rootIndex+1:]
        root = TreeNode(pre[0])
        root.left = self.reConstructBinaryTree(pre_left, in_left)
        root.right = self.reConstructBinaryTree(pre_right, in_right)
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

        
preorder = [1,2,4,7,3,5,6,8]
inorder = [4,7,2,1,5,3,8,6]
obj = Solution()
root = obj.reConstructBinaryTree(preorder, inorder)
# print(root)
re = obj.levelOrder(root)
print(re)
