#!/usr/bin/python
#coding:utf-8

import sys,math
from typing import List
import heapq

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
    
    
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        row = len(matrix)
        col = len(matrix[0])
        re = 0

        def getmax(colsum, k):
            maxval = cursum = colsum[0]
            for i in range(1, len(colsum)):
                cursum = max(cursum, cursum + colsum[i])
                maxval = max(maxval, cursum)
            return maxval

        for c in range(col):
            colsum = [0] * row
            for j in range(c, col):
                for r in range(row):
                    colsum[r] += matrix[r][j]
                re = max(re, getmax(colsum, k))
                if re>=k:return k
        return re
    
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs or not costs[0]: return 0
        dp = costs                                  #直接更新原始数组，节省空间
        
        def preline(idx, k):
            minval = float('inf')
            # minval = max(costs[idx])
            for i,num in enumerate(costs[idx]):
                if i==k:
                    continue
                minval = min(minval, num)
            return minval


        for i in range(1,len(costs)):
            for k in range(len(costs[i])):
                dp[i][k] += preline(i-1, k)

        return min(dp[-1])

costs = [[1,5,3],[2,9,4]]
o = Solution()
print(o.minCost(costs))


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

