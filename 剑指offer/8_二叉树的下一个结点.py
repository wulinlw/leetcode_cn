#!/usr/bin/python
#coding:utf-8

# 二叉树的下一个结点
# 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
# 注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

class Solution:

    def GetNext(self, node):
        if not root: 
            return False
        if node.right:
            next = node.right
            while next.left:
                next = next.left
            return next
        if node.parent:
            cur = node
            parent = node.parent
            while parent and (cur == parent.right):#只要cur是parent.right，就一直往上找
                cur = parent
                parent = parent.parent
            next = parent       #根右变的没有下一个的，这里会是root.parent ,就是none
        return next


    
    # 层次遍历，改成调试用的
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 从根开始遍历，每层写入一个新数组
        # 在将left ,right写入下次需要巡皇的数组
        # 循环完成即可得到每层的数组
        queue = [root]
        res = []
        if not root:
            return []
        while queue:
            templist = []#此层的数组
            templen =len(queue)
            for i in range(templen):                
                temp = queue.pop(0)
                # 节点值， parent值  用于调试
                templist.append((temp.val, temp.parent.val if temp.parent else None))
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            # print(templist)
            res.append(templist)
        return res


# 测试树
#        6
#    2     8
#  1  4   7 9                
#    3 5
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t7 = TreeNode(7)
t8 = TreeNode(8)
t9 = TreeNode(9)

root = t6
root.left = t2
root.right = t8
t2.parent = root
t8.parent = root

t2.left = t1
t2.right = t4
t1.parent = t2
t4.parent = t2

t4.left = t3
t4.right = t5
t3.parent = t4
t5.parent = t4

t8.left = t7
t8.right = t9
t7.parent = t8
t9.parent = t8

obj = Solution()

re = obj.levelOrder(root)
# print(re)
for i in re:
    print(i)
re = obj.GetNext(t1)
print(t1.val, obj.GetNext(t1).val)
print(t2.val, obj.GetNext(t2).val)
print(t3.val, obj.GetNext(t3).val)
print(t4.val, obj.GetNext(t4).val)
print(t5.val, obj.GetNext(t5).val)
print(t6.val, obj.GetNext(t6).val)
print(t7.val, obj.GetNext(t7).val)
print(t8.val, obj.GetNext(t8).val)
print(t9.val, obj.GetNext(t9))