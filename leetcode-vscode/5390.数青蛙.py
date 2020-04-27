# 5390. 数青蛙
# 给你一个字符串 croakOfFrogs，它表示不同青蛙发出的蛙鸣声（字符串 "croak" ）的组合。由于同一时间可以有多只青蛙呱呱作响，所以 croakOfFrogs 中会混合多个 “croak” 。请你返回模拟字符串中所有蛙鸣所需不同青蛙的最少数目。
# 注意：要想发出蛙鸣 "croak"，青蛙必须 依序 输出 ‘c’, ’r’, ’o’, ’a’, ’k’ 这 5 个字母。如果没有输出全部五个字母，那么它就不会发出声音。
# 如果字符串 croakOfFrogs 不是由若干有效的 "croak" 字符混合而成，请返回 -1 。

# 示例 1：
# 输入：croakOfFrogs = "croakcroak"
# 输出：1 
# 解释：一只青蛙 “呱呱” 两次

# 示例 2：
# 输入：croakOfFrogs = "crcoakroak"
# 输出：2 
# 解释：最少需要两只青蛙，“呱呱” 声用黑体标注
# 第一只青蛙 "crcoakroak"
# 第二只青蛙 "crcoakroak"

# 示例 3：
# 输入：croakOfFrogs = "croakcrook"
# 输出：-1
# 解释：给出的字符串不是 "croak" 的有效组合。

# 示例 4：
# 输入：croakOfFrogs = "croakcroa"
# 输出：-1
 
# 提示：
# 1 <= croakOfFrogs.length <= 10^5
# 字符串中的字符只有 'c', 'r', 'o', 'a' 或者 'k'

class Solution:
    # 思想就是维护croak的个数，如果遇到当前字母，则肯定是由前面字母过来，前面字母数-1。
    # 如遇到r，则必是c->r，所以c--
    # k代表结尾，其实也是青蛙的起始（一次喊叫结束），所以遇到c的时候，先去消耗k，没有k了，需要新青蛙，答案+1
    # https://leetcode-cn.com/problems/minimum-number-of-frogs-croaking/solution/cai-ji-gong-xian-ge-chun-onzuo-fa-by-imcover/
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c, r, o, a, k = 0, 0, 0, 0, 0
        re = 0
        for i in range(len(croakOfFrogs)):
            if croakOfFrogs[i] == 'c':
                if k>0:
                    k -= 1
                else:
                    re += 1
                c += 1
            elif croakOfFrogs[i] == 'r':
                c -= 1
                r += 1
            elif croakOfFrogs[i] == 'o':
                r -= 1
                o += 1
            elif croakOfFrogs[i] == 'a':
                o -= 1
                a += 1
            elif croakOfFrogs[i] == 'k':
                a -= 1
                k += 1
            if c<0 or r<0 or o<0 or a<0:
                break
        if c!=0 or r!=0 or o!=0 or a!=0:
            return -1
        return re



croakOfFrogs = "croakcroak"
o = Solution()
print(o.minNumberOfFrogs(croakOfFrogs))   