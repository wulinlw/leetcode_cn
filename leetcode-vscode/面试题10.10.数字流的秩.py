# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题10.10.数字流的秩
# 
# https://leetcode-cn.com/problems/rank-from-stream-lcci/
# 
# 假设你正在读取一串整数。每隔一段时间，你希望能找出数字 x 的秩(小于或等于 x 的值的个数)。请实现数据结构和算法来支持这些操作，也就是说：
# 实现 track(int x) 方法，每读入一个数字都会调用该方法；
# 
# 实现 getRankOfNumber(int x) 方法，返回小于或等于 x 的值的个数。
# 
# 注意：本题相对原题稍作改动
# 
# 示例:
# 
# 输入:
# ["StreamRank", "getRankOfNumber", "track", "getRankOfNumber"]
# [[], [1], [0], [0]]
# 输出:
# [null,0,null,1]
# 
# 
# 提示：
# 
# 
# 	x <= 50000
# 	track 和 getRankOfNumber 方法的调用次数均不超过 2000 次
# 
# 
# 
# Medium 59.6%
# Testcase Example: ["StreamRank", "getRankOfNumber", "track", "getRankOfNumber"]
# [[], [1], [0], [0]]
# 
# 提示:
# 使用数组存在的问题是插入一个数字会比较慢。我们还能使用其他的数据结构吗？
# 二叉搜索树效果好吗？
# 考虑一个二叉搜索树，其中每个节点存储一些额外的数据。
# 
# 
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.cnt = 1                               #当前值出现次数

class StreamRank:

    def __init__(self, x=None):
        self.root = None

    def track(self, x: int) -> None:
        def insert(node, x):
            if not node:
                return TreeNode(x) 
            if x < node.val:
                node.left = insert(node.left, x)
            elif x > node.val:
                node.right = insert(node.right, x)
            else:
                node.cnt += 1                      #当前值出现次数+1
            return node
        self.root = insert(self.root, x)

    def getRankOfNumber(self, x: int) -> int:
        def find(node, x):
            if not node: return 0
            re = 0
            if node.val <= x:
                re += node.cnt                      #在右边，加root，
                re += find(node.right, x)           #一步一步加右边
            re += find(node.left, x)                #一步一步加左边
            return re
        return find(self.root, x)
            




# Your StreamRank object will be instantiated and called as such:
obj = StreamRank()
print(obj.getRankOfNumber(1))
obj.track(0)
print(obj.getRankOfNumber(0))
