#!/usr/bin/python
#coding:utf-8

# 旋转数组的最小数字
# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
# NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

class Solution:
    def minNumberInRotateArray(self, nums):
        n = len(nums)
        if n == 0: return 0
        l = 0
        r = n-1
        minVal = nums[0]
        if nums[0] < nums[r]:#没有反转
            return nums[0]
        while r-l>1:
            mid = (r-l)//2+l
            if nums[mid] > nums[r]:
                l = mid
            elif nums[mid] < nums[r]:
                r = mid
            elif nums[mid] == nums[l] and nums[mid] == nums[r]:
                # 极端情况,左=中=右，全部扫描一遍
                # [1,0,1,1,1]
                # [1,1,1,0,1]
                for i in range(1, n):
                    if nums[i] < minVal:
                        minVal = nums[i]
                        r = i#终止后r指向返回值
        minVal = nums[r]
        return minVal
        
nums = [3,4,5,1,2]
obj = Solution()
print(obj.minNumberInRotateArray(nums))
print(obj.minNumberInRotateArray([1,0,1,1,1]))
print(obj.minNumberInRotateArray([1,1,1,0,1]))