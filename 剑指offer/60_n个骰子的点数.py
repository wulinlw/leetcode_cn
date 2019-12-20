#!/usr/bin/python
#coding:utf-8

# 剑指Offer 60.
# n个骰子的点数（Python）
# 把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值的概率。
# https://blog.csdn.net/qq_39315740/article/details/98036906

# 动态规划
# 可以用两个数组来存储每个总数出现的次数。
# 在一轮循环中，第一个数组中的第n个数字表示骰子和出现的次数。
# 在下一轮循环中，加上一个新的骰子，此时和为n出现的次数为上一轮出现的和为n-1,n-2,n-3,n-4,n-5,n-6之和，
# 即前面提到的f(n)=f(n−1)+f(n−2)f(n−3)+f(n−4)+f(n−5)+f(n−6)


# 关于以下这行，这里可能不太好理解：

# for k in range(1, min(j+1, 7)):
# 	res[i][j] += res[i-1][j-k]

# 我们可以举个具体的例子来解释：
# 例如n = 3 , s = 7, 这时满足s > 6.
# 那么在n=2时，加上一个骰子，s=7会有多少种情况呢？
# 答案是6种，s=1+6，s=2+5，s=3+4，s=4+3，s=5+2，s=6+1，
# 也就是f(n) = f(n-1) +f(n-2) f(n-3)+ f(n-4) +f(n-5)+ f(n-6)
# 但假设n=3，s = 3，这时s <= 6.
# 这时显然就没有6种情况，只有2种情况，即s=1+2，s=2+1
# 这就是为什么我们要用min(j+1,7)来区分以上两种条件。

# res[i][j] += res[i-1][j-k]
# j-k
# j是n到6*n的数，
# k是当前掷的数1-6
# f(n) = j-1 + j-2 + j-3 + j-4 + j-5 + j-6

class Solution(object):
    def numberOfDice(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # 为了将index与n对应上，特意把第0行空出来
        res = [[0 for i in range(6*n+1)] for i in range(n+1)]
        
        # 将第0行与第0列空出来，res[1][1:7] = [1,1,1,1,1,1]
        # 表示第一个骰子6种情况各出现一次
        for i in range(1,7):
            res[1][i] = 1
        print(res)
        
        # 从第二个骰子开始遍历，2颗，3颗，4颗，n颗
        for i in range(2,n+1):
        	# n个骰子之和的范围为n到6*n， 2颗色子时，和的范围是2-12
            for j in range(i, 6*i+1):
            	# 当 j > 6 时，f(n) = f(n-1) +f(n-2) f(n-3)+ f(n-4) +f(n-5)+ f(n-6)
            	# 当 j <= 6 时，例如3，f(n) = f(n-1) +f(n-2)
                for k in range(1, min(j,6)+1):#当前掷的数
                    res[i][j] += res[i-1][j-k]#i-1上一颗色子的值，j-k是和减去当前 （j是n到6*n的数，k是当前掷的数1-6）
        print(res)
        return res[-1][n:]


n=3
S = Solution()
deep = S.numberOfDice(n)
print("deep:",deep)
