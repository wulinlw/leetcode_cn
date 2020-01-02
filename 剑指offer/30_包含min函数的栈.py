#!/usr/bin/python
#coding:utf-8

# // 面试题30：包含min函数的栈
# // 题目：定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的min
# // 函数。在该栈中，调用min、push及pop的时间复杂度都是O(1)。

class StackWithMin:
    def __init__(self):
        self.stack = []
        self.stack_min = []

    def min(self):
        if not self.stack_min:
            return None
        return self.stack_min[-1]

    def push(self, obj):
        self.stack.append(obj)
        if not self.stack_min:
            self.stack_min.append(obj)
        else:#最小的放stack_min最后
            tmp = None
            if obj < self.stack_min[-1]:
                tmp = obj
            else:
                tmp = self.stack_min[-1]
            self.stack_min.append(tmp)

    def pop(self):
        if not self.stack or not self.stack_min:
            return None
        self.stack_min.pop()
        return self.stack.pop()
    
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