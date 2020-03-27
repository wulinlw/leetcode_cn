#
# @lc app=leetcode.cn id=914 lang=python3
#
# [914] 卡牌分组
#
# https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards/description/
#
# algorithms
# Easy (32.96%)
# Likes:    100
# Dislikes: 0
# Total Accepted:    15.2K
# Total Submissions: 43.3K
# Testcase Example:  '[1,2,3,4,4,3,2,1]'
#
# 给定一副牌，每张牌上都写着一个整数。
# 
# 此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：
# 
# 
# 每组都有 X 张牌。
# 组内所有的牌上都写着相同的整数。
# 
# 
# 仅当你可选的 X >= 2 时返回 true。
# 
# 
# 
# 示例 1：
# 
# 输入：[1,2,3,4,4,3,2,1]
# 输出：true
# 解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]
# 
# 
# 示例 2：
# 
# 输入：[1,1,1,2,2,2,3,3]
# 输出：false
# 解释：没有满足要求的分组。
# 
# 
# 示例 3：
# 
# 输入：[1]
# 输出：false
# 解释：没有满足要求的分组。
# 
# 
# 示例 4：
# 
# 输入：[1,1]
# 输出：true
# 解释：可行的分组是 [1,1]
# 
# 
# 示例 5：
# 
# 输入：[1,1,2,2,2,2]
# 输出：true
# 解释：可行的分组是 [1,1]，[2,2]，[2,2]
# 
# 
# 
# 提示：
# 
# 
# 1 <= deck.length <= 10000
# 0 <= deck[i] < 10000
# 
# 
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def hasGroupsSizeX2(self, deck: List[int]) -> bool:
        import collections
        if len(deck)<=1:return False
        c = collections.Counter(deck)                   #每个数字计数
        for x in range(2, len(deck)+1):                 #从2开始
            if len(deck)%x==0:                          #长度能整除才有机会true
                if all(i % x == 0 for i in c.values()): #所有数字个数都能被x整除，就可以分组完成
                    return True
        return False

    def hasGroupsSizeX(self, deck: List[int]) -> bool: 
        import functools,collections
        def gcd(a, b):
            return b if a==0 else gcd(b%a, a)
        c = collections.Counter(deck)
        return functools.reduce(gcd, c.values()) >= 2






# @lc code=end

deck = [1,2,3,4,4,3,2,1]
# deck = [1]
deck = [1,1]
o = Solution()
print(o.hasGroupsSizeX(deck))