#!/usr/bin/python
#coding:utf-8

# // 面试题54：二叉搜索树的第k个结点
# // 题目：给定一棵二叉搜索树，请找出其中的第k大的结点。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def KthNode(self, root, k):
        if not root or k<=0:return False
        return self.core(root, k)
    
    #类似中序遍历
    def core(self, root, k):
        if not root:
            return None
        target = self.core(root.left, k)        #遍历左节点，
        if target:
            return target
        k-=1                                    #左节点空了，-1
        if k==1:                                #左节点遍历完，检查是否等于k
            return root
        target = self.core(root.right, k)
        if target:
            return target
# 1. 递归左子树，并判断有无返回节点。如果有，停止递归，返回所要返回的节点。
# 2. 当左子树没有返回节点时，判断当前的根节点是不是第k个遍历到的值（即第k大）。如果是，则返回该节点，停止递归。
# 3. 当左子树和根节点都没有返回节点时，递归右子树，并判断有无返回节点。如果有，停止递归，返回所要返回的节点。


    def kthLargest3(self, root, k) :
        ans = []
        def fuc(root):
            if not root :
                return 0
            fuc(root.left)
            ans.append(root.val)
            fuc(root.right)
        fuc(root)
        return ans[-k]


# 作者：z1m
# 链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/solution/zhong-xu-bian-li-by-ml-zimingmeng/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 测试树
#        6
#    2     8
#  1  4   7 9                
t1 = None
t2 = TreeNode(2)
t4 = TreeNode(4)
t6 = TreeNode(6)
t7 = TreeNode(7)
t8 = TreeNode(8)
t9 = TreeNode(9)

root = t6
root.left = t2
root.right = t8
t2.left = t1
t2.right = t4
t8.left = t7
t8.right = t9

obj = Solution()
print(obj.KthNode(root, 1).val)