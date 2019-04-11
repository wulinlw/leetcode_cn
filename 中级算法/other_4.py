#!/usr/bin/python
#coding:utf-8


# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/54/others/122/
# Task Scheduler
# 给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。

# 然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。
# 你需要计算完成所有任务所需要的最短时间。
# 示例 1：
# 输入: tasks = ["A","A","A","B","B","B"], n = 2
# 输出: 8
# 执行顺序: A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
# 注：

# 任务的总个数为 [1, 10000]。
# n 的取值范围为 [0, 100]。


# https://blog.csdn.net/xiaoxiaoley/article/details/79159125
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        output = [0]*26
        for i in tasks:
            output[ord(i)-ord('A')] = output[ord(i)-ord('A')]+1
 
        count = 0
        len_o = 0
        max_o = max(output)
        for i in output:
            if i==max_o:
                count = count+1
                    
        return max(len(tasks),(max_o-1)*(n+1)+count)
        

tasks = ["A","A","A","B","B","B"]
n = 2
s = Solution()
n = s.leastInterval(tasks, n)
print(n)


