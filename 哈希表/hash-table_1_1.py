#!/usr/bin/python
# coding:utf-8

# https://leetcode-cn.com/explore/learn/card/hash-table/203/design-a-hash-table/799/
# 设计哈希集合
# 不使用任何内建的哈希表库设计一个哈希集合

# 具体地说，你的设计应该包含以下的功能

# add(value)：向哈希集合中插入一个值。
# contains(value) ：返回哈希集合中是否存在这个值。
# remove(value)：将给定值从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。

# 示例:

# MyHashSet hashSet = new MyHashSet()
# hashSet.add(1)
# hashSet.add(2)
# hashSet.contains(1)
# // 返回 true
# hashSet.contains(3)
# // 返回 false(未找到)
# hashSet.add(2)
# hashSet.contains(2)
# // 返回 true
# hashSet.remove(2)
# hashSet.contains(2)
# // 返回  false(已经被删除)

# 注意：

# 所有的值都在[1, 1000000]的范围内。
# 操作的总数目在[1, 10000]范围内。
# 不要使用内建的哈希集合库。


class Node:

    def __init__(self, val, nex):
        self.val = val
        self.nex = nex


class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.h = [Node(None, None) for _ in range(self.size)]

    def add(self, key: int) -> None:
        p = self.h[key % self.size]
        node = p.nex
        while node:
            if node.val == key:
                break
            p = node
            node = node.nex
        else:
            p.nex = Node(key, None)

    def remove(self, key: int) -> None:
        p = self.h[key % self.size]
        node = p.nex
        while node:
            if node.val == key:
                p.nex = node.nex
                break
            p = node
            node = node.nex

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        node = self.h[key % self.size]
        while node:
            if node.val == key:
                return True
            node = node.nex
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
