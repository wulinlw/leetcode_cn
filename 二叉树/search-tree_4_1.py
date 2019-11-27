#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/67/appendix-height-balanced-bst/188/
# 平衡二叉树
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 本题中，一棵高度平衡二叉树定义为：
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

# 示例 1:
# 给定二叉树 [3,9,20,null,null,15,7]

#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回 true 。

# 示例 2:
# 给定二叉树 [1,2,2,3,3,null,null,4,4]

#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# 返回 false 。
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
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 自底向上递归O(N)
        # 递归确实光想不手动推导下难以理解，建议你把题目描述的两个例子手动推导一下就能更好理解了。
        # 1.递归到最深处返回0，因为叶子节点的左右节点是空呀；此时max(left,right)=0 ,left和right表达式中的+1就是为了计数的，把叶子 节点这一层加上了
        # 2.想象所有递归到最后第一步返回值都是1，然后往上一层想，叶子节点的父节点也会得到{max（left，right）+1} 的返回值，其实return表达式可以+1来替换left和right表达式中的+1
        # 3.递归的往上统计树的高度
        # 4.题目中的self.res = False 我觉得可以更有效的利用一下，出现这种情况基本不用再递归往上count了，不必要的计算。我还没想好怎么改，不过下一个精选题解的解决方案不错。
        self.res = True
        def helper(root):
            if not root:
                return 0
            left = helper(root.left) + 1
            right = helper(root.right) + 1
            #print(right, left)
            if abs(right - left) > 1: 
                self.res = False
            return max(left, right)
        helper(root)
        return self.res




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
 