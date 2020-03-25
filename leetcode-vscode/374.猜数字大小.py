#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#
# https://leetcode-cn.com/problems/guess-number-higher-or-lower/description/
#
# algorithms
# Easy (42.96%)
# Likes:    55
# Dislikes: 0
# Total Accepted:    18.7K
# Total Submissions: 43.3K
# Testcase Example:  '10\n6'
#
# 我们正在玩一个猜数字游戏。 游戏规则如下：
# 我从 1 到 n 选择一个数字。 你需要猜我选择了哪个数字。
# 每次你猜错了，我会告诉你这个数字是大了还是小了。
# 你调用一个预先定义好的接口 guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）：
# 
# -1 : 我的数字比较小
# ⁠1 : 我的数字比较大
# ⁠0 : 恭喜！你猜对了！
# 
# 
# 示例 :
# 
# 输入: n = 10, pick = 6
# 输出: 6
# 
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

# def guess(num):
#     if num==6: 
#         return 0 
#     elif num>6:
#         return 1
#     else:
#         return -1
class Solution:
    #”我的“指出题人。。。
    def guessNumber(self, n: int) -> int:
        l,r = 0,n
        while l<=r:
            mid = l+(r-l)//2
            re = guess(mid)
            if re==0:
                return mid 
            elif re<0:
                r = mid-1 
            else:
                l = mid+1
        return -1

    # def guess(self,num):
    #     if num==6: 
    #         return 0 
    #     elif num>6:
    #         return 1
    #     else:
    #         return -1


        
# @lc code=end

n = 10
pick = 6
o = Solution()
print(o.guessNumber(n))