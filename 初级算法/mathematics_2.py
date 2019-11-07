#!/usr/bin/python
#coding:utf-8
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/25/math/61/
# 计数质数
# 统计所有小于非负整数 n 的质数的数量。

# 示例:

# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。


# 厄拉多塞筛法
# 西元前250年，希腊数学家厄拉多塞(Eeatosthese)想到了一个非常美妙的质数筛法，
# 减少了逐一检查每个数的的步骤，可以比较简单的从一大堆数字之中，筛选出质数来，这方法被称作厄拉多塞筛法(Sieve of Eeatosthese)。

# 具体操作：
# 先将 2~n 的各个数放入表中，然后在2的上面画一个圆圈，然后划去2的其他倍数；
# 第一个既未画圈又没有被划去的数是3，将它画圈，再划去3的其他倍数；
# 现在既未画圈又没有被划去的第一个数 是5，将它画圈，并划去5的其他倍数……
# 依次类推，一直到所有小于或等于 n 的各数都画了圈或划去为止。
# 这时，表中画了圈的以及未划去的那些数正好就是小于 n 的素数。

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        prime = [1] * n
        prime[0] = prime[1] = 0
        for i in range(2, int(n**0.5) +1):#根号N后面的都会被划掉
            if prime[i] == 1:#没有划去的值为1
                # print(i,prime[i*i:n:i])
                prime[i*i:n:i] = [0]*len(prime[i*i:n:i])#划去I的倍数，值设为0
                # print(i,prime[i*i:n:i])
        return sum(prime)#最后留下的都是质数，值为1



n=12
s = Solution()
re = s.countPrimes(n)
print("deep:",re)