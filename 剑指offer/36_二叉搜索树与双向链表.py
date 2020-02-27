#!/usr/bin/python
#coding:utf-8

# // 面试题36：二叉搜索树与双向链表
# // 题目：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求
# // 不能创建任何新的结点，只能调整树中结点指针的指向。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 中序遍历，中间需要连接左边，root，右边，
    # 连接完成后需要移动lastnode到最右，即root
    # 遍历完成后返回的节点是最后，需要往前找到头部
    def Convert(self, root):
        if not root:return False
        lastNode = None
        lastNode = self.core(root, lastNode)
        while lastNode and lastNode.left:       #向左找到链表头
            lastNode = lastNode.left
        return lastNode
    
    def core(self, root, lastNode):
        if not root:return 
        if root.left:
            lastNode = self.core(root.left, lastNode)
        if lastNode:                                    #连接左 root 右
            lastNode.right = root                        #左边的下一个是root
            root.left = lastNode                         #右边的上一个是root
        lastNode = root                                  #连接后last变为root
        if root.right:
            lastNode = self.core(root.right, lastNode)
        return lastNode

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
        
# 测试树
#        6
#    2     8
#  1  4   7 9                
t1 = TreeNode(1)
t2 = TreeNode(2)
t4 = TreeNode(4)
t6 = TreeNode(6)
t7 = TreeNode(7)
t8 = TreeNode(8)
t9 = TreeNode(9)

root = t6
root.left = t2
root.right = t8
t2.left = t1
t2.right = t4
t8.left = t7
t8.right = t9

# obj = Solution()
# re = obj.levelOrder(root)
# for i in range(len(re)):
#     print(re[i])
# print("\n")

# re = obj.Convert(root)
# while re :
#     print(re.val)
#     if re.right:
#         re = re.right
#     else:
#         break

# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。
# 要求不能创建任何新的节点，只能调整树中节点指针的指向。
我们希望将这个二叉搜索树转化为双向循环链表。链表中的每个节点都有一个前驱和后继指针。对于双向循环链表，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。
下图展示了上面的二叉搜索树转化成的链表。“head” 表示指向链表中有最小元素的节点。
特别地，我们希望可以就地完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中的第一个节点的指针。
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof
class Solution2:
    def __init__(self):
        self.pre = None
        self.head = None
        self.tail = None

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        self.treeList(root)
        #将head与tail连接起来即得完整的双向链表
        self.head.left = self.tail          #head生成一个顺序的双向链表（首尾不相接）
        self.tail.right = self.head         #tail会得到逆序的双向链表（首尾不相接）
        return self.head

    def treeList(self,node):
        if not node:
            return None
        self.treeList(node.left)
        
        if self.pre == None:
            self.head = node
        else: 
            self.pre.right = node
        node.left = self.pre
        self.pre = node
        self.tail = node

        self.treeList(node.right)
# 采用中序遍历二叉搜索树，按照从小到大的顺序访问二叉树。用中间量将上一结点与当前结点进行双向连接。得到首尾不相接的双向顺序链表head和逆序链表tail
# 作者：ciwe
# 链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/solution/zhong-xu-bian-li-jie-fa-by-ciwe/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# 层次遍历

    # 提交第一名
    def treeToDoublyList1(self, root: 'Node') -> 'Node':
        if not root:
            return root 
        first, last = None, None 
        def dfs(head:'Node'):
            nonlocal first, last 
            if head:
                dfs(head.left)
                if last:
                   last.right = head 
                   head.left = last  
                else:
                    first = head 
                last = head 
                dfs(head.right)
        dfs(root)
        last.right = first
        first.left = last  
        return first
    
    #第二
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        l = self.pre(root)
        for i in range(len(l)):
            l[i].left = l[(i - 1) % len(l)]
            l[i].right = l[(i + 1) % len(l)]
        return l[0]

    def pre(self, root):
        if root is None:
            return []
        return self.pre(root.left) + [root] + self.pre(root.right)

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

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)

root = t4
root.left = t2
root.right = t5
t2.left = t1
t2.right = t3

obj = Solution2()
re = obj.levelOrder(root)
print(re)