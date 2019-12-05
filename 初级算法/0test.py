#!/usr/bin/python
#coding:utf-8
import sys

class TreeNode(object):
    def __init__(self, x=None, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class B_Tree(object):
    def __init__(self, node=None):
        self.root = node
        self.treelist = []
        
    def add(self, item=None):
        #如果输入item是None 则表示一个空节点
        node = TreeNode(x=item)
        #如果是空树，则直接添到根
        #此时判断空的条件为，
        if not self.root or self.root.val is None:
            self.root = node
        else:
        #不为空，则按照 左右顺序 添加节点
            my_queue = []
            my_queue.append(self.root)
            while True:
                cur_node = my_queue.pop(0)
                #即如果该当前节点为空节点则直接跳过它，起到一个占位的作用
                if cur_node.val is None:
                    continue
                if not cur_node.left:
                    cur_node.left = node
                    return
                elif not cur_node.right:
                    cur_node.right = node
                    return
                else:
                    my_queue.append(cur_node.left)
                    my_queue.append(cur_node.right)

    def build(self, itemList):
        for i in itemList:
            self.add(i)
    
    def preTraverse(self, root):  
        '''
        前序遍历
        '''
        if root==None:  
            return  
        self.treelist.append(root.val)  
        self.preTraverse(root.left)  
        self.preTraverse(root.right)  

    def midTraverse(self, root): 
        '''
        中序遍历
        '''
        if root==None:  
            return  
        self.midTraverse(root.left)  
        print(root.val)  
        self.midTraverse(root.right)  

    def afterTraverse(self, root):  
        '''
        后序遍历
        '''
        if root==None:  
            return  
        self.afterTraverse(root.left)  
        self.afterTraverse(root.right)  
        print(root.val)



class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def printn(self, n):
        num = ['0']*n
        for i in range(10):
            num[0] = str(i)
            self.recur(num,n,0)

    def recur(self,num,n,index):
        l = len(num)
        if index ==l-1: 
            self.printshow(num)
            return 
        for i in range(10):
            num[index+1] = str(i)
            self.recur(num,n,i+1)
    def printshow(self,s):
        print(s)
        # for i in range(len(s)):
        #     if s[i]!=0:
        #         print(i,"")
        # print("\t")

    def permute(self, nums):
        res = []
        def per(nums,i):
            newstr = nums[:]
            if i==len(newstr)-1:
                res.append(newstr)
            for j in range(i, len(newstr)):
                newstr[i],newstr[j] = newstr[j],newstr[i]
                per(newstr, i+1)
                newstr[i],newstr[j] = newstr[j],newstr[i]
        per(nums,0)
        return res
    
    def test(self,nums,k):
        def position(nums,l,r):
            i = l-1
            h = nums[r-1]
            for j in range(r):
                if nums[i]<h:
                    i+=1
                    nums[i],nums[j] = nums[j],nums[i]
            nums[i+1],h = h,nums[i+1]
            print(nums,i+1)
            return i+1
        position(nums,0,len(nums)-1)
    
    def numberOfDice(self,n):
        res = []
        f = [[0 for _ in range(6 * n + 1)] for _ in range(n + 1)]
        print(f)
        for i in range(1, 7): # 初始状态为1
            f[1][i] = 1
        print(f)
        for i in range(2, n + 1):
            for j in range(i, 6 * i + 1):
                for k in range(1, min(j, 6) + 1):
                    f[i][j] += f[i - 1][j - k] # 上一次抛掷target为j - k时的状态

        for i in range(n, n * 6 + 1):
            res.append(f[n][i]) # 第n次抛掷时值为i的次数
        return res

    def multiply(self, A):
        # write code here
        if not A:
            return []
        num = len(A)
        B = [None]*num
        #B[i]的意义是A数组不包括i位置的所有乘积，分为i左边的元素乘积和 i右边的所有元素乘积。
        #初始化B[0]=1，是因为0左边没有元素，所以乘积为1。
        B[0] = 1
        for i in range(1,num):
            B[i] = B[i-1]*A[i-1]
        temp = 1
        for i in range(num-2,-1,-1):#从后往前遍历不算最后一个（num-1）因为第一个for循环中已经计算了 
            temp *= A[i+1]
            B[i] *= temp
        return B



n=3
s = Solution()
r = s.numberOfDice(n)
print(r)
a = [0,1,2,3,4,5]
r2 = s.multiply(a)
print(r2)