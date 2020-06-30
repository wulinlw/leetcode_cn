#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# https://leetcode-cn.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (29.10%)
# Likes:    543
# Dislikes: 0
# Total Accepted:    103.5K
# Total Submissions: 340.3K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
# 
# 假设一个二叉搜索树具有如下特征：
# 
# 
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 
# 
# 示例 1:
# 
# 输入:
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 输出: true
# 
# 
# 示例 2:
# 
# 输入:
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
# 根节点的值为 5 ，但是其右子节点值为 4 。
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
    # 层次遍历
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 从根开始遍历，每层写入一个新数组
        # 在将left ,right写入下次需要巡皇的数组
        # 循环完成即可得到每层的数组
        queue = [root]
        res = []
        if not root:
            return []
        while queue:
            templist = []#此层的数组
            templen =len(queue)
            for i in range(templen):                
                temp = queue.pop(0)
                templist.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            # print(templist)
            res.append(templist)
        return res
    
    # 递归
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:return True
        def dfs(root, small, big):                  #需要带上最大值，最小值取到下一次比较
            if not root:return True
            val = root.val
            if val <= small or val >= big:
                return False
            if not dfs(root.left, small, val):
                return False
            if not dfs(root.right, val, big):
                return False
            return True

        return dfs(root, float('-inf'), float('inf'))

    # 中序遍历
    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True



# @lc code=end

#   5
#  1  4
#    3 6
# t1 = TreeNode(5)
# t2 = TreeNode(1)
# t3 = TreeNode(4)
# t4 = TreeNode(3)
# t5 = TreeNode(6)

# root = t1
# root.left = t2
# root.right = t3
# t3.left = t4
# t3.right = t5

def stringToTreeNode(input):
    inputValues = [s.strip() for s in input.split(',')]
    print(inputValues)
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1 
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

input = "5,1,4,null,null,3,6"
input = "10,5,15,null,null,6,20"
root = stringToTreeNode(input)
o = Solution()
# print(o.levelOrder(root))
print(o.isValidBST(root))