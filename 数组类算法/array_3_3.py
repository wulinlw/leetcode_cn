#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/orignial/card/all-about-array/232/two-pointers/967/
# 反转字符串中的元音字母
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

# 示例 1:
# 输入: "hello"
# 输出: "holle"

# 示例 2:
# 输入: "leetcode"
# 输出: "leotcede"
# 说明:
# 元音字母不包含字母"y"。
class Solution(object):
    # 在英文中，5个元音字母分别为：a[ei]、e[i:]、i[ ai]、o[eu]、u[ju:]。
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = s
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        p1, p2 = 0, len(arr) - 1
        while p1 < p2:
            while arr[p1] not in vowel :
                p1 += 1
                continue
            while arr[p2] not in vowel :
                p2 -= 1
                continue
            if p1 < p2:
                arr[p1], arr[p2] = arr[p2], arr[p1]
                p1 += 1
                p2 -= 1
        return ''.join(arr)


s = "hello"
S = Solution()
deep = S.reverseVowels(s)
print("deep:",deep)
