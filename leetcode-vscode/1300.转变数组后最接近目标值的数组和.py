#
# @lc app=leetcode.cn id=1300 lang=python3
#
# [1300] 转变数组后最接近目标值的数组和
#
# https://leetcode-cn.com/problems/sum-of-mutated-array-closest-to-target/description/
#
# algorithms
# Medium (45.67%)
# Likes:    50
# Dislikes: 0
# Total Accepted:    4.9K
# Total Submissions: 10.4K
# Testcase Example:  '[4,9,3]\n10'
#
# 给你一个整数数组 arr 和一个目标值 target ，请你返回一个整数 value ，使得将数组中所有大于 value 的值变成 value
# 后，数组的和最接近  target （最接近表示两者之差的绝对值最小）。
# 
# 如果有多种使得和最接近 target 的方案，请你返回这些整数中的最小值。
# 
# 请注意，答案不一定是 arr 中的数字。
# 
# 
# 
# 示例 1：
# 
# 输入：arr = [4,9,3], target = 10
# 输出：3
# 解释：当选择 value 为 3 时，数组会变成 [3, 3, 3]，和为 9 ，这是最接近 target 的方案。
# 
# 
# 示例 2：
# 
# 输入：arr = [2,3,5], target = 10
# 输出：5
# 
# 
# 示例 3：
# 
# 输入：arr = [60864,25176,27249,21296,20204], target = 56803
# 输出：11361
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr.length <= 10^4
# 1 <= arr[i], target <= 10^5
# 
# 
#
from typing import List
import bisect
# @lc code=start
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()                                      #先排序，这样找到大于target的值后，后面的值
        n = len(arr)
        pre = [0]
        for num in arr:                                 #计算前缀和，方便后面计算所有和
            pre.append(pre[-1] + num)
        
        l, r = 0, max(arr)                              #value的左右边界
        re = -1
        while l <= r:
            mid = (l + r) // 2
            idx = bisect.bisect_left(arr, mid)          #插到原数组的索引
            cur = pre[idx] + (n - idx) * mid            #之前的和+后面都变为mid之后的和，剩余长度是n-idx
            if cur < target:                            #小则l右移1，大则r左移1
                l = mid + 1
                re = mid
            else:
                r = mid - 1
        
        def check(x):                                   #计算数组和，大于x的变为x
            re = 0
            for num in arr:
                if num >= x:
                    re += x
                else:
                    re += num
            return re

        small = check(re)                               #计算re和re+1，哪个更接近target，返回最接近的
        big = check(re + 1)
        if abs(small - target) <= abs(big - target):
            return re
        else:
            return re + 1



# @lc code=end

arr = [4,9,3]
target = 10
arr = [2,3,5]
target = 10
o = Solution()
print(o.findBestValue(arr, target))