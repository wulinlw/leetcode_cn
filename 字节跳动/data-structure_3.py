#!/usr/bin/python
#coding:utf-8

# https://leetcode-cn.com/explore/interview/card/bytedance/245/data-structure/1033/
# 全 O(1) 的数据结构
# 实现一个数据结构支持以下操作：

# Inc(key) - 插入一个新的值为 1 的 key。或者使一个存在的 key 增加一，保证 key 不为空字符串。
# Dec(key) - 如果这个 key 的值是 1，那么把他从数据结构中移除掉。否者使一个存在的 key 值减一。如果这个 key 不存在，这个函数不做任何事情。key 保证不为空字符串。
# GetMaxKey() - 返回 key 中值最大的任意一个。如果没有元素存在，返回一个空字符串""。
# GetMinKey() - 返回 key 中值最小的任意一个。如果没有元素存在，返回一个空字符串""。
# 挑战：以 O(1) 的时间复杂度实现所有操作。


class AllOne(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_val={}
        self.val_key={} 
        self.maxV=1
        self.minV=1

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key in self.key_val:
            nowV=self.key_val[key]
            if len(self.val_key[nowV])==1:
                del self.val_key[nowV] 
            else:
                del self.val_key[nowV][key]
            self.key_val[key] +=1
            if nowV+1 in self.val_key:
                self.val_key[nowV+1][key]=nowV+1
            else:
                self.val_key[nowV+1]={key:nowV+1}
            self.maxV=max(self.maxV,self.key_val[key])
            if self.minV==nowV:
                if not nowV in self.val_key:
                    self.minV+=1
        else:
            self.key_val[key] =1
            if 1 in self.val_key:
                self.val_key[1][key]=1
            else:
                self.val_key[1]={key:1}
            self.minV=1
                    
    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.key_val:
            if self.key_val[key] ==1:
                del self.key_val[key]
                if len(self.val_key[1])==1:
                    del self.val_key[1]
                    self.minV=self.maxV
                    for key in self.val_key.keys():
                        self.minV=min(self.minV,key)
                else:
                    del self.val_key[1][key]
            else:
                nowV=self.key_val[key]
                if len(self.val_key[nowV])==1:
                    del self.val_key[nowV] 
                else:
                    del self.val_key[nowV][key]
                self.key_val[key]-=1
                if nowV-1 in self.val_key:
                    self.val_key[nowV-1][key]=nowV-1
                else:
                    self.val_key[nowV-1]={key:nowV-1} 
                if not self.maxV in self.val_key:
                    self.maxV-=1 
                if self.minV==nowV:
                    self.minV-=1
            
    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if len(self.key_val)==0: return ''
        item=self.val_key[self.maxV].popitem()
        if len(self.val_key[self.maxV])==0:
            self.val_key[self.maxV]={item[0]:item[1]}
        else:
            self.val_key[self.maxV][item[0]]=item[1]
        return item[0]
    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if len(self.key_val)==0: return ''
        item=self.val_key[self.minV].popitem()
        if len(self.val_key[self.minV])==0:
            self.val_key[self.minV]={item[0]:item[1]}
        else:
            self.val_key[self.minV][item[0]]=item[1]
        return item[0]

        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()



