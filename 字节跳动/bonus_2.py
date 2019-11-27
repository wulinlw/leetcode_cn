#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/bytedance/247/bonus/1037/
# UTF-8 编码验证
# UTF-8 中的一个字符可能的长度为 1 到 4 字节，遵循以下的规则：

# 对于 1 字节的字符，字节的第一位设为0，后面7位为这个符号的unicode码。
# 对于 n 字节的字符 (n > 1)，第一个字节的前 n 位都设为1，第 n+1 位设为0，后面字节的前两位一律设为10。剩下的没有提及的二进制位，全部为这个符号的unicode码。
# 这是 UTF-8 编码的工作方式：

#    Char. number range  |        UTF-8 octet sequence
#       (hexadecimal)    |              (binary)
#    --------------------+---------------------------------------------
#    0000 0000-0000 007F | 0xxxxxxx
#    0000 0080-0000 07FF | 110xxxxx 10xxxxxx
#    0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
#    0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
# 给定一个表示数据的整数数组，返回它是否为有效的 utf-8 编码。

# 注意:
# 输入是整数数组。只有每个整数的最低 8 个有效位用来存储数据。这意味着每个整数只表示 1 字节的数据。

# 示例 1:

# data = [197, 130, 1], 表示 8 位的序列: 11000101 10000010 00000001.

# 返回 true 。
# 这是有效的 utf-8 编码，为一个2字节字符，跟着一个1字节字符。
# 示例 2:

# data = [235, 140, 4], 表示 8 位的序列: 11101011 10001100 00000100.

# 返回 false 。
# 前 3 位都是 1 ，第 4 位为 0 表示它是一个3字节字符。
# 下一个字节是开头为 10 的延续字节，这是正确的。
# 但第二个延续字节不以 10 开头，所以是不符合规则的。

class Solution(object):
    # https://blog.csdn.net/gsch_12/article/details/82669505
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        # 0x0     00000000
        # 0x80    10000000
        # 0xE0    11100000
        # 0xF0    11110000
        # 0xF8    11111000
        # 0xC0    11000000
        masks = [0x0, 0x80, 0xE0, 0xF0, 0xF8]
        bits = [0x0, 0x0, 0xC0, 0xE0, 0xF0]
        while data:
            for x in (4, 3, 2, 1, 0):
                if data[0] & masks[x] == bits[x]:
                    break
                print x
            if x == 0 or len(data) < x:
                return False
            for y in range(1, x):
                if data[y] & 0xC0 != 0x80:
                    return False
            data = data[x:]
        return True
    
    # 推荐看这个解法
    def validUtf8_2(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        cnt=0 #除开第一个字节，后面字节有几个是10开头，这个是关键
        for i in range(len(data)):
            if cnt==0:#对比第一个字节的情况，就知道后面有几个是10开头的了
                if (data[i]>>5)==0b110:
                    cnt=1
                elif (data[i]>>4)==0b1110:
                    cnt=2
                elif (data[i]>>3)==0b11110:
                    cnt=3
                elif (data[i]>>7):#以上情况都不是，那就是1字节的字符，且第一位是1，不满足utf-8第一位0的要求
                    return False
            else:
                if(data[i]>>6)!=0b10:#后面几位不是10开头
                    return False
                cnt-=1#如果后面几个字节是10开头，每次-1，最后cnt=0，说明复合utf-8规则
        return cnt==0

    def validUtf8_3(self, data):
        cnt = 0  # 用于记录当前是几字节编码
        for byte in data:
            if 128 <= byte <= 191:  # 表示这数字对应的2进制 为 10xxxxxx 类型的，所以不能作为开头
                if cnt == 0:  # 此时，如果 cnt==0 直接返回 False
                    return False
                cnt -= 1  # 当前 位 合法，进入下一位比较
            else:  # -- -- 判断 当前 二进制 非10 开头的情况 
                if cnt:
                    return False
                if byte < 128:  # 表示一个字节的情况
                    continue
                elif byte < 224:  # 两个字节的情况
                    cnt = 1
                elif byte < 240:  # 三个字节的情况
                    cnt = 2
                elif byte < 248:  # 四个字节的情况
                    cnt = 3
                else:  # 其他情况均为 False
                    return False
        return cnt == 0  # 比较结束， cnt 必须为0 才是合法的


data = [197, 130, 1]
s = Solution()
res = s.validUtf8(data)
print(res)
















