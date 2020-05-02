# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题03.03.堆盘子
# 
# https://leetcode-cn.com/problems/stack-of-plates-lcci/
# 
# 堆盘子。设想有一堆盘子，堆太高可能会倒下来。因此，在现实生活中，盘子堆到一定高度时，我们就会另外堆一堆盘子。请实现数据结构SetOfStacks，模拟这种行为。SetOfStacks应该由多个栈组成，并且在前一个栈填满时新建一个栈。此外，SetOfStacks.push()和SetOfStacks.pop()应该与普通栈的操作方法相同（也就是说，pop()返回的值，应该跟只有一个栈时的情况一样）。 进阶：实现一个popAt(int index)方法，根据指定的子栈，执行pop操作。
# 当某个栈为空时，应当删除该栈。当栈中没有元素或不存在该栈时，pop，popAt&nbsp;应返回 -1.
# 
# 示例1:
# 
#  输入：
# ["StackOfPlates", "push", "push", "popAt", "pop", "pop"]
# [[1], [1], [2], [1], [], []]
#  输出：
# [null, null, null, 2, 1, -1]
# 
# 
# 示例2:
# 
#  输入：
# ["StackOfPlates", "push", "push", "push", "popAt", "popAt", "popAt"]
# [[2], [1], [2], [3], [0], [0], [0]]
#  输出：
# [null, null, null, null, 2, 1, 3]
# 
# 
# 
# Medium 37.0%
# Testcase Example: ["StackOfPlates", "push", "push", "popAt", "pop", "pop"]
# [[1], [1], [2], [1], [], []]
# 
# 提示:
# 你需要追踪每个子栈的大小。当一个栈已满时，你可能需要创建一个新栈。
# 在一个特定的子栈中弹出一个元素意味着一些栈没有满。这是个问题吗？没有正确的答案，但你应该考虑如何处理这个问题。
# 
# 

class StackOfPlates:

    def __init__(self, cap: int):
        self.capacity = cap
        self.data = [[]]

    def push(self, val: int) -> None:
        if self.capacity <= 0:return
        if len(self.data)==0 or len(self.data[-1]) == self.capacity:
            self.data.append([])
        self.data[-1].append(val)
        # print(self.data)

    def pop(self) -> int:
        if len(self.data) == 0 or len(self.data[-1]) == 0:
            return -1
        re = self.data[-1].pop()
        if len(self.data[-1]) == 0:
            self.data.pop()
        return re

    def popAt(self, index: int) -> int:
        if len(self.data) <= index or len(self.data[index]) == 0:
            return -1
        re = self.data[index].pop()
        if len(self.data[index]) == 0:
            self.data.pop(index)
        return re



# Your StackOfPlates object will be instantiated and called as such:
obj = StackOfPlates(1)
obj.push(1)
obj.push(2)
print(obj.popAt(1))
print(obj.pop())
print(obj.pop())

# obj = StackOfPlates(2)
# obj.push(1)
# obj.push(2)
# obj.push(3)
# print(obj.popAt(0))
# print(obj.popAt(0))
# print(obj.popAt(0))



