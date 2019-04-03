#!/usr/bin/python
#coding:utf-8

# 给定一个二叉树，找出其最大深度。
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 说明: 叶子节点是指没有子节点的节点。

# 用Python实现二叉树、二叉树非递归遍历及绘制
# https://blog.csdn.net/huang_shiyang/article/details/79981332
# python 数据结构 二叉树
# https://www.jianshu.com/p/b09a6b6c2f4b

# Definition for a binary tree node.
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


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0 
        else:
            return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))



treeList = [3,9,20,None,None,15,7]
b = B_Tree()
b.build(treeList)
b.preTraverse(b.root)

s = Solution()
deep = s.maxDepth(b.root)
print("deep:",deep)






