#!/usr/bin/python
#coding:utf-8
import sys

class TreeNode(object):
    def __init__(self, x=None, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class B_Tree(object):
    def __init__(self, node=None):
        self.root = node
        self.treelist = []
        
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
        self.treelist.append(root.val)  
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
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 0
        for i in nums:
            # idx < 2的情况是前2个值，跳过即可
            # 当前值不喝上上个相等，idx就可以想下走一步
            if idx < 2 or i != nums[idx - 2]:
                nums[idx] = i
                idx += 1

        return idx

        


nums = [1,1,1,2,2,3]
s = Solution()
deep = s.removeDuplicates(nums)
print("deep:",deep)
