#!/usr/bin/python
#coding:utf-8

import sys,math
from typing import List

# 59（一）：滑动窗口的最大值


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
    
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        l = 1 
        r = 0
        cursum = 0
        re = []
        while r<target:
            r+=1
            cursum += r
            while cursum >target:
                cursum -= l
                l+=1 
            if cursum == target and l!=r:
                re.append(list(range(l,r+1)))
        return re

target = 9
# 输出：[[2,3,4],[4,5]]
# target = 15
# 输出：[[1,2,3,4,5],[4,5,6],[7,8]]

o = Solution()
print(o.findContinuousSequence(target))
