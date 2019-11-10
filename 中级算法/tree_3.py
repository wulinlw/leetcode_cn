#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/32/trees-and-graphs/87/
# 从前序与中序遍历序列构造二叉树
# 根据一棵树的前序遍历与中序遍历构造二叉树。

# 注意:
# 你可以假设树中没有重复的元素。

# 例如，给出

# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 返回如下的二叉树：

#     3
#    / \
#   9  20
#     /  \
#    15   7

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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 首先我们都知道先序遍历的递归定义是 根-左-右，中序遍历的定义为 左-中-右。
        # 首先根据前序遍历的定义可以知道，preorder这个数组的第一个元素preorder[0]一定是root，
        # 再根据中序遍历的定义， 在inorder这个数组里，root前面的元素都属于root的左子树，root后面的元素都属于右子树，从这一步得到了left_inorder和right_inorder，
        # 接下来我们只需要把root在inorder里的位置index = inorder.index(preorder[0])查找出来，就可以知道其左子树和右子树的长度，
        # 然后再回到preorder，root后面先是左子树，然后是右子树，因为上一步我们已经知道了它们的长度，所以可以得到left_preorder和left_preorder，
        # 然后递归不就完事了。

        if inorder==[]:
            return None
        root = TreeNode(preorder[0])        
        left_inorder = inorder[: inorder.index(root.val)]
        right_inorder = inorder[inorder.index(root.val) + 1 :]
        
        l_left = len(left_inorder)
        left_preorder = preorder[1:l_left + 1]
        right_preorder = preorder[l_left + 1 :]
        
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        
        return root



preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
b = B_Tree()
# b.build(treeList)
b.preTraverse(b.root)
print("\n")

s = Solution()
head1 = s.buildTree(preorder,inorder)
b.preTraverse(head1)
print(head1)