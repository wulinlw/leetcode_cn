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

    def lengthOfLIS1(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0:return 0 
        dp = [1] * n 
        maxLen = 0
        for i in range(n):
            for  j in range(i):
                if nums[j] < nums[i]:
                  dp[i] = max(dp[i], dp[j]+1)
            maxLen = max(maxLen, dp[i])
        print(dp)
        return maxLen   

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0:return 0 
        tail = [nums[0]]
        for num in nums[1:]:
            if num > tail[-1]:
                tail.append(num)
                continue
            l,r = 0,len(tail)-1 
            while l<r:
                mid = l+(r-l)//2 
                if tail[mid]<num:
                    l = mid+1
                else:
                    r = mid
            tail[l] = num
        print(tail)
        return len(tail) 

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def core(grid, i, j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]==0:
                return 0
            grid[i][j] = 0
            re = 1
            re += core(grid, i-1, j) +\
                  core(grid, i+1, j) +\
                  core(grid, i, j-1) +\
                  core(grid, i, j+1)
            return re

        maxval = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                tmp = core(grid,  i, j)
                maxval = max(maxval, tmp)
        return maxval

    #只看递归思路，会超时
    def divingBoard2(self, shorter: int, longer: int, k: int) -> List[int]:
        # 0块板    0, 0
        # 1       shorter, longer
        # 2       rec(k-1)+shorter, rec(k-1)+longer
        def recursion(k):
            nonlocal re
            if k==0:return 0, 0
            if k==1:return shorter, longer
            min, max = recursion(k-1)
            return min+shorter, max+longer
        small, big = recursion(k)
        if longer-shorter==0 :return []
        re = list(range(small, big+1, longer-shorter))
        return re

    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:return []
        elif shorter == longer:
            return [k*shorter]
        return list(range(shorter*k, longer*k + 1, (longer-shorter)))

    def compressString(self, S: str) -> str:
        s = list(S)
        re = ""
        i=0
        while i<len(s):
            j = i
            while j<len(s) and s[i]==s[j]:
                j += 1
            re = re+s[i]+str(j-i)
            i=j
        return re if len(re)<len(s) else S

    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        re = 0
        for i in range(n+1):
            re = re+i
            if i<n:
                re -=nums[i]
        return re


nums = [3,0,1]
#  输出："a2b1c5a3"
# s = "abbccd"
#  输出："abbccd"  a1b2c2d1
# 输出： {3,4,5,6}
o = Solution()
print(o.missingNumber(nums))

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

