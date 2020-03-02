#!/usr/bin/python
#coding:utf-8

# // 面试题34：二叉树中和为某一值的路径
# // 题目：输入一棵二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所
# // 有路径。从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:    
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
        
    def pathSum(self, root, target) :
        if not root:
            return None
        res = []
        def dfs(root,tmp):
            if not root.left and not root.right:
                if sum(tmp)== target:
                    res.append(tmp)
            if root.left:
                dfs(root.left,tmp+[root.left.val])
            if root.right:
                dfs(root.right,tmp+[root.right.val])

        dfs(root,[root.val])
        return res 


# 测试树
#        10
#    5     9
#  4  7                  
t1 = TreeNode(10)
t2 = TreeNode(5)
t3 = TreeNode(9)
t4 = TreeNode(4)
t5 = TreeNode(7)

root = t1
root.left = t2
root.right = t3
t2.left = t4
t2.right = t5



obj = Solution()
re = obj.levelOrder(root)
# for i in range(len(re)):
#     print(re[i])
# print("\n")
print(obj.pathSum(t1, 19))
