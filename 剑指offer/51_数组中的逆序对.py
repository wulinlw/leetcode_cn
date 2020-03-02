#!/usr/bin/python
#coding:utf-8

# // 面试题51：数组中的逆序对
# // 题目：在数组中的两个数字如果前面一个数字大于后面的数字，则这两个数字组
# // 成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

import heapq
class Solution:
    # 归并排序
    def InversePairs(self, nums):
        self.cnt = 0
        def merge(nums, start, mid, end, temp):
            i, j = start, mid + 1
            while i <= mid and j <= end:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    self.cnt += mid - i + 1
                    temp.append(nums[j])
                    j += 1
            while i <= mid:
                temp.append(nums[i])
                i += 1
            while j <= end:
                temp.append(nums[j])
                j += 1
            
            for i in range(len(temp)):
                nums[start + i] = temp[i]      #交换了顺序，num变成从小到大排列
            temp.clear()
                    

        def mergeSort(nums, start, end, temp):
            if start >= end: return
            mid = (start + end) >> 1
            mergeSort(nums, start, mid, temp)
            mergeSort(nums, mid + 1, end, temp)
            merge(nums, start, mid,  end, temp)

        mergeSort(nums, 0, len(nums) - 1, [])
        return self.cnt

# 作者：fe-lucifer
# 链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/jian-dan-yi-dong-gui-bing-pai-xu-python-by-azl3979/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。



nums = [7,5,6,4]
obj = Solution()
print(obj.InversePairs(nums))