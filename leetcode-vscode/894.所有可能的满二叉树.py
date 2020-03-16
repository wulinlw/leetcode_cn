#
# @lc app=leetcode.cn id=894 lang=python3
#
# [894] 所有可能的满二叉树
#
# https://leetcode-cn.com/problems/all-possible-full-binary-trees/description/
#
# algorithms
# Medium (73.00%)
# Likes:    75
# Dislikes: 0
# Total Accepted:    4.8K
# Total Submissions: 6.5K
# Testcase Example:  '7'
#
# 满二叉树是一类二叉树，其中每个结点恰好有 0 或 2 个子结点。
# 
# 返回包含 N 个结点的所有可能满二叉树的列表。 答案的每个元素都是一个可能树的根结点。
# 
# 答案中每个树的每个结点都必须有 node.val=0。
# 
# 你可以按任何顺序返回树的最终列表。
# 
# 
# 
# 示例：
# 
# 输入：7
# 
# 输出：[[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# 解释：
# 
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= N <= 20
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 子问题：构造一棵满二叉树
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        res = []
        if N == 1:
            return [TreeNode(0)]
        # 结点个数必须是奇数
        if N % 2 == 0:
            return []
        
        # 左子树分配一个节点
        left_num = 1
        # 右子树可以分配到 N - 1 - 1 = N - 2 个节点
        right_num = N - 2
        
        while right_num > 0:
            # 递归构造左子树
            left_tree = self.allPossibleFBT(left_num)
            # 递归构造右子树
            right_tree = self.allPossibleFBT(right_num)
            # 具体构造过程
            for i in range(len(left_tree)):
                for j in range(len(right_tree)):
                    root = TreeNode(0)
                    root.left = left_tree[i]
                    root.right = right_tree[j]
                    res.append(root)
            left_num += 2
            right_num -= 2
        
        return res     

    # 作者：jalan
    # 链接：https://leetcode-cn.com/problems/all-possible-full-binary-trees/solution/man-er-cha-shu-di-gui-xiang-jie-by-jalan/
    # 来源：力扣（LeetCode）
    # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# @lc code=end

