# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题03.06.动物收容所
# 
# https://leetcode-cn.com/problems/animal-shelter-lcci/
# 
# 动物收容所。有家动物收容所只收容狗与猫，且严格遵守“先进先出“的原则。在收养该收容所的动物时，收养人只能收养所有动物中“最老“（由其进入收容所的时间长短而定）的动物，或者可以挑选猫或狗（同时必须收养此类动物中“最老“的）。换言之，收养人不能自由挑选想收养的对象。请创建适用于这个系统的数据结构，实现各种操作方法，比如enqueue、dequeueAny、dequeueDog和dequeueCat。允许使用Java内置的LinkedList数据结构。
# enqueue方法有一个animal参数，animal[0]代表动物编号，animal[1]代表动物种类，其中 0 代表猫，1 代表狗。
# 
# dequeue*方法返回一个列表[动物编号, 动物种类]，若没有可以收养的动物，则返回[-1,-1]。
# 
# 示例1:
# 
#  输入：
# ["AnimalShelf", "enqueue", "enqueue", "dequeueCat", "dequeueDog", "dequeueAny"]
# [[], [[0, 0]], [[1, 0]], [], [], []]
#  输出：
# [null,null,null,[0,0],[-1,-1],[1,0]]
# 
# 
# 示例2:
# 
#  输入：
# ["AnimalShelf", "enqueue", "enqueue", "enqueue", "dequeueDog", "dequeueCat", "dequeueAny"]
# [[], [[0, 0]], [[1, 0]], [[2, 1]], [], [], []]
#  输出：
# [null,null,null,null,[2,1],[0,0],[1,0]]
# 
# 
# 说明:
# 
# 
# 	收纳所的最大容量为20000
# 
# 
# 
# Easy 59.6%
# Testcase Example: ["AnimalShelf", "enqueue", "enqueue", "dequeueCat", "dequeueDog", "dequeueAny"]
# [[], [[0, 0]], [[1, 0]], [], [], []]
# 
# 提示:
# 让我们假设用不同的列表存储猫和狗。怎样才能找到所有物种中最老的动物呢？要有创意。
# 可以考虑为狗和猫保留一个链表，然后遍历它找到第一只狗（或猫）。这样做的影响是什么？
# 想想现实生活中你是怎么做的。你有一个按时间排序的狗列表和一个按时间排序的猫列表。你需要什么数据才能找到最老的动物？你将如何维护这些数据？
# 
# 
from typing import List
class AnimalShelf:

    def __init__(self):
        self.q = [[],[]]    #其中 0 代表猫，1 代表
        self.order = []

    def enqueue(self, animal: List[int]) -> None:
        self.q[animal[1]].append(animal)
        self.order.append(animal)

    def dequeueAny(self) -> List[int]:
        if len(self.order) == 0: return [-1, -1]
        v = self.order.pop(0)
        return self.q[v[1]].pop(0)

    def dequeueDog(self) -> List[int]:
        if len(self.q[1]) == 0: return [-1, -1]
        re = self.q[1].pop(0)
        idx = 0
        for i in range(len(self.order)):
            if self.order[i][0] == re[0] and self.order[i][1] == re[1]:
                idx = i
                break
        self.order.pop(idx)
        return re

    def dequeueCat(self) -> List[int]:
        if len(self.q[0]) == 0: return [-1, -1]
        re = self.q[0].pop(0)
        idx = 0
        for i in range(len(self.order)):
            if self.order[i][0] == re[0] and self.order[i][1] == re[1]:
                idx = i
                break
        self.order.pop(idx)
        return re


# Your AnimalShelf object will be instantiated and called as such:
obj = AnimalShelf()
# obj.enqueue([0,0])
# obj.enqueue([1,0])
# print(obj.dequeueCat())
# print(obj.dequeueDog())
# print(obj.dequeueAny())

obj.enqueue([0,0])
obj.enqueue([1,0])
obj.enqueue([2,1])
print(obj.dequeueDog())
print(obj.dequeueCat())
print(obj.dequeueAny())


