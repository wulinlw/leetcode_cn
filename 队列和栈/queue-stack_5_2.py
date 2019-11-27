#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/learn/card/queue-stack/220/conclusion/889/
# 用队列实现栈
# 使用队列实现栈的下列操作：

# push(x) -- 元素 x 入栈
# pop() -- 移除栈顶元素
# top() -- 获取栈顶元素
# empty() -- 返回栈是否为空
# 注意:

# 你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
# 你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
# 你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
import collections
class MyQueue:
    
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1): 
            self.q.append(self.q.popleft())
        
    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]
    
    def empty(self):
        return not len(self.q)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()





