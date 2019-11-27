#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/65/basic-operations-in-a-bst/174/
# Search in a Binary Search Tree
# 给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。

# 例如，
# 给定二叉搜索树:

#         4
#        / \
#       2   7
#      / \
#     1   3

# 和值: 2
# 你应该返回如下子树:

#       2     
#      / \   
#     1   3
# 在上述示例中，如果要找的值是 5，但因为没有节点值为 5，我们应该返回 NULL。

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
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root: return None
        while root: 
            if root.val<val: 
                root = root.right
            elif root.val>val:
                root = root.left
            else:
                return root
        return None

treeList = [4,2,7,1,3]
b = B_Tree()
b.build(treeList)
# b.preTraverse(b.root)
res = b.levelOrder(b.root)
print(res)

obj = Solution()
re = obj.searchBST(b.root, 4)
res = b.levelOrder(b.root)
print(res)