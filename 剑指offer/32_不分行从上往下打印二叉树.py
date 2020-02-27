#!/usr/bin/python
#coding:utf-8

# // 面试题32（一）：不分行从上往下打印二叉树
# // 题目：从上往下打印出二叉树的每个结点，同一层的结点按照从左到右的顺序打印。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def PrintFromTopToBottom(self, root):
        if not root:return None
        re = []
        stack = [root]
        while stack:
            tmp = []
            for _ in range(len(stack)):
                node = stack.pop(0)
                tmp.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            re.append(tmp)
        return re

    # 之字形打印二叉树
    def PrintFromTopToBottom2(self, root):
        nodelist=[root]
        res=[]
        flag=0 #0代表从左向右
        while nodelist:
            temp=[]
            restemp=[]
            for i in range(len(nodelist)-1, -1, -1):
                if nodelist[i]:
                    restemp.append(nodelist[i].val)
                    if flag%2==0:
                        temp.append(nodelist[i].left) 
                        temp.append(nodelist[i].right)
                    else:
                        temp.append(nodelist[i].right)
                        temp.append(nodelist[i].left)
            
            nodelist=temp
            # for i in temp:
            #     print(i.val)
            # print("\n")
            res.append(restemp)
            flag=1-flag
        return res[:-1]

    def PrintFromTopToBottom3(self, root):
        re = []
        stack = [root]          #奇数行队列
        next = []               #偶数行队列
        while stack or next:
            tmp = []
            if stack:#遍历奇数栈
                while stack:
                    node = stack.pop()
                    tmp.append(node.val)
                    if node.left:
                        next.append(node.left)
                    if node.right:
                        next.append(node.right)
                re.append(tmp)
            else:#遍历偶数栈
                while next:
                    node = next.pop()
                    tmp.append(node.val)
                    if node.right:                  #先放右边，这一行完成时，如9，7，4，1
                        stack.append(node.right)
                    if node.left:
                        stack.append(node.left)
                re.append(tmp)
        return re



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
t2.left = t1
t2.right = t4
t4.left = t3
t4.right = t5
t8.left = t7
t8.right = t9

obj = Solution()
# re = obj.PrintFromTopToBottom(root)
# print(re)
re = obj.PrintFromTopToBottom3(root)
print(re)
# for i in range(1,-1,-1):
#     print(i)