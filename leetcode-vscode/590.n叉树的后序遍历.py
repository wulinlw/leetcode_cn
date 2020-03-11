#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
#
# https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/description/
#
# algorithms
# Easy (72.10%)
# Likes:    55
# Dislikes: 0
# Total Accepted:    17.3K
# Total Submissions: 23.8K
# Testcase Example:  '[1,null,3,2,4,null,5,6]\r'
#
# 给定一个 N 叉树，返回其节点值的后序遍历。
# 
# 例如，给定一个 3叉树 :
# 
# 
# 
# 
# 
# 
# 
# 返回其后序遍历: [5,6,3,2,4,1].
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
    def postorder222(self, root: 'Node') -> List[int]:
        if not root:return []
        stack = [root,]
        re = []
        while stack:
            n = stack.pop()
            re.append(n.val)
            stack.extend(n.children)  #extend,为空时不会加进入
        return re[::-1]
    
    def postorder(self, root: 'Node') -> List[int]:
        re = []
        def dfs(root):
            if not root:return
            if len(root.children)>0:
                for i in root.children:
                    dfs(i)
            re.append(root.val)
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
print(o.postorder222(root))