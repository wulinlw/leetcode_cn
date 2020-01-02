#!/usr/bin/python
#coding:utf-8

# // 面试题39：数组中出现次数超过一半的数字
# // 题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例
# // 如输入一个长度为9的数组{1, 2, 3, 2, 2, 2, 5, 4, 2}。由于数字2在数组中
# // 出现了5次，超过数组长度的一半，因此输出2。
class Solution:
    # 摩尔投票法
    def CheckMoreThanHalf(self, nums):
        if len(nums) == 0:return False
        cur = float('-inf')
        c = 0
        for i in range(len(nums)):
            if c == 0 :
                cur = nums[i]
                c = 1 
            elif cur == nums[i]:
                c += 1
            else:
                c -= 1
        return cur


    # 快排的方法
    def CheckMoreThanHalf2(self, nums):
        n = len(nums)
        start = 0
        end = n-1
        mid = end//2
        index = self.Partition(nums, start, end)
        # print(mid,index)

        # 经过Partition后，比index大的都在index右边，小的都在index左边
        while index != mid:
            if index > mid:                         #大于说明mid在左边，
                end = index-1
            else:
                start = index+1
            index = self.Partition(nums, start, end)
        # print(mid)
        # 不断递归后，中间的数就是众数

        if not self.check(nums, nums[mid]):
            return 
        return nums[mid]

    def check(self, nums, target):
        c = 0
        for i in range(len(nums)):
            if target == nums[i]:
                c+=1
        return c>len(nums)//2

    def Partition(self, nums, low, high):
        i = low-1
        pivot = nums[high]
        for j in range(low, high):
            if nums[j] < pivot:
                i += 1
                nums[i],nums[j] = nums[j],nums[i] 
        nums[i+1],nums[high] = nums[high],nums[i+1]
        return i+1


nums = [1,2,3,2,5,4,2,3,3,3,3,3,3,3,3]
obj = Solution()
re = obj.CheckMoreThanHalf2(nums)
print(re)
