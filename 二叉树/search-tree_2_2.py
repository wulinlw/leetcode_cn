#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/65/basic-operations-in-a-bst/177/
# Insert into a Binary Search Tree
# 给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 保证原始二叉搜索树中不存在新值。
# 注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回任意有效的结果。

# 例如, 
# 给定二叉搜索树:

#         4
#        / \
#       2   7
#      / \
#     1   3

# 和 插入的值: 5
# 你可以返回这个二叉搜索树:

#          4
#        /   \
#       2     7
#      / \   /
#     1   3 5
# 或者这个树也是有效的:

#          5
#        /   \
#       2     7
#      / \   
#     1   3
#          \
#           4

class TreeNode(object):
    def __init__(self, x=None, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
        
class B_Tree(object):
    def __init__(self, node=None):
        self.root = node
        
    def add(self, item=None):
        #如果输入item是None 则表示一个空节点
        node = TreeNode(x=item)
        #如果是空树，则直接添到根
        #此时判断空的条件为，
        if not self.root or self.root.val is None:
            self.root = node
        else:
        #不为空，则按照 左右顺序 添加节点
            my_queue = []
            my_queue.append(self.root)
            while True:
                cur_node = my_queue.pop(0)
                #即如果该当前节点为空节点则直接跳过它，起到一个占位的作用
                if cur_node.val is None:
                    continue
                if not cur_node.left:
                    cur_node.left = node
                    return
                elif not cur_node.right:
                    cur_node.right = node
                    return
                else:
                    my_queue.append(cur_node.left)
                    my_queue.append(cur_node.right)

    def build(self, itemList):
        for i in itemList:
            self.add(i)
    
    def preTraverse(self, root):  
        '''
        前序遍历
        '''
        if root==None:  
            return  
        print(root.val)  
        self.preTraverse(root.left)  
        self.preTraverse(root.right)  

    def midTraverse(self, root): 
        '''
        中序遍历
        '''
        if root==None:  
            return  
        self.midTraverse(root.left)  
        print(root.val)  
        self.midTraverse(root.right)  

    def afterTraverse(self, root):  
        '''
        后序遍历
        '''
        if root==None:  
            return  
        self.afterTraverse(root.left)  
        self.afterTraverse(root.right)  
        print(root.val)

    def levelOrder(self, root):
        WHITE, GRAY = 0, 1
        stack = []
        init_level = 0
        stack.append((root, WHITE, init_level))
        result = []
        while stack:
            node, color, level = stack.pop()
            if node:
                if color == WHITE:
                    stack.append((node.right, WHITE, level+1))
                    stack.append((node.left, WHITE, level+1))
                    stack.append((node, GRAY, level))
                else:
                    if len(result) == level: result.append([])
                    result[level].append(node.val)
        return result

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # 遇到应该走向左子树而左子树为空，或者应该走向右子树而右子树为空时，
        # 就是找到了新字典项的插入位置，构造新结点并完成实际插入。
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val > val:
                if node.left:
                    stack.append(node.left)#存在时，需要继续往下遍历
                else:
                    node.left = TreeNode(val)#不存在时，直接放在这里
            else:
                if node.right:
                    stack.append(node.right)
                else:
                    node.right = TreeNode(val)
        return root


treeList = [4,2,7,1,3]
b = B_Tree()
b.build(treeList)
# b.preTraverse(b.root)
res = b.levelOrder(b.root)
print(res)

obj = Solution()
re = obj.insertIntoBST(b.root, 5)
res = b.levelOrder(b.root)
print(res)