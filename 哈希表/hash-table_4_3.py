#!/usr/bin/python
# coding:utf-8


# https://leetcode-cn.com/explore/learn/card/hash-table/206/practical-application-design-the-key/823/
# 寻找重复的子树
# 给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。
# 两棵树重复是指它们具有相同的结构以及相同的结点值。

# 示例 1：
#         1
#        / \
#       2   3
#      /   / \
#     4   2   4
#        /
#       4
# 下面是两个重复的子树：

#       2
#      /
#     4
# 和

#     4
# 因此，你需要以列表的形式返回上述重复子树的根结点。


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

import collections
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        d = collections.defaultdict(list)
        def dfs(root):
            if not root: return ''
            s = ' '.join((str(root.val), dfs(root.left), dfs(root.right))) #hash算法
            d[s].append(root)
            return s
        dfs(root)
        # return [l[0] for l in d.values() if len(l) > 1]
        res = []
        for l in d.values():
            if len(l) > 1:
                res.append(l[0])
        return res



list1 = [1,2,3,4,2,4,None,4]
t = B_Tree()
t.build(list1)
obj = Solution()
res = obj.findDuplicateSubtrees(t.root)
print(res[0].val)
