#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/65/basic-operations-in-a-bst/180/
# Delete Node in a BST
# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

# 一般来说，删除节点可分为两个步骤：
# 首先找到需要删除的节点；
# 如果找到了，删除它。
# 说明： 要求算法时间复杂度为 O(h)，h 为树的高度。

# 示例:
# root = [5,3,6,2,4,null,7]
# key = 3

#     5
#    / \
#   3   6
#  / \   \
# 2   4   7

# 给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
# 一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。

#     5
#    / \
#   4   6
#  /     \
# 2       7

# 另一个正确答案是 [5,2,6,null,4,null,7]。

#     5
#    / \
#   2   6
#    \   \
#     4   7
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
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        # 1. 如果目标节点没有子节点，我们可以直接移除该目标节点。
        # 2. 如果目标节只有一个子节点，我们可以用其子节点作为替换。
        # 3. 如果目标节点有两个子节点，我们需要用其中序后继节点或者前驱节点来替换，再删除该目标节点。
        par = None#用于存储当前遍历节点的父节点
        p = root
        while p:
            if key < p.val:#小于当前往左找
                par = p
                p = p.left
            elif key > p.val:#大于当前往右找
                par = p
                p = p.right
            else:#找到了要删除节点
                if p.left is None and p.right is None:#没有子节点
                    if par is None:#要删的是根，返回none
                        root = None
                    else:
                        if key < par.val:#判断要删的在父节点的左还是右，然后删掉对应的节点
                            par.left = None
                        else:
                            par.right = None
                elif p.left is None:#没有左节点
                    if par is None:#root没有左节点
                        root = p.right
                    else:
                        if key < par.val:#直接用右节点替代
                            par.left = p.right
                        else:
                            par.right = p.right
                else:#有左节点
                    # 这个情况下，需要找删除节点的左节点中最大值，（这里解答用的这种）
                    # 或者右节点中的最小值
                    r = p.left
                    while r.right is not None:#找到左子树的最右节点
                        r = r.right
                    if par is None:#如果要删的是root
                        root = p.left
                        r.right = p.right
                    else:
                        if key < par.val:
                            par.left = p.left
                            r.right = p.right
                        else:
                            par.right = p.left
                            r.right = p.right
                return root
                                                    
        return root



treeList = [4,2,7,1,3]
b = B_Tree()
b.build(treeList)
# b.preTraverse(b.root)
res = b.levelOrder(b.root)
print(res)

obj = Solution()
re = obj.deleteNode(b.root, 5)
res = b.levelOrder(b.root)
print(res)
 