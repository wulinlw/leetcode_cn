#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
# https://leetcode-cn.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (48.02%)
# Likes:    313
# Dislikes: 0
# Total Accepted:    36.9K
# Total Submissions: 75.8K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# 给定一个未排序的整数数组，找出最长连续序列的长度。
# 
# 要求算法的时间复杂度为 O(n)。
# 
# 示例:
# 
# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
# 
#
from typing import List
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxlen, curlen = 0, 0
        h = set(nums)                           #hash保存，查找O(1)
        for num in h:
            if num - 1 not in h:                #num-1不在h中，已这样的数据为开始， 如果在h中，说明它已经被其他的循环中处理了
                curlen = 1
                while num + 1 in h:             #一直找，破纪录了就更新
                    num += 1
                    curlen += 1
                maxlen = max(maxlen, curlen)
        return maxlen


# @lc code=end
nums = [100,4,200,1,3,2]
o = Solution()
print(o.longestConsecutive(nums))
