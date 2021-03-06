#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/8/sorting-and-searching/52/
# 合并两个有序数组
# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
# 说明:
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
# 示例:
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# 输出: [1,2,2,3,5,6]


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        count = 0     #nums2索引
        index = 0     #nums1索引
        while count<n:    #判断条件(nums2长度)
            if nums1[index]>nums2[count]:      #nums2中元素插入nums1中有效部分(非0部分)
                # for i in range(m+count,index,-1):    #注释的两行和注释下面一行效果相同
                #     nums1[i] = nums1[i-1]
                nums1[index+1:m+count+1] = nums1[index:m+count]
                nums1[index] = nums2[count]
                count += 1
            if index > m+count-1:              #nums2中元素插入nums1列表后面全0区域
                nums1[index] = nums2[count]
                count += 1
            index += 1
    
    #从右往左遍历，向长的后面插最大值
    def merge2(self, nums1, m, nums2, n):
        while m>0 and n>0:
            if nums1[m-1]>nums2[n-1]:#若nums1中最后一个元素大于nums2[]中最后一个元素
                nums1[m+n-1]=nums1[m-1]#则扩展后的列表最后一个元素是俩元素中最大的
                m-=1       #nums1中元素-1
            else:
                nums1[m+n-1]=nums2[n-1]
                n-=1
            print(nums1)
        if n>0:#若nums1完了，nums2还没完
            nums1[:n]=nums2[:n]#把剩下nums2加在最开始
        return nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

nums1 = [3,4,5,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
s = Solution()
deep = s.merge2(nums1, m, nums2, n)
print("deep:",deep)