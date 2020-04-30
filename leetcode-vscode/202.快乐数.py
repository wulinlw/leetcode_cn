#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#
# https://leetcode-cn.com/problems/happy-number/description/
#
# algorithms
# Easy (57.39%)
# Likes:    295
# Dislikes: 0
# Total Accepted:    59.1K
# Total Submissions: 100.9K
# Testcase Example:  '19'
#
# 编写一个算法来判断一个数 n 是不是快乐数。
# 
# 「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到
# 1。如果 可以变为  1，那么这个数就是快乐数。
# 
# 如果 n 是快乐数就返回 True ；不是，则返回 False 。
# 
# 
# 
# 示例：
# 
# 输入：19
# 输出：true
# 解释：
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# 
# 
#
import math
# @lc code=start
class Solution:
    #普通hash
    def isHappy2(self, n: int) -> bool:
        d = {}
        while 1:
            tmp = 0
            while n:
                tmp += math.pow((n % 10), 2)
                n = n // 10
            n = tmp
            if n in d:
                return False
            else:
                d[tmp] = 1
            if n == 1:return True 
    
    #快慢指针，和链表一样
    def isHappy(self, n: int) -> bool:
        def getnext(n):
            sum = 0
            while n:
                n,b = divmod(n, 10)
                sum += b * b
            return sum
        slow, fast = n, n
        while 1:
            slow = getnext(slow)
            fast = getnext(fast)    #快指针走两步，有循环就会相遇
            fast = getnext(fast)
            if slow == fast:
                break
        return slow == 1



# @lc code=end

o = Solution()
print(o.isHappy(19))
print(o.isHappy(2))