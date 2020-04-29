# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题03.05.栈排序
# 
# https://leetcode-cn.com/problems/sort-of-stacks-lcci/
# 
# 栈排序。 编写程序，对栈进行排序使最小元素位于栈顶。最多只能使用一个其他的临时栈存放数据，但不得将元素复制到别的数据结构（如数组）中。该栈支持如下操作：push、pop、peek 和 isEmpty。当栈为空时，peek&nbsp;返回 -1。
# 示例1:
# 
#  输入：
# ["SortedStack", "push", "push", "peek", "pop", "peek"]
# [[], [1], [2], [], [], []]
#  输出：
# [null,null,null,1,null,2]
# 
# 
# 示例2:
# 
#  输入： 
# ["SortedStack", "pop", "pop", "push", "pop", "isEmpty"]
# [[], [], [], [1], [], []]
#  输出：
# [null,null,null,null,null,true]
# 
# 
# 说明:
# 
# 
# 	栈中的元素数目在[0, 5000]范围内。
# 
# 
# 
# Medium 53.0%
# Testcase Example: ["SortedStack", "push", "push", "peek", "pop", "peek"]
# [[], [1], [2], [], [], []]
# 
# 提示:
# 排序数组的一种方法是遍历数组，并将每个元素按排序顺序插入到一个新数组中。你可以用一个栈实现吗？
# 假设二级栈已排序。你能按顺序插入元素吗？你可能需要一些额外的存储空间。你可以使用什么额外的存储？
# 保持二级栈的排序顺序，最大的元素在顶部。使用主栈进行额外的存储。
# 
# 

class SortedStack:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, val: int) -> None:
        while self.s1 and self.s1[-1] > val:
            self.s2.append(self.s1.pop())
        self.s1.append(val)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> None:
        if not self.s1:
            return None
        self.s1.pop(0)


    def peek(self) -> int:
        if not self.s1:
            return -1
        return self.s1[0]


    def isEmpty(self) -> bool:
        return not self.s1 


# Your SortedStack object will be instantiated and called as such:
obj = SortedStack()
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.pop())
print(obj.peek())


# print(obj.pop())
# print(obj.pop())
# obj.push(1)
# print(obj.pop())
# print(obj.isEmpty())
