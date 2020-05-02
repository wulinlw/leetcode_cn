# #!/usr/bin/python
# #coding:utf-8
# 
# 面试题05.02.二进制数转字符串
# 
# https://leetcode-cn.com/problems/bianry-number-to-string-lcci/
# 
# 二进制数转字符串。给定一个介于0和1之间的实数（如0.72），类型为double，打印它的二进制表达式。如果该数字不在0和1之间，或者无法精确地用32位以内的二进制表示，则打印"ERROR"。
# 示例1:
# 
#  输入：0.625
#  输出："0.101"
# 
# 
# 示例2:
# 
#  输入：0.1
#  输出："ERROR"
#  提示：0.1无法被二进制准确表示
# 
# 
# 提示：
# 
# 
# 	32位包括输出中的"0."这两位。
# 
# 
# 
# Medium 58.3%
# Testcase Example: 0.625
# 
# 提示:
# 为了解决这个问题，试着想想如何用它来处理整数。
# 像0.893这样的数字（以10为底），每个数字代表什么？那么以2为底的0.10 010中的每个数字代表什么？
# 一个数字如0.893（以10为底）表示8×101 + 9×102 + 3×103。将此系统转换为以2为底。
# 你将如何获得0.893中的第一个数字？如果乘以10，那么你会改变值得到8.93。如果乘以2，结果会是什么？
# 想想那些不能用二进制精确表示的值会发生什么。
# 
# 

class Solution:
    # https://leetcode-cn.com/problems/bianry-number-to-string-lcci/solution/c-python-mian-shi-ti-0502-er-jin-zhi-shu-zhuan-zi-/
    def printBin(self, num: float) -> str:
        res, i = "0.", 30       #若 "0." 计为两位，i 初始化为 30，若计为 1 位，初始化为 31
        while num > 0 and i:
            num *= 2
            if num >= 1:        #取num的个位（0或1），将对应的字符加入res的末尾
                res += '1'
                num -= 1        #截取num的小数部分，作为num的新值
            else:
                res += '0'
            i -= 1
        return res if not num else "ERROR"  #当num为0时（即res已经精确地表达了num），返回res

nums = 0.625
o = Solution()
print(o.printBin(nums))