#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/top-interview-questions-medium/50/sorting-and-searching/96/
# 颜色分类
# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

# 注意:
# 不能使用代码库中的排序函数来解决这道题。

# 示例:
# 输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]
# 进阶：

# 一个直观的解决方案是使用计数排序的两趟扫描算法。
# 首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
# 你能想出一个仅使用常数空间的一趟扫描算法吗？
# O(n)

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 三指针：如果只有两种颜色，那么很容易想到一前一后两个指针向中间遍历，颜色不对就交换位置。三种颜色仍然可以这么做，只不过要多一个指针，前后两个指针用来分隔已经排好的红色和蓝色，中间的指针来遍历元素： 
        # 如果是红色，那么和前指针交换，并两个一起向后移，前指针换过来的一定是白色的，因为中指针已经扫描过那些元素了 
        # 如果是白色，那么继续向后移 
        # 如果是蓝色，那么和后指针交换，后指针向前移，中指针不能后移，因为此时不确定换过来的元素是什么颜色
        left = mid = 0
        right = len(nums) - 1
        while mid <= right:
            print(left,mid,right,nums)
            if nums[mid] == 0:#红色向左交换
                nums[mid], nums[left] = nums[left], nums[mid]
                left += 1
                mid += 1
            elif nums[mid] == 1:#白色向后移动指针
                mid += 1
            else:#蓝色向右交换，但是中指针不动
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
            

        

nums = [2,0,2,1,1,0,2]
s = Solution()
r = s.sortColors(nums)
print(r)




