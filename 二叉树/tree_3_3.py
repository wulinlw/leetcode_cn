#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/learn/card/data-structure-binary-tree/4/conclusion/18/
# 填充每个节点的下一个右侧节点指针 II
# 给定一个二叉树

# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
# 初始状态下，所有 next 指针都被设置为 NULL。

# 示例：

# 输入：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":null,"next":null,"right":{"$id":"6","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}
# 输出：{"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":null,"right":null,"val":7},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"6","left":null,"next":null,"right":{"$ref":"5"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"6"},"val":1}
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。

# 提示：
# 你只能使用常量级额外空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。

class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # 层序遍历，给每层的的前n-1个节点添加next指针，同116题相同做法，O(n)的时间空间复杂度
        if not root: return root
        queue = [root]
        while(queue): 
            node_pre = None
            for _ in range(len(queue)):#保证每次都是读取一行的量
                node = queue.pop(0)
                if node_pre: node_pre.next = node
                node_pre = node
                if node.left:queue.append(node.left)
                if node.right:queue.append(node.right)
        return root

    def connect3(self, root: 'Node') -> 'Node':
        last = root #last始终表示每一层第一个有子树的节点
        while(last):
            while(last and not last.left and not last.right):#到达叶子
                last = last.next
            if not last:#为空
                break #如果没有左右子树，自然不用更改什么
            cur = None#当前节点，第一次赋值是第二层第一个
            i= last
            while(i):#相当于遍历每一层，利用next信息进行递推
                if i.left:
                    if cur:
                        cur.next = i.left
                    cur = i.left
                if i.right:
                    if cur:
                        cur.next = i.right
                    cur = i.right
                i = i.next#找兄弟给右节点
            last = last.left if last.left else last.right#由于开始的while循环已经确保last有子树
        return root




nums = [7,2,5,10,8]
m = 2
ss = Solution()
re = ss.splitArray(nums,m)
print(re)

