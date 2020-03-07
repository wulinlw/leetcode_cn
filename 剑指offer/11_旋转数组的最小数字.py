#!/usr/bin/python
#coding:utf-8

# 旋转数组的最小数字
# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
# NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

class Solution:
    #书上的思路
    def minNumberInRotateArray(self, nums):
        n = len(nums)
        if n == 0: return 0

        def minInOrder(nums, l, r):
            re = nums[l]
            for i in range(l+1, r+1):
                if re>nums[i]:
                    re = nums[i]
            return re

        l = 0
        r = n-1
        mid = l
        if nums[0] < nums[r]:#没有反转
            return nums[0]
        while nums[l]>=nums[r]:                #l后面是r时结束循环，找到旋转点r
            if r-l==1:
                mid = r
                break
            mid = (l+r)//2
            if nums[mid] == nums[l] and nums[mid] == nums[r]:# 极端情况,左=中=右，全部扫描一遍[1,0,1,1,1]
                return minInOrder(nums, l, r)
            if nums[mid] >= nums[l]:
                l = mid
            elif nums[mid] <= nums[r]:
                r = mid
        return nums[mid]


    #以此答案为准
    def minArray(self, numbers: [int]) -> int:
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]: i = m + 1   #大于时，向右推进
            elif numbers[m] < numbers[j]: j = m     #小于时，j=mid
            else: j -= 1                            #等于时，想左推进
        return numbers[i]


        
nums = [3,4,5,1,2]
obj = Solution()
# print(obj.minNumberInRotateArray(nums))
# print(obj.minNumberInRotateArray([1,0,1,1,1]))
# print(obj.minNumberInRotateArray([1,1,1,0,1]))
# print(obj.minNumberInRotateArray([1,1,1]))
# print(obj.minNumberInRotateArray([3,1,1]))
# print("\n")

print(obj.minArray([3,4,5,1,2]))
print(obj.minArray([1,0,1,1,1]))
print(obj.minArray([1,1,1,0,1]))
print(obj.minArray([1,1,1]))
print(obj.minArray([3,1,1]))