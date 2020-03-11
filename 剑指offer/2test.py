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
    
    
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        n = len(A)
        arrsum = sum(A)
        if arrsum%3!=0:
            return False
        subsum = arrsum//3
        i,j = 0,len(A)-1
        lsum,rsum = 0,0
        while lsum!=subsum and i<n:
            lsum+=A[i]
            i+=1
        while rsum!=subsum and j>=0:
            rsum+=A[j]
            j-=1
        return i<=j
    
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:return t2 
        if not t2:return t1
        def dfs(r1, r2):
            if not r1 and not r2:return None
            if not r1:
                return r2
            if not r2:return r1 
            r1.val += r2.val
            r1.left = dfs(r1.left, r2.left)
            r1.right = dfs(r1.right, r2.right)
            return r1
        dfs(t1, t2)
        return t1

    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:return []
        stack = [root]
        re = []
        while stack:
            cursum, cnt = 0,0
            for _ in range(len(stack)):
                n = stack.pop(0)
                cursum += n.val
                cnt += 1
                if n.left:
                    stack.append(n.left)
                if n.right:
                    stack.append(n.right)
            re.append(cursum/cnt)
        return re
    
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:return None
        def dfs(root):
            if not root:return None
            if root.val<L:
                return dfs(root.right)
            if root.val>R:
                return dfs(root.left)
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            return root
        dfs(root)
        return root

    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root: return -1 
        minval = root.val
        def dfs(root):
            nonlocal minval
            if not root :return -1
            if root.val>minval:
                return root.val
            l = dfs(root.left)
            r = dfs(root.right)
            if l<0:return r 
            if r<0:return l
            return min(l,r)
        return dfs(root)

    def convertBiNode(self, root: TreeNode) -> TreeNode:
        p = pre = None
        def dfs(root):
            nonlocal pre,p
            if not root:return None
            dfs(root.left)
            root.left = None
            if pre:
                pre.right = root
            else:
                p = root
            pre = root
            dfs(root.right)
        
        dfs(root)
        return p


# [4,2,5,1,3,null,6,0]
# o = Solution()
# print(o.canThreePartsEqualSum(A))


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
t1 = TreeNode(4)
t2 = TreeNode(2)
t3 = TreeNode(5)
t4 = TreeNode(1)
t5 = TreeNode(3)
t6 = TreeNode(6)
t7 = TreeNode(0)
root = t1
root.left = t2
root.right = t3
t2.left = t4
t2.right = t5
t3.right = t6
t4.left = t7

o = Solution()
# print(o.findSecondMinimumValue(root))
# print(o.levelOrder(t))
t = o.convertBiNode(root)
re = []
while t:
    re.append(t.val)
    t = t.right
print(re)

