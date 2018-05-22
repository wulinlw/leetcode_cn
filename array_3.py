#!/usr/bin/python
#coding:utf-8
class Solution(object):
    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        每次向右移动一位，右边最大的放入tmp，依次向右移动，最后将tmp放入最左边，重复K次
        测试用例如果太大，会超时
        """
        l = len(nums)
        if l == 1:
            return
        p = k % l
        if p > 0:
            while (p > 0):
                tmp = nums[l - 1]
                for i in range(l):
                    nums[l - i - 1] = nums[l - i - 2]
                nums[0] = tmp
                p -= 1
        print(nums)

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        先反转所有，在反转0-(k-1)和k-len(nums)
        """
        l = len(nums)
        k = k % l
        self.reversal(nums, 0, l - 1)
        self.reversal(nums, 0, k - 1)
        self.reversal(nums, k, l - 1)

    def reversal(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
# nums = [5,6,7,1,2,3,4]
# nums = [1,2]
# k = 3

s = Solution()
n = s.rotate(nums, k)
print(nums)