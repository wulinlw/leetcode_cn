#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/1/array/28/
# 移动零
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

# 示例:

# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 说明:

# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        zeroIndex = False
        moveIndex = []
        f = False
        for i in range(l):
            if nums[i] == 0:
                f = True
                if type(zeroIndex) == bool:
                    zeroIndex = i
            elif f == True:
                moveIndex.append(i)
        # print(zeroIndex)
        # print(moveIndex)
        # sys.exit()
        if type(zeroIndex) == bool:
            return 
        zl = len(moveIndex)
        p = 0
        while(p < zl):
            nums[zeroIndex+p] = nums[moveIndex[p]]
            p +=1
        start = zeroIndex+zl
        while(start<l):
            nums[start] = 0
            start+=1
        
    def moveZeroes2(self, nums):
        # 变量j用来保存已遍历过部位0的值。
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums



nums = [0,1,0,3,12]
s = Solution()
n = s.moveZeroes2(nums)
print('return', n)
