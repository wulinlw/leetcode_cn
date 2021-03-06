#!/usr/bin/python
#coding:utf-8

# // 面试题51：数组中的逆序对
# // 题目：在数组中的两个数字如果前面一个数字大于后面的数字，则这两个数字组
# // 成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
from typing import List
import bisect
class Solution:
    # 归并排序
    # https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/jian-dan-yi-dong-gui-bing-pai-xu-python-by-azl3979/
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
            merge(nums, start, mid,  end, temp) #合并的时候，因为要算逆序对，会从起点和中点开始向右走，所以要传mid

        mergeSort(nums, 0, len(nums) - 1, [])
        return self.cnt

    # 二分插入
    def InversePairs2(self, nums: List[int]) -> int:
        cnt, tmp = 0, []
        for num in nums[::-1]:
            cnt += bisect.bisect_left(tmp, num)#二分插入，计算已有列表(后面的先插入)比num小的数字
            bisect.insort(tmp, num)
        return cnt


nums = [7,5,6,4]
obj = Solution()
print(obj.InversePairs(nums))