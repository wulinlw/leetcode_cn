#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#
# https://leetcode-cn.com/problems/insert-interval/description/
#
# algorithms
# Hard (37.11%)
# Likes:    129
# Dislikes: 0
# Total Accepted:    19.7K
# Total Submissions: 53.1K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
# 
# 在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
# 
# 示例 1:
# 
# 输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出: [[1,5],[6,9]]
# 
# 
# 示例 2:
# 
# 输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出: [[1,2],[3,10],[12,16]]
# 解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # O(n*log(n))
    def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:return [newInterval]
        intervals.append(newInterval)                           #直接插入，其他和56题一样O(n*log(n))
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

    # O(n)
    # 由于题目给的区间是排序的，只需要在合适的时机插入newInterval，原理和56题一样
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        re = []
        idx = 0
        while idx < n and newInterval[0] > intervals[idx][0]:   #起点比要插入的小的区间，都写入结果
            re.append(intervals[idx])
            idx += 1

        if not re or re[-1][1] < newInterval[0]:                #处理要插入的，上一个区间在newInterval前已结束就直接写入，不然就更新他的终点
            re.append(newInterval)
        else:
            re[-1][1] = max(re[-1][1], newInterval[1])

        while idx < n:                                          #处理剩下的，和56题一样
            if re[-1][1] < intervals[idx][0]:
                re.append(intervals[idx])
            else:
                re[-1][1] = max(re[-1][1], intervals[idx][1])
            idx += 1
        return re



# @lc code=end
intervals = [[1,3],[6,9]]
newInterval = [2,5]
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
# intervals = [[1,5]]
# newInterval = [2,7]
o = Solution()
print(o.insert(intervals, newInterval))