# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题10.11.峰与谷
# 
# https://leetcode-cn.com/problems/peaks-and-valleys-lcci/
# 
# 在一个整数数组中，&ldquo;峰&rdquo;是大于或等于相邻整数的元素，相应地，&ldquo;谷&rdquo;是小于或等于相邻整数的元素。例如，在数组{5, 8, 6, 2, 3, 4, 6}中，{8, 6}是峰， {5, 2}是谷。现在给定一个整数数组，将该数组按峰与谷的交替顺序排序。
# 示例:
# 
# 输入: [5, 3, 1, 2, 3]
# 输出: [5, 1, 3, 2, 3]
# 
# 
# 提示：
# 
# 
# 	nums.length <= 10000
# 
# 
# 
# Medium 64.7%
# Testcase Example: [3,5,2,1,6,4]
# 
# 提示:
# 假设数组按升序排序。有什么办法可以把它调整为交替的高峰和低谷？
# 尝试遍历排序的数组。你可以交换元素直到将数组调整好吗？
# 请注意，如果确保山峰位置正确，那么山谷也会在正确位置。因此，对数组x的迭代可以跳过每一个其他元素。
# 你是否一定要对数组进行排序？你可以用一个未排序的数组来做到这一点吗？
# 假设你有{0, 1, 2}三个元素的序列，以任意顺序排列。写出这些元素所有可能的排列，以及如何把它们变成1是波峰的形式。
# 重新访问你刚才写出的{0, 1, 2}序列。想象一下有元素在最左边的元素之前。你能确保交换元素的方式不会使数组的前一部分失效吗？
# 你应该可以设计一个O(n) 的算法。
# 
# 
from typing import List
class Solution:
    # 按照峰-谷-峰的顺序排列数组
    # 如果i为峰的位置，则判断当前位置是否小于前一个位置（前一个为谷），若小于，则交换，大于则不处理。
    # 如果i为谷的位置，则判断当前位置是否大于前一个位置（前一个为峰），若大于，则交换，大于则不处理。
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            if (i&1 == 0 and nums[i] < nums[i-1]) or (i&1 == 1 and nums[i] > nums[i-1]):    #奇数位，比前面小，或 偶数位比前面大
                nums[i], nums[i-1] = nums[i-1], nums[i]



nums = [5, 3, 1, 2, 3]
o = Solution()
print(o.wiggleSort(nums))
print(nums)