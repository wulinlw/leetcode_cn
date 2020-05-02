# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题16.08.整数的英语表示
# 
# https://leetcode-cn.com/problems/english-int-lcci/
# 
# 给定一个整数，打印该整数的英文描述。
# 示例 1:
# 
# 输入: 123
# 输出: "One Hundred Twenty Three"
# 
# 
# 示例 2:
# 
# 输入: 12345
# 输出: "Twelve Thousand Three Hundred Forty Five"
# 
# 示例 3:
# 
# 输入: 1234567
# 输出: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# 
# 示例 4:
# 
# 输入: 1234567891
# 输出: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
# 
# 
# Hard 37.8%
# Testcase Example: 123
# 
# 提示:
# 试着从三位作为一段的角度思考。
# 你考虑过负数吗？你的解决方案是否适用于100 030 000这样的值？
# 考虑把一个数字分成由3位数组成的序列。
# 
# 

class Solution:
    #3位一段，迭代分治处理
    ns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,30, 40, 50, 60, 70, 80, 90, 100, 1000, 1000000, 1000000000]
    ss = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine","Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen","Seventeen", "Eighteen", "Nineteen","Twenty", "Thirty", "Forty", "Fifty","Sixty","Seventy", "Eighty", "Ninety","Hundred", "Thousand", "Million", "Billion"]
    k = 90
    def numberToWords(self, num: int) -> str:
        if num == 0: return 'Zero'
        i = len(self.ns) - 1
        while i>0 and self.ns[i] > num:
            i -= 1
        # print(i)
        n, s = self.ns[i], self.ss[i]
        pre, suf = '', ''
        if n > self.k:                                  #大于90，就是这一段有3位，取百位
            pre = self.numberToWords(num//n) + ' '
        if num % n:                                     #取个位
            suf = ' ' + self.numberToWords(num%n)
        return pre + s + suf                            #百位 十位 个位

num = 123
# num = 12345
o = Solution()
print(o.numberToWords(num))