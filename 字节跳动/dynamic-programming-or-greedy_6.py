#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/bytedance/246/dynamic-programming-or-greedy/1031/
# 俄罗斯套娃信封问题
# 给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
# 请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

# 说明:
# 不允许旋转信封。

# 示例:
# 输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# 输出: 3 
# 解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。

from typing import List
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        from bisect import bisect_left
        if not envelopes:
            return 0
        
        #左高度相同的信封右高度大的排在前面
        envelopes.sort(key=lambda a:(a[0], -a[1]))#第二个参数前面的-，表示第二个参数倒序排列
        mem = list()
        for e in envelopes:
            index = bisect_left(mem, e[1])#把h插入mem,返回插入的index
            if len(mem) == index:#如果插入到了最后，说明可以套娃
                mem.append(e[1])
            else:#插入到中间，说明有重复
                mem[index] = e[1]#主要是不存在的时候，需要写入
        return len(mem)

    

    # https://leetcode-cn.com/problems/russian-doll-envelopes/solution/tan-xin-suan-fa-er-fen-cha-zhao-python-dai-ma-java/
    # 该算法超时，不采用
    def maxEnvelopes2(self, envelopes: List[List[int]]) -> int:
        size = len(envelopes)
        # 特判
        if size < 2:
            return size

        # 对第一列排序，按照宽度排序（按照高度排序亦可，只不过后面定义状态的时候就得定义宽度）
        envelopes.sort(key=lambda x: x[0])
        # print(envelopes)
        # 以 envelopes[i][1] 结尾的上升子序列的长度
        dp = [1 for _ in range(size)]
        for i in range(1, size):
            for j in range(i):
                # 注意宽度也要严格小于
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    # https://leetcode-cn.com/problems/russian-doll-envelopes/solution/tan-xin-suan-fa-er-fen-cha-zhao-python-dai-ma-java/
    def maxEnvelopes3(self, envelopes: List[List[int]]) -> int:
        size = len(envelopes)
        # 特判
        if size < 2:
            return size

        # 对第一列排序，按照宽度排序
        # 【特别注意】当宽度相等的时候，按照高度降序排序
        # 以避免 [[11, 3], [12, 4], [12, 5], [12, 6], [14, 6]] 这种情况发生
        # 正确排序 [[11, 3], [12, 6], [12, 5], [12, 4], [14, 6]]
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # print(envelopes)
        tail = [envelopes[0][1]]

        for i in range(1, size):
            target = envelopes[i][1]
            if target > tail[-1]:
                tail.append(target)
                continue

            left = 0
            right = len(tail) - 1

            while left < right:
                mid = (left + right) >> 1
                if tail[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            tail[left] = target
        # print(tail)
        return len(tail)


 

        
envelopes = [[5,4],[6,1],[6,7],[2,3]]
envelopes = [[1,2],[2,3],[3,4],[3,5],[4,5],[5,5],[5,6],[6,7],[7,8]]
envelopes = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
s = Solution()
res = s.maxEnvelopes0(envelopes)
print(res)
