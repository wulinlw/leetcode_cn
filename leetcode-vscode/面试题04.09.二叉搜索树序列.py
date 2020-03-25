#!/usr/bin/python
#coding:utf-8


# 面试题 04.09. 二叉搜索树序列
# 从左向右遍历一个数组，通过不断将其中的元素插入树中可以逐步地生成一棵二叉搜索树。给定一个由不同节点组成的二叉树，输出所有可能生成此树的数组。

# 示例:
# 给定如下二叉树

#         2
#        / \
#       1   3
# 返回:

# [
#    [2,1,3],
#    [2,3,1]
# ]
# https://leetcode-cn.com/problems/bst-sequences-lcci/
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # https://leetcode-cn.com/problems/bst-sequences-lcci/solution/15xing-dai-ma-by-suibianfahui/
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return [[]]
        res = []
        def findPath(cur, q, path):
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            if not q:
                res.append(path)
                return
            for i, nex in enumerate(q): 
                newq = q[:i] + q[i + 1:]
                findPath(nex, newq, path + [nex.val])
        findPath(root, [], [root.val])
        return res

t1 = TreeNode(2)
t2 = TreeNode(1)
t3 = TreeNode(3)
t1.left = t2
t1.right = t3
o = Solution()
print(o.BSTSequences(t1))