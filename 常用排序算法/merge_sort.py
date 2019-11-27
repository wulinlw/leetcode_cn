# -*- coding:utf-8 -*-

import math

#归并排序：
def mergeSort(arr):
    if(len(arr)<2): #退出的边界条件
        return arr
    middle = math.floor(len(arr)/2)
    left, right = arr[0:middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left,right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


if __name__=='__main__':

	testlist=[1,4,6,2,3,5,7,9,2,4]
	re = mergeSort(testlist)
	print(re)
	




