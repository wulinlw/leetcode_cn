#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#
# https://leetcode-cn.com/problems/lru-cache/description/
#
# algorithms
# Medium (45.87%)
# Likes:    482
# Dislikes: 0
# Total Accepted:    44.1K
# Total Submissions: 94.2K
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
#  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
# 
# 获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) -
# 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
# 
# 进阶:
# 
# 你是否可以在 O(1) 时间复杂度内完成这两种操作？
# 
# 示例:
# 
# LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得密钥 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得密钥 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4
# 
# 
#

# @lc code=start
import collections
class Node:
    def __init__(self, key=None, value=None):
        self.key = key 
        self.value = value
        self.nex = None                                 #双向链表前后指针
        self.pre = None

    #插入节点
	# self-> nex-> self.nex
    def insert(self, node):
        node.pre = self
        node.nex = self.nex
        self.nex.pre = node
        self.nex = node
        
# 创建双向链表，包含值位0的head，tail
def create_linked_list():
	head = Node(0, 0)
	tail = Node(0, 0)
	head.nex = tail
	tail.pre = head
	return (head, tail)

class LRUCache:
    def __init__(self, capacity: int):
        self.keyMap = {}                                #存储键值对，值是node 类型#键值对总数
        self.visitMap = create_linked_list()            #双向链表，最近访问的放在链表后面tail.pre，则删除时从前面删head.nex
        self.size = 0                                   #键值对总数
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.keyMap:  
            self.update(self.keyMap[key])               #更新最近访问，从链表头删掉，放到链表结尾
            return self.keyMap[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity:
            if key in self.keyMap:                      #存在则更新值
                node = self.keyMap[key]
                node.value = value
            else:
                node = Node(key, value)                 #不存在新建Node
                self.keyMap[key] = node
                self.size += 1                          #键值对总数+1
            if self.size > self.capacity:               #超出容量时，删除链表头的，新节点插入链表尾
                self.size -= 1
                delete = self.delete(self.visitMap[0].nex)
                self.keyMap.pop(delete)
            self.update(node)

    def delete(self, node):                             #删除双向链表节点
        if node.pre:
            node.pre.nex = node.nex
            node.nex.pre = node.pre
        return node.key

    def update(self, node):                             #更新一个节点为最后访问，删除链表头的，新节点插入链表尾
        self.delete(node)
        self.visitMap[-1].pre.insert(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))       #返回  1
cache.put(3, 3)                 #该操作会使得密钥 2 作废
print(cache.get(2))       #返回 -1 (未找到)
cache.put(4, 4)                 #该操作会使得密钥 1 作废
print(cache.get(1))       #返回 -1 (未找到)
print(cache.get(3))       #返回  3
print(cache.get(4))       #返回  4
 