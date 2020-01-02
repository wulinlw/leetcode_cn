#!/usr/bin/python
#coding:utf-8

# // 面试题26：树的子结构
# // 题目：输入两棵二叉树A和B，判断B是不是A的子结构。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, root1, root2):
        if not root1 or not root2:return False
        re = False
        if root1.val == root2.val:
            re = self.HasSubtreeCore(root1, root2)      #只有等于才到core里找，不然就分别左右和完整的root2比
        if not re: 
            re = self.HasSubtree(root1.left, root2)
        if not re: 
            re = self.HasSubtree(root1.right, root2)
        return re

    def HasSubtreeCore(self, root1, root2):
        if not root2: return True                       #正确的要放前面，不然会一直错误
        if not root1: return False

        if root1.val != root2.val:
            return False
        
        return self.HasSubtreeCore(root1.left, root2.left) and \
        self.HasSubtreeCore(root1.right, root2.right)        

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
re = obj.levelOrder(root)
for i in range(len(re)):
    print(re[i])

print(obj.HasSubtree(root, t8))
print(obj.HasSubtree(root, t9))
print(obj.HasSubtree(root, t1))
print(obj.HasSubtree(root, t4))



