#!/usr/bin/python
#coding:utf-8

# // 面试题28：对称的二叉树
# // 题目：请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和
# // 它的镜像一样，那么它是对称的。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetrical(self, root):
        if not root:return True
        def core(L, R):
            if not L and not R:return True
            if not L or not R:return False
            if L.val != R.val:return False
            return core(L.left, R.right) and core(L.right, R.left)
        
        return core(root.left, root.right)
        

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
#    8     8
#  1  4   4 1      
# 按层定义          
t1 = TreeNode(6)
t2 = TreeNode(8)
t3 = TreeNode(8)
t4 = TreeNode(1)
t5 = TreeNode(4)
t6 = TreeNode(4)
t7 = TreeNode(1)

root = t1
root.left = t2
root.right = t3
t2.left = t4
t2.right = t5
t3.left = t6
t3.right = t7
# t3.right = None #False

obj = Solution()
re = obj.levelOrder(root)
for i in range(len(re)):
    print(re[i])
print("\n")

print(obj.isSymmetrical(root))



