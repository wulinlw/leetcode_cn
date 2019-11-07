#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/7/trees/51/
# 将有序数组转换为二叉搜索树
# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
# 示例:
# 给定有序数组: [-10,-3,0,5,9],
# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
#       0
#      / \
#    -3   9
#    /   /
#  -10  5

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
    def sortedArrayToBST(self, nums):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 因为给定的数组是按照升序排列的，
        # 所以可以先取出数组中间位置的值作为二叉查找树的根结点，
        # 然后以该数组中间位置的值为中心，将左边的数组划分到根结点的左子树中，右边的数组划分到根结点的右子树中，
        # 这样就能保证根结点的左子树上任意结点的值都小于根结点的值，右子树上任意结点的值大于根节点的值。
        # 接下来，可以使用递归地方法继续取出左边数组的中间值作为根结点的左子结点，右边数组的中间值作为根结点的右子结点，
        # 然后以左边数组中间值为中心，再次划分左右子树，右边数组同理，如此递归下去，
        # 对于每个结点，总是能保证其左子树上任意结点的值都要小于该节点的值，其右子树上任意结点的值都要大于该节点的值
        length = len(nums)
        if not nums:
            return None
        mid = length//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root




# treeList = [3,9,20,None,None,15,7]
treeList = [-10,-3,0,5,9]
b = B_Tree()
# b.build(treeList)
# b.preTraverse(b.root)
# b.midTraverse(b.root)
# b.afterTraverse(b.root)


s = Solution()
deep = s.sortedArrayToBST(treeList)
# print("deep:",deep)
b.preTraverse(deep)






