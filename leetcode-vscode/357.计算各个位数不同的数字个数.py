#
# @lc app=leetcode.cn id=357 lang=python3
#
# [357] 计算各个位数不同的数字个数
#
# https://leetcode-cn.com/problems/count-numbers-with-unique-digits/description/
#
# algorithms
# Medium (50.35%)
# Likes:    52
# Dislikes: 0
# Total Accepted:    7.4K
# Total Submissions: 14.6K
# Testcase Example:  '2'
#
# 给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10^n 。
# 
# 示例:
# 
# 输入: 2
# 输出: 91 
# 解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。
# 
# 
#

# @lc code=start
class Solution:   
    # 回溯
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        import functools
        visited = set()
        @functools.lru_cache(None)
        def helper(d):                      #d 几位数
            if d == n: return 1
            res = 1
            for i in range(1 if d == 0 else 0, 10):
                if i not in visited:
                    visited.add(i)
                    res += helper(d + 1)
                    visited.remove(i)
            return res

        return helper(0)

    # 规律
    # n=1: res=10
    # n=2: res=9*9+10=91 # 两位数第一位只能为1-9，第二位只能为非第一位的数，加上一位数的所有结果
    # n=3: res=9 * 9 * 8+91=739 # 三位数第一位只能为1-9，第二位只能为非第一位的数，第三位只能为非前两位的数，加上两位数的所有结果
    # n=4: res=9 * 9 * 8 * 7+739=5275 # 同上推法
    def countNumbersWithUniqueDigits2(self, n: int) -> int:
        if not n:
            return 1
        res = 10    #1位数10种
        muls = 9    #大于1位的，第一位只能取0-9的9个数
        for i in range(1, min(n,10)):   #n>10以后答案都不变了，因为11位数不可能各个位数都不同
            muls *= 10 - i              #第二位只能取除了第一位以外的9个，在后面就只能取8，7，6...
            res += muls                 #加上之前的总数
        return res


# @lc code=end

n = 2
n = 1
n = 3
o = Solution()
print(o.countNumbersWithUniqueDigits(n))