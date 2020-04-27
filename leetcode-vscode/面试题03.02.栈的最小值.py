# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题03.02.栈的最小值
# 
# https://leetcode-cn.com/problemset/lcci/
# 
# 请设计一个栈，除了常规栈支持的pop与push函数以外，还支持min函数，该函数返回栈元素中的最小值。执行push、pop和min操作的时间复杂度必须为O(1)。示例：MinStack minStack = new MinStack();minStack.push(-2);minStack.push(0);minStack.push(-3);minStack.getMin();   --> 返回 -3.minStack.pop();minStack.top();      --> 返回 0.minStack.getMin();   --> 返回 -2.
# 
# Easy 60.3%
# Testcase Example: ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# 
# 提示:
# 注意最小的元素不会经常变化。它只在添加更小的元素或最小的元素被弹出时才发生变化。
# 如果保持追踪每个栈节点的额外数据会怎么样？什么样的数据可能更容易解决这个问题呢？
# 考虑让每个节点知道它“子栈”的最小值（包括它下面的所有元素，以及它本身）。
# 
# 

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []
        
    def push(self, x: int) -> None:
        if not self.stack:
            self.minStack.append(x)
        else:
            if self.minStack[-1] >= x:
                self.minStack.append(x)
            else:
                self.minStack.append(self.minStack[-1])
        self.stack.append(x)

    def pop(self) -> None:
        if not self.stack:
            return 
        val = self.stack.pop()
        # if self.minStack[-1] == val:
        self.minStack.pop()


    def top(self) -> int:
        if not self.stack:
            return 
        return self.stack[-1]


    def getMin(self) -> int:
        return self.minStack[-1]
    def debug(self):
        print(self.stack)
        print(self.minStack)


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2)
obj.push(0)
obj.push(3)
obj.push(0)
print(obj.getMin())
obj.pop()
print(obj.getMin())
obj.pop()
print(obj.getMin())
obj.pop()
print(obj.getMin())
# print(obj.top())
obj.debug()
# print(obj.getMin())



