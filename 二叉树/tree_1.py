#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/learn/card/data-structure-binary-tree/2/traverse-a-tree/1/
# 二叉树的前序遍历

# https://leetcode-cn.com/explore/learn/card/data-structure-binary-tree/2/traverse-a-tree/2/
# 中序遍历二叉树

# https://leetcode-cn.com/explore/learn/card/data-structure-binary-tree/2/traverse-a-tree/3/
# 二叉树的后序遍历

# https://leetcode-cn.com/explore/learn/card/data-structure-binary-tree/2/traverse-a-tree/9/
# 二叉树的层次遍历


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        stack, output = [root, ], []
        
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
        
        return output

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)
                
        return output[::-1]

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        WHITE, GRAY = 0, 1
        stack = []
        init_level = 0
        stack.append((root, WHITE, init_level))
        result = []
        while stack:
            node, color, level = stack.pop()
            if node:
                if color == WHITE:
                    stack.append((node.right, WHITE, level+1))
                    stack.append((node.left, WHITE, level+1))
                    stack.append((node, GRAY, level))
                else:
                    if len(result) == level: result.append([])
                    result[level].append(node.val)
        return result

nums = [7,2,5,10,8]
m = 2
ss = Solution()
re = ss.splitArray(nums,m)
print(re)

