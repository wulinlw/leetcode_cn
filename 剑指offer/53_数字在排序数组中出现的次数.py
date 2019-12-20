#!/usr/bin/python
#coding:utf-8

# // 面试题53（一）：数字在排序数组中出现的次数
# // 题目：统计一个数字在排序数组中出现的次数。例如输入排序数组{1, 2, 3, 3,
# // 3, 3, 4, 5}和数字3，由于3在这个数组中出现了4次，因此输出4。

class Solution:
    def GetNumberOfK(self, nums, k):
        n = len(nums)
        if n==0 or k<=0:return False
        first = self.getFirstK(nums, k, 0, n-1)
        print(first)
        last = self.getLastK(nums, k, 0, n-1)
        if first>=0 and last>=0:
            return last-first+1

    def getFirstK(self, nums, k, start, end):
        if start>end:
            return -1
        mid = (start+end)//2
        if nums[mid] == k:
            if (mid>0 and nums[mid-1] != k) or (mid==0):
                return mid
            else:
                end = mid -1
        elif nums[mid]>k:
            end = mid-1
        else:
            start = mid+1
        print(mid,start,end )
        return self.getFirstK(nums, k, start, end)

    def getLastK(self, nums, k, start, end):
        if start>end:
            return -1
        mid = (start+end)//2
        if nums[mid] == k:
            if (mid<len(nums) and nums[mid+1] != k) or (mid==(len(nums)-1)):
                return mid
            else:
                start = mid +1
        elif nums[mid]>k:
            end = mid-1
        else:
            start = mid+1
        return self.getLastK(nums, k, start, end)


nums = [1,2,3,3,3,3,4,5]
k = 3
obj = Solution()
print(obj.GetNumberOfK(nums, k))