#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
#
# https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/description/
#
# algorithms
# Easy (72.21%)
# Likes:    66
# Dislikes: 0
# Total Accepted:    19.7K
# Total Submissions: 27.2K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# 给定一个 N 叉树，返回其节点值的前序遍历。
# 
# 例如，给定一个 3叉树 :
# 
# 
# 
# 
# 
# 
# 
# 返回其前序遍历: [1,3,5,6,2,4]。
# 
# 
# 
# 说明: 递归法很简单，你可以使用迭代法完成此题吗?
#
from typing import List
# @lc code=start
""""""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder222(self, root: 'Node') -> List[int]:
        if not root:return []
        stack = [root,]
        re = []
        while stack:
            n = stack.pop(0)
            re.append(n.val)
            stack.extend(n.children)  #extend,为空时不会加进入
        return re
    
    def preorder(self, root: 'Node') -> List[int]:
        re = []
        def dfs(root):
            if not root:return
            re.append(root.val)
            if len(root.children)>0:
                for i in root.children:
                    dfs(i)

        dfs(root)
        return re


        
# @lc code=end

t1 = Node(1,[])
t2 = Node(3,[])
t3 = Node(2,[])
t4 = Node(4,[])
t5 = Node(5,[])
t6 = Node(6,[])
root = t1
root.children.extend([t2,t3,t4])
t2.children.extend([t5,t6])

o = Solution()
print(o.preorder222(root))