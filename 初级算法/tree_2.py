#!/usr/bin/python
#coding:utf-8

# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
# 假设一个二叉搜索树具有如下特征：

# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。

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
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 中序遍历。 合法的BST中序遍历必为有序序列，
        # 如果非法，则便利结果会出现相邻的逆序对。
        def inorderTraversal(root): 
            if root == None:
                return []
            res = []
            res += inorderTraversal(root.left)
            res.append(root.val)
            res += inorderTraversal(root.right)
            return res
 
        res = inorderTraversal(root)
        if res != sorted(list(set(res))): return False
        return True

    
    # 第二种方法
    # 递归判断左右子树。需要用出现过的最大、最小值来判断；
    def validBST(self,root,small,large):
        if root == None:
            return True
        if small >= root.val or large <= root.val:
            return False  
        return self.validBST(root.left, small, root.val) and self.validBST(root.right, root.val, large)      
        
    def isValidBST2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.validBST(root, -2**32, 2**32-1)





treeList = [3,9,20,None,None,15,7]#false
treeList = [5,1,4,None,None,3,6]#false
# treeList = [2,1,3]#true
b = B_Tree()
b.build(treeList)
# b.preTraverse(b.root)
b.midTraverse(b.root)
# b.afterTraverse(b.root)

s = Solution()
deep = s.isValidBST(b.root)
print("deep:",deep)






