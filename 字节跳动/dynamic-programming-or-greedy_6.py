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

 

        
envelopes = [[5,4],[6,1],[6,7],[2,3]]
envelopes = [[1,2],[2,3],[3,4],[3,5],[4,5],[5,5],[5,6],[6,7],[7,8]]
s = Solution()
res = s.maxEnvelopes(envelopes)
print(res)
