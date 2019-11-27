#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/66/conclusion/183/
# Kth Largest Element in a Stream
# 设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。
# 你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，它包含数据流中的初始元素。每次调用 KthLargest.add，返回当前数据流中第K大的元素。
# 示例:

# int k = 3;
# int[] arr = [4,5,8,2];
# KthLargest kthLargest = new KthLargest(3, arr);
# kthLargest.add(3);   # returns 4
# kthLargest.add(5);   # returns 5
# kthLargest.add(10);  # returns 5
# kthLargest.add(9);   # returns 8
# kthLargest.add(4);   # returns 8
# 说明:
# 你可以假设 nums 的长度≥ k-1 且k ≥ 1。
class TreeNode(object):
    def __init__(self, x=None, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
        
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
        '''
        if root==None:  
            return  
        print(root.val)  
        self.preTraverse(root.left)  
        self.preTraverse(root.right)  

    def midTraverse(self, root): 
        '''
        中序遍历
        '''
        if root==None:  
            return  
        self.midTraverse(root.left)  
        print(root.val)  
        self.midTraverse(root.right)  

    def afterTraverse(self, root):  
        '''
        后序遍历
        '''
        if root==None:  
            return  
        self.afterTraverse(root.left)  
        self.afterTraverse(root.right)  
        print(root.val)

    def levelOrder(self, root):
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

class KthLargest(object):
    
    # def __init__(self, k, nums):
    #     self.k, self.n = k, sorted(nums)

    # def add(self, val) :
    #     import bisect
    #     idx = bisect.bisect_left(self.n, val, 0, len(self.n))
    #     self.n.insert(idx, val)
    #     return self.n[-self.k]
    
    def __init__(self, k, nums):
        import heapq
        self.pool = heapq.nlargest(k, nums)[::-1] #hi，我是一丢丢。。。。
        # print(self.pool)
        self.k = k

    def add(self, val) :
        import heapq
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)#删除堆中最小元素并加入一个元素
        # print(self.pool)
        return self.pool[0] 


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
k = 3
arr = [4,5,8,2]
kthLargest = KthLargest(k, arr)
# re = kthLargest.add(3)   # returns 4
# re = kthLargest.add(5)   # returns 5
re = kthLargest.add(10)  # returns 5
# kthLargest.add(9)   # returns 8
# kthLargest.add(4)   # returns 8
print(re)

