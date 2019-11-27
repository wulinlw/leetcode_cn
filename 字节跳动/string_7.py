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
        # 回溯算法
        result = list()
        if not s and  4 > len(s) > 12 :
            return result

        self._restoreIpAddresses(s, 4, 0, "", result)
        return result

    def _restoreIpAddresses(self, s, n, index, ip, result):
        if n == 0:#边界条件，剩余数=0
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

    # 回溯算法
    def restoreIpAddresses2(self, s):
        res = []
        n = len(s)


        # flag 还剩余几段ip
        def backtrack(i, tmp, flag):
            if i == n and flag == 0:
                res.append(tmp[:-1])
                return
            if flag < 0:
                return
            for j in range(i, i + 3):
                if j < n:
                    # print(i == j and s[j] == "0",0 < int(s[i:j + 1]) <= 255,tmp)
                    if i == j and s[j] == "0":
                        backtrack(j + 1, tmp + s[j] + ".", flag - 1)
                        break
                    if 0 < int(s[i:j + 1]) <= 255:
                        backtrack(j + 1, tmp + s[i:j + 1] + ".", flag - 1)

        backtrack(0, "", 4)
        return res


string = "25525511135"
s = Solution()
n = s.restoreIpAddresses2(string)
print(n)