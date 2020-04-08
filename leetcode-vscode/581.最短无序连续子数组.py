#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#
# https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/description/
#
# algorithms
# Easy (34.02%)
# Likes:    266
# Dislikes: 0
# Total Accepted:    22.6K
# Total Submissions: 65.5K
# Testcase Example:  '[2,6,4,8,10,9,15]'
#
# 给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
# 
# 你找到的子数组应是最短的，请输出它的长度。
# 
# 示例 1:
# 
# 
# 输入: [2, 6, 4, 8, 10, 9, 15]
# 输出: 5
# 解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
# 
# 
# 说明 :
# 
# 
# 输入的数组长度范围在 [1, 10,000]。
# 输入的数组可能包含重复元素 ，所以升序的意思是<=。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    #单调栈
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l, r = float('inf'), float('-inf')
        stack = []
        for i in range(len(nums)):                      #从左边找第一个逆序的位置l
            while stack and nums[stack[-1]] > nums[i]:
                l = min(l, stack.pop())
            stack.append(i)
        stack.clear()
        for i in range(len(nums)-1, -1, -1):            #从右边找第一个逆序的位置r
            while stack and nums[stack[-1]] < nums[i]: 
                r = max(r, stack.pop())
            stack.append(i)
        return r-l+1 if r-l>0 else 0
    
    #方法二
    #排序后从左边找到第一个不相等的位置
    #右边同理
        
# @lc code=end
nums = [2, 6, 4, 8, 10, 9, 15]
nums = [1,3,2,2,2]#4
o = Solution()
print(o.findUnsortedSubarray(nums))