#!/usr/bin/python
#coding:utf-8

# // 面试题30：包含min函数的栈
# // 题目：定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的min
# // 函数。在该栈中，调用min、push及pop的时间复杂度都是O(1)。

class StackWithMin:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.min_stack:
            self.min_stack.append(node)
        else:
            if self.min_stack[-1] < node:
                self.min_stack.append(self.min_stack[-1])
            else:
                self.min_stack.append(node)
    def pop(self):
        # write code here
        self.stack.pop(-1)
        self.min_stack.pop(-1)
    
    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]
        else:
            return []

    def min(self):
        # write code here
        return self.min_stack[-1]
    
    def debug(self):
        print(self.stack)
        print(self.stack_min)
        print("\n")


s = StackWithMin()
s.push(2.98)
s.push(3)
s.debug()

s.pop()
s.debug()

s.push(1)
s.debug()

s.pop()
s.debug()

s.push(1)
s.push(2)
s.push(3)
s.debug()

s.push(0)
s.debug()