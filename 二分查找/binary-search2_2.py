#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/learn/card/binary-search/209/template-i/837/
# 猜数字大小
# 我们正在玩一个猜数字游戏。 游戏规则如下：
# 我从 1 到 n 选择一个数字。 你需要猜我选择了哪个数字。
# 每次你猜错了，我会告诉你这个数字是大了还是小了。
# 你调用一个预先定义好的接口 guess(int num)，它会返回 3 个可能的结果（-1，1 或 0）：

# -1 : 我的数字比较小
#  1 : 我的数字比较大
#  0 : 恭喜！你猜对了！
# 示例 :

# 输入: n = 10, pick = 6
# 输出: 6
def guess(num):
    pass
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            # mid = left + (right - left) // 2
            mid = (left + right) >> 1#左移乘2，右移除2
            if guess(mid) == 1:
                # 中位数比猜的数小，因此比中位数小的数包括中位数都不是目标元素
                left = mid + 1
            else:
                right = mid
        # 最后剩下的数一定是所求，无需后处理
        return left

        
        

rooms = [[1],[2],[3],[]]
rooms = [[1,3],[3,0,1],[2],[0]]
ss = Solution()
re = ss.updateMatrix(rooms)
print(re)

