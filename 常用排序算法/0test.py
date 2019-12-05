#!/usr/bin/python
#coding:utf-8

def shell(a):
    n = len(a)
    gap = n//2
    while gap>0:
        for i in range(len(a)):
            j = i
            cur = a[i]
            while j-gap >=0 and a[j-gap]>cur:
                a[j] = a[j-gap]
                j = j-gap
            a[j] = cur
        gap = gap//2
    return a

if __name__ == '__main__':
    a = [4, 8, 7, 3, 9,22,10,14]
    # print(quick(a,0,len(a)-1))
    print(shell(a))