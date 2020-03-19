#
# @lc app=leetcode.cn id=1079 lang=python3
#
# [1079] 活字印刷
#
# https://leetcode-cn.com/problems/letter-tile-possibilities/description/
#
# algorithms
# Medium (72.33%)
# Likes:    41
# Dislikes: 0
# Total Accepted:    3.4K
# Total Submissions: 4.6K
# Testcase Example:  '"AAB"'
#
# 你有一套活字字模 tiles，其中每个字模上都刻有一个字母 tiles[i]。返回你可以印出的非空字母序列的数目。
# 
# 
# 
# 示例 1：
# 
# 输入："AAB"
# 输出：8
# 解释：可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。
# 
# 
# 示例 2：
# 
# 输入："AAABBC"
# 输出：188
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= tiles.length <= 7
# tiles 由大写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def numTilePossibilities2(self, tiles: str) -> int:
        def backtrack(counter):
            res = 0
            for i in range(26):         #每个字符遍历
                if counter[i]==0:       #不存在的跳过
                    continue
                res += 1                #存在的结果+1
                counter[i] -= 1
                res += backtrack(counter)
                counter[i] += 1
            return res

        #字母频次统计
        counter = [0]*26 
        for i in tiles:
            counter[ord(i)-ord('A')] += 1
        return backtrack(counter)
    
    def numTilePossibilities(self, tiles: str) -> int:
        ans = set()
        def backtrack(arr, tmp):
            if len(tmp)>0:
                ans.add(tmp[:])
            for i in range(len(arr)):
                backtrack(arr[:i]+arr[i+1:], arr[i]+tmp)
        backtrack(tiles, "")
        # print(ans)
        return len(ans)
# @lc code=end

tiles = "AAB"
# tiles = "AAABBC"
o = Solution()
print(o.numTilePossibilities(tiles))
# print(o.numTilePossibilities2(tiles))