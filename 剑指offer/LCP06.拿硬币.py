# LCP 06. 拿硬币
# 桌上有 n 堆力扣币，每堆的数量保存在数组 coins 中。我们每次可以选择任意一堆，拿走其中的一枚或者两枚，求拿完所有力扣币的最少次数。

# 示例 1：

# 输入：[4,2,1]

# 输出：4

# 解释：第一堆力扣币最少需要拿 2 次，第二堆最少需要拿 1 次，第三堆最少需要拿 1 次，总共 4 次即可拿完。

# 示例 2：

# 输入：[2,3,10]

# 输出：8

# 限制：

# 1 <= n <= 4
# 1 <= coins[i] <= 10

# https://leetcode-cn.com/problems/na-ying-bi/
from typing import List
class Solution:
    def minCount2(self, coins: List[int]) -> int:
        re = 0
        for i in coins:
            a, b = divmod(i, 2)
            re += a
            if 0<b<=2:
                re += 1
        return re

    def minCount(self, coins: List[int]) -> int:
        re = 0
        for i in coins:
            re += (i+1)//2
        return re

# coins = [4,2,1]
coins = [2,3,10]
o = Solution()
print(o.minCount(coins))