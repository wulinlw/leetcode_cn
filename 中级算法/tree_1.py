#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/32/trees-and-graphs/85/
# 中序遍历二叉树
# 给定一个二叉树，返回它的中序 遍历。

# 示例:
# 输入: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# 输出: [1,3,2]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？

# https://blog.csdn.net/qq_17550379/article/details/80809930
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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
        根在最前
        从上到下，最左边的val，左、右
        '''
        if root==None:  
            return  
        print(root.val)  
        self.preTraverse(root.left)  
        self.preTraverse(root.right)  

    def midTraverse(self, root): 
        '''
        中序遍历
        根在中间
        最左边的从左、val、右，...根...最右边的从左、val、右
        '''
        if root==None:  
            return  
        self.midTraverse(root.left)  
        print(root.val)  
        self.midTraverse(root.right)  

    def afterTraverse(self, root):  
        '''
        后序遍历
        根在最后
        最左边的左、右，val,依次排列，最后是根
        '''
        if root==None:  
            return  
        self.afterTraverse(root.left)  
        self.afterTraverse(root.right)  
        print(root.val)

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = list()
        if root == None:
            return result
        
        stack = list()
        while stack or root:
            if root != None:
                stack.append(root)#根放入栈中
                root = root.left#左值赋值给root，用于下次循环，直到最左边的一个（最下面的左值）
            else:
                root = stack.pop()#弹出栈顶元素
                result.append(root.val)
                root = root.right#left完了继续处理right

        return result


treeList = [3,9,20,None,None,15,7]
b = B_Tree()
b.build(treeList)
b.preTraverse(b.root)
print("\n")
b.midTraverse(b.root)
print("\n")
b.afterTraverse(b.root)
print("\n")
s = Solution()
head1 = s.inorderTraversal(b.root)
print(head1)






