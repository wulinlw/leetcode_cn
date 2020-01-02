#!/usr/bin/python
#coding:utf-8

# // 面试题40：最小的k个数
# // 题目：输入n个整数，找出其中最小的k个数。例如输入4、5、1、6、2、7、3、8
# // 这8个数字，则最小的4个数字是1、2、3、4。
import heapq
class Solution:
    def GetLeastNumbers(self, nums, k):
        start = 0
        end = len(nums)-1
        index = self.partition(nums, start, end)
        # print(index, nums)
        while index != k-1:
            if index > k-1:                 #索引需要的值，往左缩小范围
                end = index-1
            else:
                start = index+1             #不够K个数，继续往右扩大范围，由于前面的都排好了，这里index+1设为新的开始排序点
            index = self.partition(nums, start, end)
        return nums[:k]

    def partition(self, nums, start, end):
        i = start-1
        pivot = nums[end]
        for j in range(start, end):
            if nums[j] < pivot:
                i += 1
                nums[i],nums[j] = nums[j],nums[i]
        nums[i+1],nums[end] = nums[end],nums[i+1]
        # print(nums, i+1)
        return i+1

    def GetLeastNumbers2(self, nums, k):
        tmp = []
        re = []
        for i in nums:
            heapq.heappush(tmp, -i) #用负号存值,这样下面pop时就可以pop掉十几的最大值
            if len(tmp)>k:
                heapq.heappop(tmp)
        # print(tmp,re)
        for i in tmp[::-1]:         #倒序后用-号，得到从小到大的re
            re.append(-i)
        re.sort()
        return re


nums = [4,5,1,6,2,7,3,8]
k = 4
obj = Solution()
re = obj.GetLeastNumbers(nums, k)
print(re)

# re = obj.GetLeastNumbers2(nums, k)
# print(re)

# a = []
# for i in nums:
#     heapq.heappush(a, -i)
# print(a)