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


    def movingCount(self, m: int, n: int, k: int) -> int:
        self.cache = {}
        def moving(x, y):
            curCnt = 0
            if x<0 or x>=m or y<0 or y>=n or not check(x, y, k) or (x, y) in self.cache:
                return curCnt
            self.cache[(x, y)] = 1
            curCnt +=  1 + moving(x+1, y)+\
                    moving(x, y+1)
            return curCnt
        
        def check(x, y, k):
            n = int(str(x)+str(y))
            ans = 0
            while n:
                ans += n % 10
                n //= 10
            return True if ans<=k else False

        return moving(0, 0)

        



m = 2
n = 3
k = 1

# m = 3
# n = 1
# k = 0
o = Solution()
print(o.movingCount(m, n, k))


1 5 5 11
1 6 11 22



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

