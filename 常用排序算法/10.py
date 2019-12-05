#!/usr/bin/python
#coding:utf-8

# 
#堆排序
import math, random
def print_tree(array): #打印堆排序使用

    index = 0
    depth = math.ceil(math.log2(len(array)))
    sep = '  '
    for i in range(depth):
        offset = 2 ** i
        print(sep * (2 ** (depth - i - 1) - 1), end='')
        line = array[index:index + offset]
        for j, x in enumerate(line):
            print("{:>{}}".format(x, len(sep)), end='')
            interval = 0 if i == 0 else 2 ** (depth - i) - 1
            if j < len(line) - 1:
                print(sep * interval, end='')
        index += offset
        print()

def sift(data, low, high):
    i = low
    j = 2 * i + 1
    tmp = data[i]
    while j <= high:
        if j < high and data[j] > data[j + 1]:
            j += 1
        if tmp > data[j]:
            data[i] = data[j]
            i = j
            j = 2 * i + 1
        else:
            break
    data[i] = tmp

def sift_2(data,low,high):
    i = low
    j = 2 * i + 1
    tmp = data[i]
    while j <= high:
        if j < high and data[j] > data[j + 1]:
            j += 1
        if tmp > data[j]:
            data[j],data[i] = data[i],data[j]
            i = j
            j = 2 * i + 1
        else:
            break

def heap_sort(data):
    n = len(data)
    for i in range(n//2-1, -1, -1):
        sift_2(data, i, n-1)
    return data

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

if __name__ == '__main__':
    a = [4, 8, 7, 3, 9,22,10,14]
    print(RadixSort2(a))
