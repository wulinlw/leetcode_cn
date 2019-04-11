#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/50/sorting-and-searching/98/
# 数组中的第K个最大元素
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

# 示例 1:
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 示例 2:

# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
# 说明:
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

# https://blog.csdn.net/Strive_0902/article/details/82940456
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 插入排序
        for i in range(1,k):
            for j in range(i,0,-1):
                if nums[j] > nums[j-1]:
                    nums[j],nums[j-1] = nums[j-1],nums[j]
                else:
                    pass
        for i in range(k,len(nums)):
            if nums[i] > nums[k-1]:
                nums[k-1] = nums[i]
                for j in range(k-1,0,-1):
                    if nums[j] > nums[j-1]:
                        nums[j],nums[j-1] = nums[j-1],nums[j]
                    else:
                        pass
        return nums[k-1]



nums = [3,2,1,5,6,4]
k = 2
s = Solution()
r = s.findKthLargest(nums,k)
print(r)




