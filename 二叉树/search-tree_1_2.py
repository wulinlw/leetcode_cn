#!/usr/bin/python
#coding:utf-8


# https://leetcode-cn.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/64/introduction-to-a-bst/172/
# 二叉搜索树迭代器
# 实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。
# 调用 next() 将返回二叉搜索树中的下一个最小的数。

# 示例：
# BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // 返回 3
# iterator.next();    // 返回 7
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 9
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 15
# iterator.hasNext(); // 返回 true
# iterator.next();    // 返回 20
# iterator.hasNext(); // 返回 false
 
# 提示：
# next() 和 hasNext() 操作的时间复杂度是 O(1)，并使用 O(h) 内存，其中 h 是树的高度。
# 你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 中至少存在一个下一个最小的数。

class TreeNode(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.head = root
        self.stack = deque()
        
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """       
        cur = self.stack.pop()
        root = cur.right
        while root:   # 使用了循环，复杂度不应该为O(1)?
            self.stack.append(root)
            root = root.left
        
        return cur.val


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()