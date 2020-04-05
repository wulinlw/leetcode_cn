#!/usr/bin/python
#coding:utf-8

import sys,math
from typing import List
import heapq
import collections

class ComplexNode(object):
	def __init__(self, value, next=None, sibling=None):
		self.val = value
		self.next = next
		self.sibling = sibling

class ListNode:
	def __init__(self, x=None):
		self.val = x
		self.next = None

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class TrieNode:
	def __init__(self):
		self.child = {}
		self.isword = False

class Solution:
	def initlinklist(self, nums):
		head = ListNode(nums[0])
		re = head
		for i in nums[1:]:
			re.next = ListNode(i)
			re = re.next
		return head
	
	def printlinklist(self, head):
		re = []
		while head:
			re.append(head.val)
			head = head.next
		print(re)
		
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
	
	
	def hasGroupsSizeX(self, deck: List[int]) -> bool: 
		import collections,functools
		# def gcd(a,b):
		#     return a if b==0 else gcd(a%b, b)
		# cnt = collections.Counter(deck)
		# return functools.reduce(gcd, cnt.values())>=2

		cnt = collections.Counter(deck)
		for i in range(2,len(deck)+1):
			if i%len(deck)==0:
				if all(j%i==0 for j in cnt.values()):
					return True
		return False


class Node:
	def __init__(self, key=None, value=None, freq=0):
		self.pre = None
		self.nex = None
		self.freq = freq
		self.key = key
		self.value = value

	def insert(self, node):
		node.nex = self.nex
		node.pre = self
		self.nex.pre = node
		self.nex = node

def linkedlist():
	head = Node(0, 0)
	tail = Node(0, 0)
	head.nex = tail 
	tail.pre = head
	return (head, tail)    

class LFUCache:
	def __init__(self, capacity: int):
		self.freqMap = collections.defaultdict(linkedlist)
		self.keyMap = {}
		self.size = 0
		self.capacity = capacity
		self.minFreq = 0

	def get(self, key: int) -> int:
		if key in self.keyMap:
			self.increase(self.keyMap[key])
			return self.keyMap[key].value
		return -1

	def put(self, key: int, value: int) -> None:
		if self.capacity != 0:
			if key in self.keyMap:
				node = self.keyMap[key]
				node.value = value
			else:
				node = Node(key, value)
				self.keyMap[key] = node
				self.size += 1
			if self.size > self.capacity:
				self.size -= 1
				delete = self.delete(self.freqMap[self.minFreq][0].nex)
				self.keyMap.pop(delete)
			self.increase(node)

	def increase(self, node):
		node.freq += 1
		self.delete(node)
		self.freqMap[node.freq][-1].pre.insert(node)
		if node.freq == 1:
			self.minFreq = 1
		elif self.minFreq == node.freq - 1:
			head, tail = self.freqMap[node.freq - 1]
			if head.nex is tail:
				self.minFreq = node.freq
							#最小频率更新为节点当前频率

	def delete(self, node):
	    if node.pre:
	        node.pre.nex = node.nex
	        node.nex.pre = node.pre
	        if node.pre is self.freqMap[node.freq][0] and node.nex is self.freqMap[node.freq][-1]:
	            self.freqMap.pop(node.freq)
	    return node.key
	



cache = LFUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))       #返回 1
cache.put(3, 3)    		  		#去除 key 2
print(cache.get(2))       #返回 -1 (未找到key 2)
print(cache.get(3))       #返回 3
cache.put(4, 4)    		  		#去除 key 1
print(cache.get(1))       #返回 -1 (未找到 key 1)
print(cache.get(3))       #返回 3
print(cache.get(4))       #返回 4

#   1
#  2  3
# 4 5
# t1 = TreeNode(1)
# t2 = TreeNode(2)
# t3 = TreeNode(3)
# t4 = TreeNode(4)
# t5 = TreeNode(5)

# root = t1
# root.left = t2
# root.right = t3
# t2.left = t4
# t2.right = t5

#     4
#   2  5
#  1 3  6
# 0
# [4,2,5,1,3,null,6,0]
# t1 = TreeNode(4)
# t2 = TreeNode(2)
# t3 = TreeNode(5)
# t4 = TreeNode(1)
# t5 = TreeNode(3)
# t6 = TreeNode(6)
# t7 = TreeNode(0)
# root = t1
# root.left = t2
# root.right = t3
# t2.left = t4
# t2.right = t5
# t3.right = t6
# t4.left = t7

# nums = [10,9,2,5,3,7,101,18]
# o = Solution()
# print(o.lengthOfLIS(nums))
# # print(o.levelOrder(t))
# t = o.convertBiNode(root)
# re = []
# while t:
#     re.append(t.val)
#     t = t.right
# print(re)

