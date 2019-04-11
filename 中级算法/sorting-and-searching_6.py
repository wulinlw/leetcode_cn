#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/50/sorting-and-searching/101/
# 合并区间
# 给出一个区间的集合，请合并所有重叠的区间。

# 示例 1:

# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2:

# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)
 
        merged = []
        for interval in intervals:
            if not merged or merged[-1].end < interval.start: #如果当前merged为空或者当前项与最后一项连接不上，直接添加
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end) #如果能连接上我们就连
            # print(self.dump(merged))
        
        return merged

    def build(self,nums):
        re = []
        for i in nums:
            re.append(Interval(i[0], i[1]))
        return re
    
    def dump(self,nums):
        re = []
        for i in nums:
            re.append([i.start, i.end])
        return re



l = [[1,3],[2,6],[8,10],[15,18]]
s = Solution()
intervals = s.build(l)
r = s.merge(intervals)
r2 = s.dump(r)
print(r2)




