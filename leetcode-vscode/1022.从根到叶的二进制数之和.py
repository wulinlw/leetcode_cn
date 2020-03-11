#
# @lc app=leetcode.cn id=1022 lang=python3
#
# [1022] 从根到叶的二进制数之和
#
# https://leetcode-cn.com/problems/sum-of-root-to-leaf-binary-numbers/description/
#
# algorithms
# Easy (57.63%)
# Likes:    37
# Dislikes: 0
# Total Accepted:    4.7K
# Total Submissions: 8.1K
# Testcase Example:  '[1,0,1,0,1,0,1]'
#
# 给出一棵二叉树，其上每个结点的值都是 0 或 1 。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。例如，如果路径为 0 -> 1 -> 1
# -> 0 -> 1，那么它表示二进制数 01101，也就是 13 。
# 
# 对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。
# 
# 以 10^9 + 7 为模，返回这些数字之和。
# 
# 
# 
# 示例：
# 
# 
# 
# 输入：[1,0,1,0,1,0,1]
# 输出：22
# 解释：(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
# 
# 
# 
# 
# 提示：
# 
# 
# 树中的结点数介于 1 和 1000 之间。
# node.val 为 0 或 1 。
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
    def sumRootToLeaf111(self, root: TreeNode) -> int:
        if not root:return 0
        path = []
        nums = []
        def dfs(root):
            nonlocal path,nums
            if not root:return
            if not root.left and not root.right:
                tmp = path[:]+[str(root.val)]
                nums.append("".join(tmp))
            path.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            path.pop()
        dfs(root)
        # print(nums)
        sum = 0 
        for i in nums:
            sum += int(i,2)
        return sum

    # 二进制    
    def sumRootToLeaf(self, root: TreeNode) -> int:
        sum = 0
        def dfs(root, val):
            nonlocal sum
            if not root:return None
            newval = val<<1 | root.val          #左移后再与当前值（0，1），组成二进制数
            if not root.left and not root.right:
                sum += newval
                return
            dfs(root.left,newval)
            dfs(root.right,newval)
        dfs(root, 0)
        return sum % 1000000007
# @lc code=end

t1 = TreeNode(1)
t2 = TreeNode(0)
t3 = TreeNode(1)
t4 = TreeNode(0)
t5 = TreeNode(1)
t6 = TreeNode(0)
t7 = TreeNode(1)
root = t1
root.left = t2
root.right = t3
t2.left = t4
t2.right = t5
t3.left = t6
t3.right = t7


o = Solution()
print(o.sumRootToLeaf(root))