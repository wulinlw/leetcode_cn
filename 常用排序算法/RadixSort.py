#!/usr/bin/python
#coding:utf-8

#基数排序
def RadixSort(a):
    i = 0
    n = 1
    max_num = max(a)
    while max_num > 10 ** n:
        n += 1
    while i < n:
        bucket = {}
        for x in range(10):
            bucket.setdefault(x, [])
        for x in a:
            radix =int((x / (10**i)) % 10)
            bucket[radix].append(x)
        j = 0
        for k in range(10):
            if len(bucket[k]) != 0:
                for y in bucket[k]:
                    a[j] = y
                    j += 1
        i += 1
    return a
#基数排序2
def RadixSort2(arr):
    max_num = max(a)
    n = len(str(max_num))

    for i in range(0,n):
        bucket = {}
        for x in range(10):
            bucket.setdefault(x,[])
        for y in a:
            radix = int(y/(10 ** i)%10)
            bucket[radix].append(y)
        j = 0
        for k in range(10):
            if len(bucket[k]) != 0:
                for y in bucket[k]:
                    a[j] = y
                    j += 1
    return arr

arr = [1,2,5,3,4]
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
re = RadixSort2(arr)
print(re)