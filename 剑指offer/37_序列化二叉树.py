#!/usr/bin/python
#coding:utf-8

# // 面试题37：序列化二叉树
# // 题目：请实现两个函数，分别用来序列化和反序列化二叉树。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #用前序遍历，方便解码
    def serialize(self, root):
        if not root:return 'None'
        return str(root.val)+','+self.serialize(root.left)+','+self.serialize(root.right)

    def unserialize(self, data):
        def rdeserialize(l):
            if l[0] == 'None':
                l.pop(0)
                return None
                
            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        arr = data.split(',')
        return rdeserialize(arr)



    # def serialize(self, root):
    #     #先序
    #     res = []
    #     def helper(node):
    #         if node == None:
    #             res.append('#')
    #             return 
    #         res.append(str(node.val))
    #         helper(node.left)
    #         helper(node.right)
    #     helper(root)
    #     return ','.join(res)
        
    # def deserialize(self, data):
    #     D = iter(data.split(','))
    #     def dfs():
    #         node_val = next(D)
    #         if node_val == '#':
    #             return None
    #         root = TreeNode(node_val)
    #         root.left = dfs()
    #         root.right = dfs()
    #         return root
    #     return dfs()


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
# re = obj.levelOrder(root)
# for i in range(len(re)):
#     print(re[i])
# print("\n")

re = obj.serialize(root)
print(re)
reroot = obj.unserialize(re)
re = obj.levelOrder(reroot)
for i in range(len(re)):
    print(re[i])
print("\n")

