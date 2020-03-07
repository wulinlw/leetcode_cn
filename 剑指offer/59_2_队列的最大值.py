#!/usr/bin/python
#coding:utf-8

# // 面试题59（二）：队列的最大值
# 请定义一个队列并实现函数max得到队列里的最大值，
# 要求函数max，push_back和pop_front的时间复杂度都是O(1)

class QueueWithMax:
    # maxQueue从大到小排列
    # push_back新数据时，把maxQueue中所有小于此值的删除
    # pop_front时，对比弹出数据的索引是不是最大值，是最大值需要把maxQueue的最大值一起删掉(pop(0))
    def __init__(self):
        self.queue = []
        self.deque = []
        
    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while self.deque and value > self.deque[-1]:
            self.deque.pop(-1)
        self.deque.append(value)

    def pop_front(self) -> int:
        front = self.queue and self.queue.pop(0)
        if self.deque and self.deque[0] == front:
            self.deque.pop(0)
        return front or -1


obj = QueueWithMax()
obj.push_back(1)
obj.push_back(3)
obj.push_back(2)
print(obj.max())
obj.pop_front()
print(obj.max())


