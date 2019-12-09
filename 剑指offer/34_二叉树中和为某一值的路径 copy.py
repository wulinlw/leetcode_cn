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
    # 后续遍历最后一位是root，比他小的是left，大的是right
    def FindPath(self, root, expectedSum):
        def core(root, curSum, path):
            path.append(root.val)
            curSum += root.val
            if not root.left and not root.right and curSum == expectedSum:
                print(path)
            if root.left:
                core(root.left, curSum, path)
            if root.right:
                core(root.right, curSum, path)
            path.pop()
        
        return core(root, 0, [])

    
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
#        10
#    5     12
#  4  7                  
t1 = TreeNode(10)
t2 = TreeNode(5)
t3 = TreeNode(12)
t4 = TreeNode(4)
t5 = TreeNode(7)

root = t1
root.left = t2
root.right = t3
t2.left = t4
t2.right = t5



obj = Solution()
re = obj.levelOrder(root)
for i in range(len(re)):
    print(re[i])
print("\n")
obj.FindPath(t1, 19)

