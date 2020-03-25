#!/usr/bin/python
#coding:utf-8

# 面试题 17.06. 2出现的次数
# 编写一个方法，计算从 0 到 n (含 n) 中数字 2 出现的次数。

# 示例:

# 输入: 25
# 输出: 9
# 解释: (2, 12, 20, 21, 22, 23, 24, 25)(注意 22 应该算作两次)
# 提示：

# n <= 10^9
# https://leetcode-cn.com/problems/number-of-2s-in-range-lcci/

class Solution:
    # 根据每一位b来计算当前位为2时候的个数(只考虑当前位的2)
    # 对于xby来说, 需要判断b与2的大小, 左边部分的个数是int(x), 如果b>2的话需要+1(即0~x之间的所有数都满足), 右边部分为10**len(y), 左边部分*右边部分的个数即为所求
    # 注意需要特殊处理b==2的情况, 需要加上左边部分恰好为x时右边的个数, 即为int(y)+1
    def numberOf2sInRange(self, n: int) -> int:
        res = 0
        s = str(n)
        for i in range(len(s))[::-1]:
            c = s[i]
            left = 0 if i == 0 else int(s[0:i])
            if c > '2':
                left += 1
            res += left * (10**(len(s) - i - 1))
            if c == '2':
                right = int(s[i + 1:]) + 1 if i + 1 < len(s) else 1
                res += right
        return res
    
    
    # 剑指offer 面试题43：从1到n整数中1出现的次数  类似，区别是current < 2和==2
    # 从1到n，我们将其分段，也就是，一位数，两位数，三位数。然后分别计算这些段中含k的次数
    # 假设abcdef
    # 当我们在计算，百位d的时候，也就是三位数的时候。
    # 当d<2：百位重复多少次，那么百位2就出现多少次，二百位重复的次数，恰恰时abc000次。
    # 当d=2：同上adc000次，但是此时，从百位还自带abck00-abcdef中的，xx次和k00这个数
    # 所以，这种情况2出现的次数位abc000+ef+1
    # 当d>2：同上abc000次，此时，还自带abck000-abc(2+1)000中的2
    # 所以出现2的情况位abc000+1000。
    def numberOf2sInRange2(self, n: int) -> int:
        res = 0
        i = 1  # 个位开始
        while n // i != 0:
            high = n//(i*10) # 高位数
            current = (n//i) % 10  # 第i位数
            low = n - (n//i) * i  # 低位数
            if current < 2:
                res += high * i
            elif current == 2:
                res += high * i + low + 1
            else:
                res += (high+1) * i
            i *= 10
        return res



o = Solution()
print(o.numberOf2sInRange(1125))
print(o.numberOf2sInRange2(1125))






