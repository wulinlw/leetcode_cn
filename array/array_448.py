#!/usr/bin/python
#coding:utf-8

# 448. 找到所有数组中消失的数字
# 给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
# 找到所有在 [1, n] 范围之间没有出现在数组中的数字。
# 您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。
# 示例
# 输入:
# [4,3,2,7,8,2,3,1]

# 输出:
# [5,6]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
class Solution(object):
    def findDisappearedNumbers(self, nums):
        # 这个交换是为了不用新的变量
        # def swap(nums, i1, i2):
        #     if i1 == i2:
        #         return
        #     nums[i1] = nums[i1] ^ nums[i2]
        #     nums[i2] = nums[i1] ^ nums[i2]
        #     nums[i1] = nums[i1] ^ nums[i2]


        for i in range(len(nums)):
            while  nums[i] != nums[nums[i]-1]:
                # 这样交换是错的，变量计算过程中已经变了
                # nums[i],nums[nums[i]-1] = nums[nums[i]-1],nums[i]
                tmp = nums[i]-1
                nums[i],nums[tmp] = nums[tmp],nums[i]
        re = []
        for i, num in enumerate(nums):
            if num != i + 1:
                re.append(i + 1)
        return re



nums = [4,3,2,7,8,2,3,1]
obj = Solution()
n = obj.findDisappearedNumbers(nums)
print('return', n)

