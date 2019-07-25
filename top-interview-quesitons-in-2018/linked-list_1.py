#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/featured/card/top-interview-quesitons-in-2018/265/linked-list/1145/
# 复制带随机指针的链表
# 给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
# 要求返回这个链表的深拷贝。 

# 示例：

# 输入：
# {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}
# 解释：
# 节点 1 的值是 1，它的下一个指针和随机指针都指向节点 2 。
# 节点 2 的值是 2，它的下一个指针指向 null，随机指针指向它自己。
# 提示：
# 你必须返回给定头的拷贝作为对克隆列表的引用。


# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    # 先循环一遍，把node建完，把所有的node存在dic的key里；之后再循环一遍，把关系整好
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        relation = {} # relation tuples
        new_prev = None
        cur = head
        while cur != None:
            new_list = Node(None, None, None)
            new_list.val = cur.val
            relation[cur] = new_list
            if new_prev:
                new_prev.next = new_list
            new_prev = new_list
            cur = cur.next
        for key,value in relation.iteritems():
            if key.random != None:
                value.random = relation[key.random]
        new_head = relation[head] if head else None
        return new_head




# s = Solution()
# res = s.copyRandomList()
# print(res)
