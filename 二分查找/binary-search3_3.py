#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/learn/card/binary-search/210/template-ii/842/
# 寻找旋转排序数组中的最小值
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。

# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

# 请找出其中最小的元素。

# 你可以假设数组中不存在重复元素。

# 示例 1:

# 输入: [3,4,5,1,2]
# 输出: 1
# 示例 2:

# 输入: [4,5,6,7,0,1,2]
# 输出: 0
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        # e.g. 1 < 2 < 3 < 4 < 5 < 7. Already sorted array.
        # 正常旋转后的数组，第一个总比最后一个大
        if nums[right] > nums[0]:
            return nums[0]

        # Binary search way
        while right >= left:
            # Find the mid element
            mid = left + (right - left) / 2
            # 前后两段都是升序的，如果当前值大于后一个，说明下一个是后段的头
            # 这里需要注意，需要对比mid的前一个和后一个
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[0]:#mid在前半段 
                left = mid + 1
            else:
                right = mid - 1

        

rooms = [[1],[2],[3],[]]
rooms = [[1,3],[3,0,1],[2],[0]]
ss = Solution()
re = ss.updateMatrix(rooms)
print(re)

