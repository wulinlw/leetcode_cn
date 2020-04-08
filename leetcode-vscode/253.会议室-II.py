#
# @lc app=leetcode.cn id=399 lang=python3
#
# [253] 会议室 II
#
# https://leetcode-cn.com/problems/
#
# 给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

# 示例 1:
# 输入: [[0, 30],[5, 10],[15, 20]]
# 输出: 2
# 示例 2:
# 输入: [[7,10],[2,4]]
# 输出: 1

# 链接：https://leetcode-cn.com/problems/meeting-rooms-ii

from typing import List
# @lc code=start
class Solution:
    #单调栈
    def minMeetingRooms(self, intervals):
        intervals.sort(key = lambda x:(x[0]))
        # print(intervals)
        stack = []
        for i in range(len(intervals)):
            while stack and stack[-1] <= intervals[i][0]:   #当前开始时间> 之前的结束时间，就可以直接用上一间的会议室了，之前的弹出
                stack.pop()
            stack.append(intervals[i][1])                   #存入会议结束时间
        return len(stack)



        
# @lc code=end

intervals = [[0, 30],[5, 10],[15, 20]]
intervals = [[7,10],[2,4]]
o = Solution()
print(o.minMeetingRooms(intervals))