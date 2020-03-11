#!/usr/bin/python
#coding:utf-8





from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self):
        self.root = None
    
    def construct_tree(self, values=None):
        if not values:
            return None
        self.root = TreeNode(values[0])
        queue = deque([self.root])
        leng = len(values)
        nums = 1
        while nums < leng:
            node = queue.popleft()
            if node:
                node.left = TreeNode(values[nums]) if values[nums] else None
                queue.append(node.left)
                if nums + 1 < leng:
                    node.right = TreeNode(values[nums+1]) if values[nums+1] else None
                    queue.append(node.right)
                    nums += 1
                nums += 1
    
    def bfs(self):
        ret = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node:
                ret.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return ret

    def pre_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return
            ret.append(head.val)
            traversal(head.left)
            traversal(head.right)
        traversal(self.root)
        return ret

    def in_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return
            traversal(head.left)
            ret.append(head.val)
            traversal(head.right)

        traversal(self.root)
        return ret

    def post_traversal(self):
        ret = []

        def traversal(head):
            if not head:
                return
            traversal(head.left)
            traversal(head.right)
            ret.append(head.val)

        traversal(self.root)
        return ret

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
    
    def traverse(self,rootnode):
        thislevel = [rootnode]
        a = '                                '
        while thislevel:
            nextlevel = list()
            a = a[:len(a)//2]
            for n in thislevel:
                print(a+str(n.val), end='')
                if n.left: nextlevel.append(n.left)
                if n.right: nextlevel.append(n.right)
            print("")
            thislevel = nextlevel

t = Tree()
t.construct_tree([1, 2, None, 4, 3, None, 5])
print(t.root)
print(t.traverse(t.root))
print(t.levelOrder(t.root))







