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
        self.data = []
        self.maxQueue = []              #从大到小排列
        self.index = 0
    
    def max(self):
        if self.maxQueue:
            return self.maxQueue[0][1]

    def push_back(self,num):
        while len(self.maxQueue)>0 and num>self.maxQueue[-1][1]:#maxQueue中比当前小的都删除
            self.maxQueue.pop()
        node = (self.index, num)
        self.maxQueue.append(node)
        self.data.append(node)
        self.index += 1
        print(self.data)
        print(self.maxQueue)
        print("\n")

    def pop_front(self):
        idx, num = self.data.pop(0)
        if idx == self.maxQueue[0][0]:
            self.maxQueue.pop(0)
        print(self.data)
        print(self.maxQueue)
        print("\n")


obj = QueueWithMax()
obj.push_back(1)
obj.push_back(3)
obj.push_back(2)
print(obj.max())
obj.pop_front()
print(obj.max())


