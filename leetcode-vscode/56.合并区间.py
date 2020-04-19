#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
# https://leetcode-cn.com/problems/merge-intervals/description/
#
# algorithms
# Medium (40.44%)
# Likes:    357
# Dislikes: 0
# Total Accepted:    72.1K
# Total Submissions: 174.8K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 给出一个区间的集合，请合并所有重叠的区间。
# 
# 示例 1:
# 
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 
# 
# 示例 2:
# 
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
# 
#
from typing import List
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:return []
        intervals.sort(key=lambda x:x[0])           #起点排序
        stack = [intervals[0]]
        re = []
        for i in range(1, len(intervals)):
            if intervals[i][0] > stack[-1][1]:      #当前起点大于前一个区间终点，前一个弹出，新的加入stack
                re.append(stack.pop())
                stack.append(intervals[i])
            elif intervals[i][1] > stack[-1][1]:    #线段有重叠就对比终点，新的终点更长则替换
                stack[-1][1] = intervals[i][1]
        if stack:                                   #最后剩下一个在stack中
            re.append(stack.pop())
        return re
    
    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged




# @lc code=end
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[4,5]]
intervals = [[1,4],[0,4]]
intervals = [[1,4],[2,3]]
o = Solution()
print(o.merge(intervals))