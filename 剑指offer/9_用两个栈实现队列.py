#!/usr/bin/python
#coding:utf-8

# 用两个栈实现队列
# 队列的声明如下，请实现它的两个函数appendTail和deleteHead, 
# 分别完成在队列尾部插入结点和在队列头部删除结点的功能

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        # 只能append到后面，从后面弹出pop(-1)
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, node):
        self.stack1.append(node)

    #2个队列互相压栈
    def deleteHead2(self):
        n = len(self.stack1)
        for _ in range(n-1):
             self.stack2.append(self.stack1.pop(-1))
        self.stack1 = []
        while self.stack2:
            self.stack1.append(self.stack2.pop(-1))

    # 正确方式
    # stack2为空时，把stack1全部压入stack2，
    # 总是从stack2中删
    def deleteHead(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop(-1))
        if not self.stack2:
            return False
        self.stack2.pop(-1)

    def print(self):
        print(self.stack1)
        print(self.stack2)
        print("\n")
        
P = Solution()
P.appendTail(10)
P.appendTail(11)
P.appendTail(12)
P.print()
print(P.deleteHead())
P.print()
P.appendTail(13)#11,12,13
P.print()
print(P.deleteHead())#12,13
P.print()

print(P.deleteHead())
print(P.deleteHead())
print(P.deleteHead())
P.print()