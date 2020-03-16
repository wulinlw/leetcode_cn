#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#
# https://leetcode-cn.com/problems/add-strings/description/
#
# algorithms
# Easy (49.60%)
# Likes:    142
# Dislikes: 0
# Total Accepted:    25.9K
# Total Submissions: 52.1K
# Testcase Example:  '"0"\n"0"'
#
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
# 
# 注意：
# 
# 
# num1 和num2 的长度都小于 5100.
# num1 和num2 都只包含数字 0-9.
# num1 和num2 都不包含任何前导零。
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
# 
# 
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)
        i, j = l1-1, l2-1
        arr = []
        carry = 0
        while i >=0 or j >= 0:
            a = int(num1[i]) if i>=0 else 0
            b = int(num2[j]) if j>=0 else 0
            sum = a + b + carry
            cur = sum % 10
            carry = 1 if sum>9 else 0
            arr.append(str(cur))
            i -= 1
            j -= 1 
        if carry:
            arr.append("1")
        return "".join(arr[::-1])
        
# @lc code=end

# num1 = "123"
# num2 = "993"
num1 = "1"
num2 = "9"
o  = Solution()
print(o.addStrings(num1, num2))