#!/usr/bin/python
#coding:utf-8

# // 面试题33：二叉搜索树的后序遍历序列
# // 题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# // 如果是则返回true，否则返回false。假设输入的数组的任意两个数字都互不相同

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 后续遍历最后一位是root，比他小的是left，大的是right
    def VerifySquenceOfBST_1(self, sequence):
            if len(sequence) ==0:return False
            root = sequence[-1]
            small = big = 0
            for i in range(len(sequence)):      #找到left的结尾
                if sequence[i]>root:
                    small = i  
                    break
            for i in range(i,len(sequence)):    #右边有比root小的返回错误
                if sequence[i] < root:
                    return False
            left = True                         #开始递归
            if small>0:
                left = self.VerifySquenceOfBST(sequence[:small-1])
            right = True
            if big>0:
                right = self.VerifySquenceOfBST(sequence[small:-1])
            return left and right

    #上一个解法的优化版本,看这个
    def VerifySquenceOfBST(self, sequence):
            if len(sequence) <2:return True
            root = sequence[-1]
            small  = 0
            for i in range(len(sequence)):
                if sequence[i]>root:
                    small = i                           #找到left的结尾
                    for j in range(i,len(sequence)):    #对比右边的，有小于root的就是false
                        if sequence[j]<root:
                            return False
                    break
            return self.VerifySquenceOfBST(sequence[:small]) and self.VerifySquenceOfBST(sequence[small:-1])
        
        

# 测试树
#        8
#    6     10
#  5  7   9 11                

nums = [5,7,6,9,11,10,8]
obj = Solution()
re = obj.VerifySquenceOfBST(nums)
print(obj.VerifySquenceOfBST([5,7,6,9,11,10,8]))#true
print(obj.VerifySquenceOfBST([5,7,6,9,11,10,1,8]))#false
print(obj.VerifySquenceOfBST([7,4,6,5]))#false