#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/50/sorting-and-searching/100/
# 在排序数组中查找元素的第一个和最后一个位置
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

# 你的算法时间复杂度必须是 O(log n) 级别。
# 如果数组中不存在目标值，返回 [-1, -1]。
# 示例 1:

# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
# 示例 2:

# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        re = [-1,-1]
        if len(nums)==1:
            if nums[0] == target:
                return [0,0]
            else:
                return re

        for i in range(0,len(nums)):
            if nums[i] < target:
                continue
            if nums[i] == target and re[0] == -1:
                re[0] = i
                if i == len(nums)-1:
                    return [i,i]
                for j in range(i+1,len(nums)):
                    if nums[j] == target:
                        re[1] = j
                    else:
                        break
                if re[1] != -1:
                    return re
                elif re[0] != -1 and re[1] == -1:
                    re[1] = re[0]
                    return re
                else:
                    return [-1,-1]
        return re

    # 二分法
    def searchRange2(self, nums, target):
        if not nums:
            return [-1,-1]
        left, right = 0, len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:#刚好找到，但不确定是头还是尾
                l=r=mid
                while l>=0 and nums[l]==target:#向左移动找到头
                    l-=1
                while r<=len(nums)-1 and nums[r]==target:#想右移动找到尾
                    r+=1
                return [l+1,r-1]
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return [-1,-1]


# nums = [5,7,7,8,8,10]
# target = 8
# nums = [5,7,7,8,8,10]
# target = 6
# nums = [2,2]
# target = 2
# nums = [1,3]
# target = 1
nums = [1,3]
target = 3
s = Solution()
r = s.searchRange(nums, target)
print(r)




