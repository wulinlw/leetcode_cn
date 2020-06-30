#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
# https://leetcode-cn.com/problems/sqrtx/description/
#
# algorithms
# Easy (37.57%)
# Likes:    364
# Dislikes: 0
# Total Accepted:    126.8K
# Total Submissions: 335.5K
# Testcase Example:  '4'
#
# 实现 int sqrt(int x) 函数。
# 
# 计算并返回 x 的平方根，其中 x 是非负整数。
# 
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
# 
# 示例 1:
# 
# 输入: 4
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842..., 
# 由于返回类型是整数，小数部分将被舍去。
# 
# 
#

# @lc code=start
class Solution:
    #二分法 O(log(n))
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        re = 0
        while l<=r:
            mid = (l + r) // 2
            if mid * mid <= x:
                re = mid
                l = mid + 1
            else:
                r = mid - 1
        return re

# @lc code=end
x = 4
o = Solution()
print(o.mySqrt(x))