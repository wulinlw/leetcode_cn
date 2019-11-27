#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/learn/card/binary-search/211/template-iii/845/
# 找到 K 个最接近的元素
# 给定一个排序好的数组，两个整数 k 和 x，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。如果有两个数与 x 的差值一样，优先选择数值较小的那个数。

# 示例 1:
# 输入: [1,2,3,4,5], k=4, x=3
# 输出: [1,2,3,4]
 

# 示例 2:
# 输入: [1,2,3,4,5], k=4, x=-1
# 输出: [1,2,3,4]
 

# 说明:
# k 的值为正数，且总是小于给定排序数组的长度。
# 数组不为空，且长度不超过 104
# 数组里的每个元素与 x 的绝对值不超过 104
 
# 更新(2017/9/19):
# 这个参数 arr 已经被改变为一个整数数组（而不是整数列表）。 请重新加载代码定义以获取最新更改。
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # 排除法（双指针）
        size = len(arr)
        left = 0
        right = size - 1

        # 我们要排除掉 size - k 这么多元素
        remove_nums = size - k
        while remove_nums:
            # 调试语句
            print(left, right, k)
            # 注意：这里等于号的含义，题目中说，差值相等的时候取小的
            # 因此相等的时候，尽量缩小右边界
            if x - arr[left] <= arr[right] - x:
                right -= 1
            else:
                left += 1
            remove_nums -= 1
        return arr[left:left + k]



nums = [1,2,3,4,5]
k=4
x=3
ss = Solution()
re = ss.findClosestElements(nums, k, x)
print(re)

