#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#
# https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/description/
#
# algorithms
# Easy (43.93%)
# Likes:    83
# Dislikes: 0
# Total Accepted:    9.6K
# Total Submissions: 21.9K
# Testcase Example:  '[1,null,2,2]'
#
# 给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
# 
# 假定 BST 有如下定义：
# 
# 
# 结点左子树中所含结点的值小于等于当前结点的值
# 结点右子树中所含结点的值大于等于当前结点的值
# 左子树和右子树都是二叉搜索树
# 
# 
# 例如：
# 给定 BST [1,null,2,2],
# 
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  2
# 
# 
# 返回[2].
# 
# 提示：如果众数超过1个，不需考虑输出顺序
# 
# 进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）
# 
#
from typing import List
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 二叉搜索树的中序遍历是一个升序序列，逐个比对当前结点(root)值与前驱结点（pre)值。
    # 更新当前节点值出现次数(curTimes)及最大出现次数(maxTimes)，
    # 更新规则：
    # 若curTimes=maxTimes,将root.val添加到结果向量(res)中；
    # 若curTimes>maxTimes,清空res,将root.val添加到res,并更新maxTimes为curTimes。
    # https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/solution/er-cha-sou-suo-shu-zhong-de-zhong-shu-by-junstat/
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:return 
        re = []
        pre = None
        curtime = 1 #起始值，从根开始，他当前出现的次数就是1
        maxtime = 0
        def dfs(root):
            nonlocal pre, curtime, maxtime, re
            if not root:return
            dfs(root.left)
            if pre:
                curtime = curtime+1 if root.val==pre.val else 1
            if curtime==maxtime:
                re.append(root.val)
            elif curtime>maxtime:
                re = []
                re.append(root.val)
                maxtime = curtime
            pre = root
            dfs(root.right)
        dfs(root)
        return re
# @lc code=end

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(2)

root = t1
root.right = t2
t2.left = t3

o = Solution()
# print(o.levelOrder(root))
print(o.findMode(root))