#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/tencent/227/hui-su-suan-fa/946/
# 格雷编码
# 格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。
# 给定一个代表编码总位数的非负整数 n，打印其格雷编码序列。格雷编码序列必须以 0 开头。

# 示例 1:
# 输入: 2
# 输出: [0,1,3,2]
# 解释:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2

# 对于给定的 n，其格雷编码序列并不唯一。
# 例如，[0,2,3,1] 也是一个有效的格雷编码序列。

# 00 - 0
# 10 - 2
# 11 - 3
# 01 - 1
# 示例 2:
# 输入: 0
# 输出: [0]
# 解释: 我们定义格雷编码序列必须以 0 开头。
#      给定编码总位数为 n 的格雷编码序列，其长度为 2n。当 n = 0 时，长度为 20 = 1。
#      因此，当 n = 0 时，其格雷编码序列为 [0]。



class Solution(object):
    # https://leetcode-cn.com/problems/gray-code/solution/gray-code-jing-xiang-fan-she-fa-by-jyd/
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res, head = [0], 1
        for _ in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(head + res[j])
            head <<= 1
        return res

    # https://leetcode-cn.com/problems/gray-code/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by--12/
    def grayCode2(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # 二进制转成格雷码有一个公式。
        # 所以我们遍历 0 到 2^n−1，然后利用公式转换即可。
        # 即最高位保留，其它位是当前位和它的高一位进行异或操作。
        # return [i ^ i >> 1  for i in range(2 ** n)]
        r = []
        for i in range(2 ** n):#2 ** n没有-1也就是最后保留了最高位
            r.append( i ^ i >> 1 )
            # print("{:0>32b}".format(i ^ i >> 1), i ^ i >> 1)
        return r
    
    # https://leetcode-cn.com/problems/gray-code/solution/jian-dan-de-si-lu-44ms-by-dannnn/
    def grayCode3(self, n):
        if n==0:
            return [0]
        res=[]
        def back(now,x):
            if len(now)==n:
                # print(now)
                res.append(int(now,2))
            elif x==0:
                back(now+'0',0)
                back(now+'1',1)
            else:
                back(now+'1',0)
                back(now+'0',1)
        
        back('',0)
        return res





n = 2
s = Solution()
r = s.grayCode3(n)
print(r)




