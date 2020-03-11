#
# @lc app=leetcode.cn id=606 lang=python3
#
# [606] 根据二叉树创建字符串
#
# https://leetcode-cn.com/problems/construct-string-from-binary-tree/description/
#
# algorithms
# Easy (52.76%)
# Likes:    98
# Dislikes: 0
# Total Accepted:    9.4K
# Total Submissions: 17.7K
# Testcase Example:  '[1,2,3,4]'
#
# 你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。
# 
# 空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。
# 
# 示例 1:
# 
# 
# 输入: 二叉树: [1,2,3,4]
# ⁠      1
# ⁠    /   \
# ⁠   2     3
# ⁠  /    
# ⁠ 4     
# 
# 输出: "1(2(4))(3)"
# 
# 解释: 原本将是“1(2(4)())(3())”，
# 在你省略所有不必要的空括号对之后，
# 它将是“1(2(4))(3)”。
# 
# 
# 示例 2:
# 
# 
# 输入: 二叉树: [1,2,3,null,4]
# ⁠      1
# ⁠    /   \
# ⁠   2     3
# ⁠    \  
# ⁠     4 
# 
# 输出: "1(2()(4))(3)"
# 
# 解释: 和第一个示例相似，
# 除了我们不能省略第一个对括号来中断输入和输出之间的一对一映射关系。
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
    def tree2str(self, root: TreeNode) -> str:
        if not root: return ""
        re = ""
        def convert(root):
            if not root:
                return ""
            elif not root.left and not root.right:
                return str(root.val)
            #注意这里elif，只能选一条路走
            elif root.right:
                return str(root.val) + "("  + convert(root.left) + ")" + "(" + convert(root.right) + ")"
            else:
                return str(root.val) + "(" + convert(root.left) + ")"
                #没有右节点时，这里会省去右节点的（）
        re += convert(root)
        return re
# @lc code=end

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
root = t1
root.left = t2
root.right = t3
t2.left = t4


o = Solution()
print(o.tree2str(root))