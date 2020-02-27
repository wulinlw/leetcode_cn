#!/usr/bin/python
#coding:utf-8

def bobble(n):
    for i in range(len(n)):
        for j in range(len(n)):
            if n[j]>n[i]:
                n[i],n[j] = n[j],n[i]
    return n

def merge(a):
    n = len(a)
    if n==1:return a
    mid = n//2 
    return _merge(merge(a[:mid]), merge(a[mid:]))
 
def _merge(l,r):
    re = []
    while l and r:
        if l[0]<r[0]:
            re.append(l.pop(0))
        else:
            re.append(r.pop(0))
    while l:
        re.append(l.pop(0))
    while r:
        re.append(r.pop(0))
    return re



def quick(a,s,end):
    if s<end:
        p = positive(a,s,end)
        quick(a,s,p-1)
        quick(a,p+1,end)
    return a


def positive(a,l,r):
    i=l-1 
    pivot = a[r]
    for j in range(l,r):
        if a[j]<pivot:
            i +=1
            a[i],a[j] = a[j],a[i]
    a[i+1],a[r] = a[r],a[i+1]
    return i+1

def insert(a):
    for i in range(len(a)):
        pre = i-1 
        cur = a[i]
        while pre>=0 and a[pre]>cur:
            a[pre+1] = a[pre]
            pre-=1
        a[pre+1] = cur
    return a


def bucket(a):
    m = max(a)
    bucket = [0]*(m+1)
    for i in a:
        bucket[i] +=1
    re = []
    for i in range(len(bucket)):
        if bucket[i] != 0:
            re.append(i)
    return re

def count(a):
    n = len(a)
    re = [0]*n
    for i in range(n):
        c=0 
        for j in range(n):
            if a[i]>a[j]:
                c+=1
        re[c] = a[i]
    return re

def select(a):
    for i in range(len(a)):
        c= i 
        for j in range(i+1, len(a)):
            if a[c]>a[j]:
                c=j
        a[c],a[i] = a[i],a[c]
    return a 

def shell2(a):
    n = len(a)
    gap = n//2 
    while gap>0:
        for i in range(n):
            j=i 
            cur = a[i]
            while j-gap>=0 and a[j-gap]>cur:
                a[j] = a[j-gap]
                j-=gap
            a[j] = cur 
        gap //=2
    return a

    
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
# re = bobble(arr)
# re = bucket(arr)
# re = count(arr)
# re = insert(arr)
# re = merge(arr)
# re = quick(arr, 0, n-1)
# re = select(arr)
# re = shell2(arr)
# print(re)


