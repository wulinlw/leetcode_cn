#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#
# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/description/
#
# algorithms
# Medium (45.16%)
# Likes:    134
# Dislikes: 0
# Total Accepted:    18.4K
# Total Submissions: 38.7K
# Testcase Example:  '[1,2,3,4,5,null,7]'
#
# 给定一个二叉树
# 
# struct Node {
# ⁠ int val;
# ⁠ Node *left;
# ⁠ Node *right;
# ⁠ Node *next;
# }
# 
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
# 
# 初始状态下，所有 next 指针都被设置为 NULL。
# 
# 
# 
# 进阶：
# 
# 
# 你只能使用常量级额外空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
# 
# 
# 
# 
# 示例：
# 
# 
# 
# 输入：root = [1,2,3,4,5,null,7]
# 输出：[1,#,2,3,#,4,5,7,#]
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
# 
# 
# 
# 提示：
# 
# 
# 树中的节点数小于 6000
# -100 <= node.val <= 100
# 
# 
# 
# 
# 
# 
# 
#

# @lc code=start
""""""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # 层次遍历
    # 每一层依次指定next
    def connect2(self, root: 'Node') -> 'Node':
        if not root:return root
        stack = [root]
        while stack:
            n = len(stack)
            for i in range(n):
                node = stack.pop(0)
                if i<n-1:
                    node.next = stack[0]        #当前的next就是stack中的第一个
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return root
    
    def connect(self, root: 'Node') -> 'Node':
        re = root
        dummy = Node(0)
        cur = dummy
        while root:
            if root.left:
                cur.next = root.left    #每层第一次，dummy.next = 下一层的第一个， 所以后面有root = dummy.next
                cur = cur.next
            if root.right:
                cur.next = root.right
                cur = cur.next
            root = root.next            #通过next，不段向右走
            if not root:                #这一层走完，重置cur
                cur = dummy
                root = dummy.next
                dummy.next = None       #重置dummy.next,否则会影响cur.next
        return re


# @lc code=end

#   1
#  2  3
# 4 5  7
t1 = Node(1)
t2 = Node(2)
t3 = Node(3)
t4 = Node(4)
t5 = Node(5)
# t6 = Node(6)
t7 = Node(7)

root = t1
root.left = t2
root.right = t3
t2.left = t4
t2.right = t5
# t3.left = t6
t3.right = t7
o = Solution()
print(o.connect(t1))