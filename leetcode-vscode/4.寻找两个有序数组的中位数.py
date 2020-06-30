#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (36.94%)
# Likes:    2624
# Dislikes: 0
# Total Accepted:    193.7K
# Total Submissions: 512.7K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
# 
# 请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
# 
# 你可以假设 nums1 和 nums2 不会同时为空。
# 
# 
# 
# 示例 1:
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# 则中位数是 2.0
# 
# 
# 示例 2:
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# 则中位数是 (2 + 3)/2 = 2.5
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # 第一种方法是合并数组，找到中位数，时间空间都是是O(m+n)

    # 二分查找
    # 不用合并，只需要移动指针指向中位数的位置
    # 问题就转换成取第k小的元素
    # m+n奇数时，中位数位置m+n//2, 偶数时取中间2个数的平均值(m+n//2 + m+n//2+1)/2
    # https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-s-114/
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k):
            idx1, idx2 = 0, 0                                               #2个数组的索引
            while True:
                if idx1 == l1:                                              #一个数组指向最后了，剩余的k从另一个数组取，每次循环剩余k都会变小，-1是从左边取
                    return nums2[idx2 + k - 1]
                if idx2 == l2:
                    return nums1[idx1 + k - 1]
                if k == 1:
                    return min(nums1[idx1], nums2[idx2])                    #k剩下最后一个时，取较小的那个数

                newindex1 = min(idx1 + k//2 -1, l1-1)                       #指针指向的那个数，原始指针+剩余长度二分处的索引， 需要和数组长度对比，避免越界
                newindex2 = min(idx2 + k//2 -1, l2-1)
                pivot1, pivot2 = nums1[newindex1], nums2[newindex2]
                if pivot1 <= pivot2:                                        #第一个数组数值<= ,舍弃他左边的(包含当前值)
                    k -= newindex1 - idx1 + 1                               #剩余的k，舍弃第一个数组左边
                    idx1 = newindex1 + 1                                    #更新新索引到右边一个
                else:
                    k -= newindex2 - idx2 + 1
                    idx2 = newindex2 + 1 


        l1, l2 = len(nums1), len(nums2)
        lenSum = l1 + l2
        if lenSum % 2 == 1:                                                 #奇数取中间的数，偶数取中间2个数的平均值
            return getKthElement((lenSum+1) // 2)
        else:
            return (getKthElement(lenSum // 2) + getKthElement(lenSum // 2 + 1)) / 2



# @lc code=end
nums1 = [1, 3]
nums2 = [2]
nums1 = [1, 2]
nums2 = [3, 4]
o = Solution()
print(o.findMedianSortedArrays(nums1, nums2))