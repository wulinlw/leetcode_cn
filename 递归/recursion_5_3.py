#!/usr/bin/python
#coding:utf-8


# https://leetcode-cn.com/explore/orignial/card/recursion-i/260/conclusion/1233/
# 不同的二叉搜索树 II
# 给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

# 示例:
# 输入: 3
# 输出:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# 解释:
# 以上的输出对应以下 5 种不同结构的二叉搜索树：

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class B_Tree(object):
    def __init__(self, node=None):
        self.root = node
        
    def add(self, item=None):
        #如果输入item是None 则表示一个空节点
        node = TreeNode(x=item)
        #如果是空树，则直接添到根
        #此时判断空的条件为，
        if not self.root or self.root.val is None:
            self.root = node
        else:
        #不为空，则按照 左右顺序 添加节点
            my_queue = []
            my_queue.append(self.root)
            while True:
                cur_node = my_queue.pop(0)
                #即如果该当前节点为空节点则直接跳过它，起到一个占位的作用
                if cur_node.val is None:
                    continue
                if not cur_node.left:
                    cur_node.left = node
                    return
                elif not cur_node.right:
                    cur_node.right = node
                    return
                else:
                    my_queue.append(cur_node.left)
                    my_queue.append(cur_node.right)

    def build(self, itemList):
        for i in itemList:
            self.add(i)
    
    def preTraverse(self, root):  
        '''
        前序遍历
        根在最前
        从上到下，最左边的val，左、右
        '''
        if root==None:  
            return  
        print(root.val)  
        self.preTraverse(root.left)  
        self.preTraverse(root.right)  

    def midTraverse(self, root): 
        '''
        中序遍历
        根在中间
        最左边的从左、val、右，...根...最右边的从左、val、右
        '''
        if root==None:  
            return  
        self.midTraverse(root.left)  
        print(root.val)  
        self.midTraverse(root.right)  

    def afterTraverse(self, root):  
        '''
        后序遍历
        根在最后
        最左边的左、右，val,依次排列，最后是根
        '''
        if root==None:  
            return  
        self.afterTraverse(root.left)  
        self.afterTraverse(root.right)  
        print(root.val)


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # 链接：https://leetcode-cn.com/problems/unique-binary-search-trees-ii/solution/bu-tong-de-er-cha-sou-suo-shu-ii-by-leetcode/
        def generate_trees(start, end):
            if start > end:
                return [None,]
            
            all_trees = []
            for i in range(start, end + 1):  # 当前数为root
                left_trees = generate_trees(start, i - 1) #i是root，剩余 i - 1 个元素可用于左子树，n - i 个元素用于右子树。 
                right_trees = generate_trees(i + 1, end)
                
                # 链接左右树
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
            return all_trees
        
        return generate_trees(1, n) if n else []


n=3
S = Solution()
deep = S.generateTrees(n)
print("deep:",deep)
