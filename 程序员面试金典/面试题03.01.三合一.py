# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题03.01.三合一
# 
# https://leetcode-cn.com/problems/three-in-one-lcci/
# 
# 三合一。描述如何只用一个数组来实现三个栈。
# 你应该实现push(stackNum, value)、pop(stackNum)、isEmpty(stackNum)、peek(stackNum)方法。stackNum表示栈下标，value表示压入的值。
# 
# 构造函数会传入一个stackSize参数，代表每个栈的大小。
# 
# 示例1:
# 
#  输入：
# ["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"]
# [[1], [0, 1], [0, 2], [0], [0], [0], [0]]
#  输出：
# [null, null, null, 1, -1, -1, true]
# 说明：当栈为空时`pop, peek`返回-1，当栈满时`push`不压入元素。
# 
# 
# 示例2:
# 
#  输入：
# ["TripleInOne", "push", "push", "push", "pop", "pop", "pop", "peek"]
# [[2], [0, 1], [0, 2], [0, 3], [0], [0], [0], [0]]
#  输出：
# [null, null, null, null, 2, 1, -1, -1]
# 
# 
# 
# Easy 54.0%
# Testcase Example: ["TripleInOne", "push", "push", "pop", "pop", "pop", "isEmpty"]
# [[1], [0, 1], [0, 2], [0], [0], [0], [0]]
# 
# 提示:
# 栈只是一个数据结构，其中最近添加的元素首先被删除。你能用一个数组来模拟单个栈吗？请记住，有很多可能的解法且每个解法都有其利弊。
# 我们可以通过将数组的前三分之一分配到第一个栈、第二个三分之一分配到第二个栈、最后的第三个三分之一分配到第三个栈，来模拟数组中的三个栈。然而，实际上某个栈可能比其他的大得多。能更灵活地分配吗？
# 如果你想考虑灵活划分，可以移动栈。你能保证使用所有可用的容量吗？
# 试着把数组看作是循环的，这样数组的结尾就“环绕”到了数组的开始部分。
# 
# 

class TripleInOne:

    def __init__(self, stackSize: int):
        self.capacity = stackSize
        self.stack = [[],[],[]]             #3个栈

    def push(self, stackNum: int, value: int) -> None:
        if len(self.stack[stackNum]) < self.capacity:
            self.stack[stackNum].append(value)

    def pop(self, stackNum: int) -> int:
        if len(self.stack[stackNum]) == 0:
            return -1
        return self.stack[stackNum].pop()

    def peek(self, stackNum: int) -> int:
        if len(self.stack[stackNum]) == 0:
            return -1
        return self.stack[stackNum][-1]

    def isEmpty(self, stackNum: int) -> bool:
        return len(self.stack[stackNum]) == 0



# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)



