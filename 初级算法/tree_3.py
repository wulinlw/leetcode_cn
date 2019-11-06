#!/usr/bin/python
#coding:utf-8

# 对称二叉树
# 给定一个二叉树，检查它是否是镜像对称的。
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 给定一个二叉树，检查它是否是镜像对称的。
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

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
    # 将根节点的左右节点假设成两颗独立的树 
    # 递归调用时，因是对称，所以是左树左节点与右树右节点，左树右节点与右树左节点
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return True
        return self.recursiveTree(root.left, root.right)

    def recursiveTree(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val == right.val:
            return self.recursiveTree(left.left, right.right) and self.recursiveTree(left.right, right.left)
        return False



treeList = [3,9,20,None,None,15,7]
b = B_Tree()
b.build(treeList)
# b.preTraverse(b.root)
# b.midTraverse(b.root)
# b.afterTraverse(b.root)


s = Solution()
deep = s.isSymmetric(b.root)
print("deep:",deep)






