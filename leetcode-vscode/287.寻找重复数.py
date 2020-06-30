#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#
# https://leetcode-cn.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (63.14%)
# Likes:    542
# Dislikes: 0
# Total Accepted:    51K
# Total Submissions: 79.7K
# Testcase Example:  '[1,3,4,2,2]'
#
# 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和
# n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
# 
# 示例 1:
# 
# 输入: [1,3,4,2,2]
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: [3,1,3,4,2]
# 输出: 3
# 
# 
# 说明：
# 
# 
# 不能更改原数组（假设数组是只读的）。
# 只能使用额外的 O(1) 的空间。
# 时间复杂度小于 O(n^2) 。
# 数组中只有一个重复的数字，但它可能不止重复出现一次。
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    # 弗洛伊德 快慢指针
    # 和链表中找环的入口一样
    # O(n)
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]                  #由于 0 不能作为 nums 中的值出现，nums[0] 不能作为循环的一部分。
        while True:
            slow = nums[slow]           
            fast = nums[nums[fast]]     #相当于两次nums[fast]，即快指针走两步
            if slow == fast:            #找到相遇节点，但不一定在入口相遇
                break
        
        ptr1 = nums[0]
        ptr2 = slow
        while ptr1 != ptr2:             #都走一步，会在环的入口相遇
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        return ptr1

    # O(nlog(n))
    def findDuplicate2(self, nums: List[int]) -> int:
        size = len(nums)
        left = 1
        right = size - 1

        while left < right:
            mid = left + (right - left) // 2

            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            # 根据抽屉原理，小于等于 4 的数的个数如果严格大于 4 个，
            # 此时重复元素一定出现在 [1, 4] 区间里

            if cnt > mid:
                # 重复的元素一定出现在 [left, mid] 区间里
                right = mid
            else:
                # if 分析正确了以后，else 搜索的区间就是 if 的反面
                # [mid + 1, right]
                left = mid + 1
        return left


# @lc code=end

nums = [1,3,4,2,2]
o = Solution()
print(o.findDuplicate(nums))
