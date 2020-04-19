#!/usr/bin/python
#coding:utf-8

import sys,math
from typing import List
import heapq,bisect
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


    def reformat(self, s: str) -> str:
        if not s:return ""
        if len(s)==1:return s
        a = []
        b = []
        re = ""
        for i in s:
            if i.isalpha():
                a.append(i)
            else:
                b.append(i)
        if not a or not b:return ""
        if len(b)>len(a):
            a,b = b,a
        i=0
        while i<len(s):
            if a:
                re = re + a.pop()
            if b:
                re = re + b.pop()
            i+=1
        return re

    def displayitem(self, orders: List[List[str]]) -> List[List[str]]:
        item = collections.defaultdict(list)
        re = [[]]
        table = []
        for i in range(len(orders)):
            if orders[i][2] not in re[0]:
                bisect.insort_left(re[0], orders[i][2])
            if orders[i][1] not in item[orders[i][1]]:
                item[orders[i][1]].append(orders[i][2])
            if int(orders[i][1]) not in table:
                bisect.insort_left(table, int(orders[i][1]))
        re[0].insert(0, 'Table')
        print(re)
        print(table)
        print(item)
        orders.sort(key = lambda x: int(x[1]))
        print(orders)
        for i in table:
            tmp = [str(i)]
            for j in range(1, len(re[0])):
                print(i,j,re[0][j])
                if re[0][j] in item[i]:
                    tmp.append("1")
                else:
                    tmp.append("0")
            re.append(tmp)
        return re



orders = [
    ["David","3","Ceviche"],
    ["Corina","10","Beef Burrito"],
    ["David","3","Fried Chicken"],
    ["Carla","5","Water"],
    ["Carla","5","Ceviche"],
    ["Rous","3","Ceviche"]]
o = Solution()
print(o.displayitem(orders))

acbacbacbacb
abab

# s = "a0b1c2"
# s = "leetcode"
# s = "1229857369"
# s = "covid2019"
# s = "ab123"
# o = Solution()
# print(o.reformat(s))





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

