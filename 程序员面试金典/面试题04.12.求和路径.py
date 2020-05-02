# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题04.12.求和路径
# 
# https://leetcode-cn.com/problems/paths-with-sum-lcci/
# 
# 给定一棵二叉树，其中每个节点都含有一个整数数值(该值或正或负)。设计一个算法，打印节点数值总和等于某个给定值的所有路径的数量。注意，路径不一定非得从二叉树的根节点或叶节点开始或结束，但是其方向必须向下(只能从父节点指向子节点方向)。
# 示例:
# 给定如下二叉树，以及目标和&nbsp;sum = 22，
# 
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# 
# 
# 返回:
# 
# 3
# 解释：和为 22&nbsp;的路径有：[5,4,11,2], [5,8,4,5], [4,11,7]
# 
# 提示：
# 
# 
# 	节点总数 <= 10000
# 
# 
# 
# Medium 47.2%
# Testcase Example: [5,4,8,11,null,13,4,7,2,null,null,5,1]
# 22
# 
# 提示:
# 尝试简化问题。如果路径必须从根开始会如何？
# 不要忘记路径可能会重叠。例如，如果你正在寻找总和6，那么路径1 -> 3 -> 2和1 -> 3 -> 2 -> 4 -> 6 -> 2都是有效的。
# 如果每条路径必须从根开始，就从根开始遍历所有可能的路径。可以在遍历的同时追踪和，每次找到一个路径满足我们的目标和，就增加totalpaths的值。现在，如何将它扩展到可以在任何地方开始呢？记住：只需要一个蛮力算法即可完成。你可以稍后再优化。
# 为了将其扩展到从任何地方开始的路径，我们可以对所有节点重复此过程。
# 如果你已经设计了以上描述的算法，那么在平衡树中你会有一个O(NlogN)的算法。这是因为共N个节点，在最坏情况下，每个节点的深度是O(logN)。节点上方的每个节点都会访问一次。因此，N个节点将被访问O(logN)的时间。有一种优化算法，其运行时间为O(N)。
# 在当前的蛮力算法中重复了什么工作？
# 从根开始考虑每个路径（有n个这样的路径）作为一个数组。该蛮力算法具体运作如下：拿着每个数组来寻找所有具有特定和的连续子序列。我们这样做是计算了所有子数组以及它们的和。把目光聚焦在这个小问题上可能会大有裨益。给定一个数组，你如何寻找具有特定和的所有连续子序列？同样，想想蛮力算法中的重复工作。
# 我们正在寻找和为targetSum的子数组。注意，可以在常数时间得到runningSumi的值，这是从元素0到元素i的和。一个从i到j的子数组和为targetSum，则 runningSumi-1 + targetSum必须等于runningSumj（试着画一个数组或一条数字线）。随着往下走，可以追踪runningSum，那么如何能快速查找i对应的使前面等式成立的值？
# 尝试使用一个散列表，从runningSum的值映射到使用runningSum元素的个数。
# 一旦你完成了这样的算法，找出了和为给定值的所有连续子数组，试着将它应用到一棵树上。请记住，在遍历和修改散列表时，你可能需要在遍历回来时将散列表的“损坏”逆转。
# 
# 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 构建两个 prefix sum 和 prefixdict dfs + 前缀和 + 回溯
    def pathSum(self, root: TreeNode, sum: int) -> int:
        re = 0
        preSum = 0                                      #前缀和
        preDic = {0:1}                                  #前缀和出现次数，默认0出现1次
        def dfs(root, preSum, preDic):
            nonlocal re
            if not root:return 0
            preSum += root.val                          #前缀和
            old = preSum - sum                          #前缀和-目标值。存在就加上这些出现的次数
            if old in preDic:
                re += preDic[old]
            preDic[preSum] = preDic.get(preSum, 0) + 1  #出现过就在原值基础上+1 ，开始回溯
            dfs(root.left, preSum, preDic)
            dfs(root.right, preSum, preDic)
            preDic[preSum] -= 1                         #回溯完-1

        dfs(root, preSum, preDic)
        return re



#       5
#     4   8
#    11  13 4
#   7 2    5 1
t1 = TreeNode(5)
t2 = TreeNode(4)
t3 = TreeNode(8)
t4 = TreeNode(11)
t5 = TreeNode(13)
t6 = TreeNode(4)
t7 = TreeNode(7)
t8 = TreeNode(2)
t9 = TreeNode(5)
t10 = TreeNode(1)

root = t1
root.left = t2
root.right = t3
t2.left = t4
t3.left = t5
t3.right = t6
t4.left = t7
t4.right = t8
t6.left = t9
t6.right = t10
sum = 22
o = Solution()
print(o.pathSum(root, sum))