#!/usr/bin/python
#coding:utf-8

# 机器人的运动范围
# 地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。
# 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
# 但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

class Solution:
    #dfs
    def movingCount2(self, m: int, n: int, k: int) -> int:
        self.cache = {}
        def moving(x, y):
            curCnt = 0
            if x<0 or x>=m or y<0 or y>=n or not check(x, y, k) or (x, y) in self.cache:
                return curCnt
            self.cache[(x, y)] = 1
            curCnt +=  1 + moving(x+1, y)+\
                    moving(x, y+1)
            return curCnt
        
        def check(x, y, k):
            n = int(str(x)+str(y))
            ans = 0
            while n:
                ans += n % 10
                n //= 10
            return True if ans<=k else False

        return moving(0, 0)

    #bfs
    def movingCount(self, m: int, n: int, k: int) -> int:
        from queue import Queue
        q = Queue()
        q.put((0, 0))

        def digitsum(n):
            ans = 0
            while n:
                ans += n % 10
                n //= 10
            return ans

        s = set()
        while not q.empty():
            x, y = q.get()
            if (x, y) not in s and 0 <= x < m and 0 <= y < n and digitsum(x) + digitsum(y) <= k:
                s.add((x, y))
                for nx, ny in [(x + 1, y), (x, y + 1)]:
                    q.put((nx, ny))
        return len(s)



obj = Solution()
print(obj.movingCount(5, 10, 10))
# print(obj.isok(18, 35, 38))
