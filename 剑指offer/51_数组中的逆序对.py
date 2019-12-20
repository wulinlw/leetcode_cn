#!/usr/bin/python
#coding:utf-8

# // 面试题51：数组中的逆序对
# // 题目：在数组中的两个数字如果前面一个数字大于后面的数字，则这两个数字组
# // 成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

import heapq
class Solution:
    # 归并排序
    def InversePairs(self, nums):
        n = len(nums)
        if n == 0:return 0
        new = [0] * n
        re = self.core(nums, new, 0, n-1)
        return re
    
    def core(self, nums, new, start, end):
        if start == end:
            new[start] = nums[start]
            return 0
        length = (end - start) //2
        left = self.core(nums, new ,start, start+length)    #不断归并排序左边
        right = self.core(nums, new, start+length+1, end)   

        # 上面已经完成了各个分段的排序，下面开始归并
        i = start + length
        j = end
        p = end
        count = 0
        while i>=start and j>=start+length+1:
            if nums[i]>nums[j]:
                new[p] = nums[i]                    #大的放到新数组中，从后往前放
                count += j-start-length             #左边大于右边，说明有逆序，
                i -= 1                              #逆序的个数等于分割点mid到end的长度
            else:
                new[p] = nums[j]
                j -= 1
            p -= 1
        while i>=start:                             #处理剩余部分，实际只有一个会while生效，因为总有一边会处理完
            new[p] = nums[i]
            p -= 1
            i -= 1
        while j>=start+length+1:
            new[p] = nums[j]
            p -= 1
            j -= 1
        
        for i in range(start, end+1):               #归并完成，需要重新给num赋值，因为有回溯
            nums[i] = new[i]
        # print(new,nums)
        return left+right+count



nums = [7,5,6,4]
obj = Solution()
print(obj.InversePairs(nums))