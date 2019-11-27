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


# https://leetcode-cn.com/problems/task-scheduler/solution/python-xiang-jie-by-jalan/
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # 计算每个任务出现的次数
        # 找出出现次数最多的任务，假设出现次数为 x
        # 计算至少需要的时间 (x - 1) * (n + 1)，记为 min_time
        # 计算出现次数为 x 的任务总数 count，计算最终结果为 min_time + count
        length = len(tasks)
        if length <= 1:
            return length
        
        # 用于记录每个任务出现的次数
        task_map = dict()
        for task in tasks:
            task_map[task] = task_map.get(task, 0) + 1
        # print(task_map)
        # 按任务出现的次数从大到小排序
        task_sort = sorted(task_map.items(), key=lambda x: x[1], reverse=True)
        # print(task_sort)
        # 出现最多次任务的次数
        max_task_count = task_sort[0][1]
        # 至少需要的最短时间
        res = (max_task_count - 1) * (n + 1)
        
        for sort in task_sort:
            if sort[1] == max_task_count:
                res += 1
        
        # 如果结果比任务数量少，则返回总任务数
        return res if res >= length else length


        

tasks = ["A","A","A","B","B","B"]
n = 2
s = Solution()
n = s.leastInterval(tasks, n)
print(n)


