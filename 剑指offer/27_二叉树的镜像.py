#!/usr/bin/python
#coding:utf-8

# // 面试题27：二叉树的镜像
# // 题目：请完成一个函数，输入一个二叉树，该函数输出它的镜像。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def MirrorRecursively(self, root):
        if not root:return None
        if not root.left and not root.right :return     #结束条件
        root.left,root.right = root.right,root.left
        if root.left:
            self.MirrorRecursively(root.left)
        if root.right:
            self.MirrorRecursively(root.right)
        return root
        

    # 层次遍历
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
                templist.append(temp.val)
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
t1 = TreeNode(1)
t2 = TreeNode(2)
t4 = TreeNode(4)
t6 = TreeNode(6)
t7 = TreeNode(7)
t8 = TreeNode(8)
t9 = TreeNode(9)

root = t6
root.left = t2
root.right = t8
t2.left = t1
t2.right = t4
t8.left = t7
t8.right = t9

obj = Solution()
re = obj.levelOrder(root)
for i in range(len(re)):
    print(re[i])
print("\n")

obj.MirrorRecursively(root)
re2 = obj.levelOrder(root)
for i in range(len(re2)):
    print(re2[i])



