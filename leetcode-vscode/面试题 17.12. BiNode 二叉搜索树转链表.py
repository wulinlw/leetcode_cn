#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/problems/binode-lcci/
# 二叉树数据结构TreeNode可用来表示单向链表（其中left置空，right为下一个链表节点）。实现一个方法，把二叉搜索树转换为单向链表，要求值的顺序保持不变，转换操作应是原址的，也就是在原始的二叉搜索树上直接修改。
# 返回转换后的单向链表的头节点。
# 注意：本题相对原题稍作改动
#  
# 示例：
# 输入： [4,2,5,1,3,null,6,0]
# 输出： [0,null,1,null,2,null,3,null,4,null,5,null,6]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # [114] 二叉树展开为链表
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        p = pre = None
        def dfs(root):                  #中序遍历
            nonlocal pre,p
            if not root:return None
            dfs(root.left)
            root.left = None
            if pre:
                pre.right = root        #设置下一个节点
            else:
                p = root                #第一个节点head
            pre = root
            dfs(root.right)
        
        dfs(root)
        return p


#     4
#   2  5
#  1 3  6
# 0
# [4,2,5,1,3,null,6,0]
t1 = TreeNode(4)
t2 = TreeNode(2)
t3 = TreeNode(5)
t4 = TreeNode(1)
t5 = TreeNode(3)
t6 = TreeNode(6)
t7 = TreeNode(0)
root = t1
root.left = t2
root.right = t3
t2.left = t4
t2.right = t5
t3.right = t6
t4.left = t7

o = Solution()
# print(o.findSecondMinimumValue(root))
# print(o.levelOrder(t))
t = o.convertBiNode(root)
re = []
while t:
    re.append(t.val)
    t = t.right
print(re)