#!/usr/bin/python
#coding:utf-8


# https:#leetcode-cn.com/explore/interview/card/bytedance/245/data-structure/1032/
# LRU缓存机制
# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

# 获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。
# 进阶:
# 你是否可以在 O(1) 时间复杂度内完成这两种操作？
# 示例:
# LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       # 返回  1
# cache.put(3, 3);    # 该操作会使得密钥 2 作废
# cache.get(2);       # 返回 -1 (未找到)
# cache.put(4, 4);    # 该操作会使得密钥 1 作废
# cache.get(1);       # 返回 -1 (未找到)
# cache.get(3);       # 返回  3
# cache.get(4);       # 返回  4

# https:#blog.csdn.net/Sun_White_Boy/article/details/87474565
class LRUCache(object):
    # 使用一个字典记录密钥和值的关系
    # 使用一个队列记录密钥使用的前后 来确定最近最少使用
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.maxlength = capacity
        self.array = {}
        self.array_list = []                        #头进尾出

    def get(self, key):
        value = self.array.get(key)
        # 如果密钥存在 将该密钥移到队列首
        if value is not None and self.array_list[0] is not key:
            index = self.array_list.index(key)
            self.array_list.pop(index)
            self.array_list.insert(0, key)

        value = value if value is not None else -1
        return value

    def put(self, key, value):
        # 如果重复
        if self.array.get(key) is not None:
            index = self.array_list.index(key)
            self.array.pop(key)
            self.array_list.pop(index)

        # 如果队满
        if len(self.array_list) >= self.maxlength:
            key_t = self.array_list.pop(self.maxlength-1)
            self.array.pop(key_t)

        # 插入队首
        self.array[key] = value
        self.array_list.insert(0, key)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
cache = LRUCache( 2 )

print cache.put(1, 1)
print cache.put(2, 2)
print cache.get(1)       # 返回  1
print cache.put(3, 3)    # 该操作会使得密钥 2 作废
print cache.get(2)       # 返回 -1 (未找到)
print cache.put(4, 4)    # 该操作会使得密钥 1 作废
print cache.get(1)       # 返回 -1 (未找到)
print cache.get(3)       # 返回  3
print cache.get(4)       # 返回  4









