#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/bytedance/242/string/1044/
# 复原IP地址
# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

# 示例:
# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = list()
        if not s and  4 > len(s) > 12 :
            return result

        self._restoreIpAddresses(s, 4, 0, "", result)
        return result

    def _restoreIpAddresses(self, s, n, index, ip, result):
        if n == 0:
            if index == len(s):
                result.append(ip)
            return

        def isNum(num):
            if 0 <= int(num) <= 255 and str(int(num)) == num:
                return True
            return False

        for i in range(index+1, len(s) + 1):
            if isNum(s[index:i]):
                self._restoreIpAddresses(s, n - 1, i, s[index:i] if ip == "" else ip+'.'+s[index:i], result)
            else:
                break


string = "25525511135"
s = Solution()
n = s.restoreIpAddresses(string)
print(n)