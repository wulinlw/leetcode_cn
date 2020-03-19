#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#
# https://leetcode-cn.com/problems/path-sum-iii/description/
#
# algorithms
# Easy (54.17%)
# Likes:    311
# Dislikes: 0
# Total Accepted:    23.8K
# Total Submissions: 43.8K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# 给定一个二叉树，它的每个结点都存放着一个整数值。
# 
# 找出路径和等于给定数值的路径总数。
# 
# 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
# 
# 二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
# 
# 示例：
# 
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
# 
# ⁠     10
# ⁠    /  \
# ⁠   5   -3
# ⁠  / \    \
# ⁠ 3   2   11
# ⁠/ \   \
# 3  -2   1
# 
# 返回 3。和等于 8 的路径有:
# 
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3.  -3 -> 11
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 双递归O(n^2)
    # pathSum来遍历整棵树，core来计算到当前节点是否符合，core中也递归处理
    # def pathSum(self, root: TreeNode, sum: int) -> int:
    #     if not root:return 0
    #     re = self.core(root, sum)+self.pathSum(root.left, sum)+self.pathSum(root.right, sum)
    #     return re

    # def core(self, root, sum):
    #     if not root:return 0
    #     cnt = 0
    #     if sum==root.val: 
    #         cnt+=1
    #     cnt += self.core(root.left, sum-root.val) 
    #     cnt += self.core(root.right, sum-root.val)
    #     return cnt

    # 前缀和，O(n)
    # https://leetcode-cn.com/problems/path-sum-iii/solution/da-dao-zhi-jian-qian-zhui-he-de-li-jie-by-cocowy/
    def pathSum(self, root: TreeNode, sum: int) -> int:
        m = {}
        m[0] = 1                                        #初始化默认值
        return self.help(root, sum, m, 0)
    
    def help(self, root, sum, m, cursum):
        if not root:return 0
        cursum += root.val
        if cursum-sum not in m:
            m[cursum-sum] = 0
        count = m[cursum-sum]                           #出现的次数，前缀出现的次数

        if cursum not in m:
            m[cursum] = 0
        m[cursum]+=1                                    #回溯，设为1，找下一个
        count += self.help(root.left, sum, m, cursum)
        count += self.help(root.right, sum, m, cursum)
        m[cursum]-=1
        return count
    # 10   5   3   数组中找和为 8 的路径
    # 10   15  18  cursum
    # 2    7   10  cursum-sum
    # cursum-sum出现了10，这个10就是前缀和
    # 回溯前前缀和的值是1，加上后面的，就是总的要反回的
    # 如果后面也能找到，就是不断的1+1+1+...
# @lc code=end


#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
t1 = TreeNode(10)
t2 = TreeNode(5)
t3 = TreeNode(-3)
t4 = TreeNode(3)
t5 = TreeNode(2)
t6 = TreeNode(11)
t7 = TreeNode(3)
t8 = TreeNode(-2)
t9 = TreeNode(1)


root = t1
root.left = t2
root.right = t3
t2.left = t4
t2.right = t5
t4.left = t7
t4.right = t8
t5.right = t9
t3.right = t6
o = Solution()
# print(o.levelOrder(root))
print(o.pathSum(root, 8))
