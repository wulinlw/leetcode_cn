#!/usr/bin/python
#coding:utf-8


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 后续遍历最后一位是root，比他小的是left，大的是right
    def VerifySquenceOfBST(self, sequence):
            if len(sequence) <2:return True
            root = sequence[-1]
            small  = 0
            for i in range(len(sequence)):
                if sequence[i]>root:
                    small = i
                    for j in range(i,len(sequence)):
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