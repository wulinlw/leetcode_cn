#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#
# https://leetcode-cn.com/problems/house-robber-iii/description/
#
# algorithms
# Medium (55.95%)
# Likes:    293
# Dislikes: 0
# Total Accepted:    20.6K
# Total Submissions: 36.6K
# Testcase Example:  '[3,2,3,null,3,null,1]'
#
# 在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。
# 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
# 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
# 
# 计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
# 
# 示例 1:
# 
# 输入: [3,2,3,null,3,null,1]
# 
# ⁠    3
# ⁠   / \
# ⁠  2   3
# ⁠   \   \ 
# ⁠    3   1
# 
# 输出: 7 
# 解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
# 
# 示例 2:
# 
# 输入: [3,4,5,1,3,null,1]
# 
# 3
# ⁠   / \
# ⁠  4   5
# ⁠ / \   \ 
# ⁠1   3   1
# 
# 输出: 9
# 解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
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
    # O(N)
    def rob1(self, root: TreeNode) -> int:
        if not root:return 0 
        cache = {}
        def dfs(root):
            if not root:return 0 
            if root in cache:
                return cache[root]
            left,right = 0,0
            if root.left:
                left = dfs(root.left.left) + dfs(root.left.right)
            if root.right:
                right = dfs(root.right.left) + dfs(root.right.right)
            do = root.val + left + right                #抢，然后去下下家，root加孙节点
            notdo = dfs(root.left) + dfs(root.right)    #不抢，然后去下家，左右子节点
            res = max(do, notdo)
            cache[root] = res 
            return res

        return dfs(root)

    # 返回一个大小为 2 的数组 arr
    # arr[0] 表示不抢 root 的话，得到的最大钱数
    # arr[1] 表示抢 root 的话，得到的最大钱数
    def rob(self, root: TreeNode) -> int: 
        def dfs(root):
            if not root:return (0, 0)                   #（不抢root，抢root）最大收益
            left = dfs(root.left)
            right = dfs(root.right)
            do = root.val + left[0] + right[0]          #抢，下家不抢
            notdo = max(left[0], left[1]) + \
                    max(right[0], right[1])             #不抢，下家可抢，可不抢
            return (notdo, do)
        res = dfs(root)
        return max(res[0], res[1])







        
# @lc code=end

# 测试树
#      3
#     / \
#    2   3
#     \   \ 
#      3   1           
t1 = TreeNode(3)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(3)
t5 = TreeNode(1)
root = t1
root.left = t2
root.right = t3
t2.right = t4
t3.right = t5

o = Solution()
print(o.rob(root))