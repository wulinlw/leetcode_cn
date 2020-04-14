#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
#
# https://leetcode-cn.com/problems/russian-doll-envelopes/description/
#
# algorithms
# Hard (33.84%)
# Likes:    125
# Dislikes: 0
# Total Accepted:    8.8K
# Total Submissions: 25.5K
# Testcase Example:  '[[5,4],[6,4],[6,7],[2,3]]'
#
# 给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h)
# 出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
# 
# 请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
# 
# 说明:
# 不允许旋转信封。
# 
# 示例:
# 
# 输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# 输出: 3 
# 解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
# 
# 
#
from typing import List
import bisect
# @lc code=start
class Solution:
    #二分
    # [300] 最长上升子序列 与这题一样
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:return 0
        envelopes.sort(key = lambda x:(x[0], -x[1]))    #w升序，w一样的h降序
        h = [i[1] for i in envelopes]
        dp = [h[0]]                                     #这里用的bisect，与leetcode300题一样
        for i in range(1, len(h)):
            idx = bisect.bisect_left(dp, h[i])
            if idx >= len(dp):
                dp.append(h[i])
            else:
                dp[idx] = h[i]
        return len(dp)


        
# @lc code=end
envelopes = [[5,4],[6,4],[6,7],[2,3]]
o = Solution()
print(o.maxEnvelopes(envelopes))