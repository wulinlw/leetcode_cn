#!/usr/bin/python
#coding:utf-8

# // 面试题36：二叉搜索树与双向链表
# // 题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求
# // 不能创建任何新的结点，只能调整树中结点指针的指向。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Convert(self, root):
        if not root:return False
        lastNode = None
        lastNode = self.core(root, lastNode)
        while lastNode and lastNode.left:       #向左找到链表头
            lastNode = lastNode.left
        return lastNode
    
    def core(self, root, lastNode):
        if not root:return 
        cur = root
        if root.left:
            lastNode = self.core(root.left, lastNode)
        if lastNode:                                    #左中右
            lastNode.right = cur
            cur.left = lastNode
        lastNode = cur
        if root.right:
            lastNode = self.core(root.right, lastNode)
        return lastNode

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

re = obj.Convert(root)
while re :
    print(re.val)
    if re.right:
        re = re.right
    else:
        break