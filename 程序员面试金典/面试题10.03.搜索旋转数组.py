# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题10.03.搜索旋转数组
# 
# https://leetcode-cn.com/problems/search-rotate-array-lcci/
# 
# 搜索旋转数组。给定一个排序后的数组，包含n个整数，但这个数组已被旋转过很多次了，次数不详。请编写代码找出数组中的某个元素，假设数组元素原先是按升序排列的。若有多个相同元素，返回索引值最小的一个。
# 示例1:
# 
#  输入: arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 5
#  输出: 8（元素5在该数组中的索引）
# 
# 
# 示例2:
# 
#  输入：arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 11
#  输出：-1 （没有找到）
# 
# 
# 提示:
# 
# 
# 	arr 长度范围在[1, 1000000]之间
# 
# 
# 
# Medium 39.8%
# Testcase Example: [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
# 5
# 
# 提示:
# 你能为此改进二分查找吗？
# 该算法的运行时间是什么？如果数组有重复，会发生什么？
# 
# 
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:return -1
        left, right = 0, len(nums) - 1
        while left<right:
            mid = (left + right) >> 1
            if nums[left] < nums[mid]:                   # 如果左值小于中值，说明左边区间升序 
                if nums[left] <= target <= nums[mid]:    # 如果目标在左边的升序区间中，右边界移动到mid
                    right = mid
                else:                               # 否则目标在右半边，左边界移动到mid+1
                    left = mid + 1
            elif nums[left] > nums[mid]:                 # 如果左值大于中值，说明左边不是升序，右半边升序
                if nums[left] <= target or target <= nums[mid]:# 如果目标在左边，右边界移动到mid
                    right = mid
                else:
                    left = mid + 1                     # 否则目标在右半边的升序区间中，左边界移动到mid+1
            elif nums[left] == nums[mid]:                # 如果左值等于中值，可能是已经找到了目标，也可能是遇到了重复值
                if nums[left] != target:
                    left += 1
                else:                               # 如果左值等于目标，说明已经找到最左边的目标值
                    right = left
        return left if nums[left] == target else -1

  



strs = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
target = 5
strs = [5,5,5,1,2,3,4,5]
target = 5
o = Solution()
print(o.search(strs, target))