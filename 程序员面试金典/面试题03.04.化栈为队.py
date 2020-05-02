# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题03.04.化栈为队
# 
# https://leetcode-cn.com/problems/implement-queue-using-stacks-lcci/
# 
# 实现一个MyQueue类，该类用两个栈来实现一个队列。示例：MyQueue queue = new MyQueue();queue.push(1);queue.push(2);queue.peek();  // 返回 1queue.pop();   // 返回 1queue.empty(); // 返回 false说明：你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size 和 is empty 操作是合法的。你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。
# 
# Easy 73.2%
# Testcase Example: ["MyQueue","push","push","peek","pop","empty"]
# [[],[1],[2],[],[],[]]
# 
# 提示:
# 队列和栈的主要区别是元素的顺序。队列删除最旧的项，栈删除最新的项。如果你只访问最新的项，那么如何从栈中删除最旧的项？
# 我们可以通过不断地删除最新的项（将这些项插入临时栈中）来删除栈中最老的项，直到得到一个元素为止。然后，在检索到最新项后，将所有元素返回。与此有关的问题是，每次在一行中做几个弹出操作（pop）将需要O(n)的时间。我们可以优化在一行中连续弹出这一场景吗？
# 
# 

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        if not self.s2:
            return False
        return self.s2.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        if not self.s2:
            return False
        return self.s2[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.s1 and not self.s2



# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.pop())
print(obj.empty())



