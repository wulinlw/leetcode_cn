#!/usr/bin/python
#coding:utf-8

#直接选择排序
# 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
# 然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
# 以此类推，直到所有元素均排序完毕。
def selectsort(arr):
	for i in range(len(arr)):
		min_idx = i
		for j in range(i+1, len(arr)):
			if arr[min_idx] > arr[j]:
				min_idx = j#更新为小的坐标
               
		arr[i], arr[min_idx] = arr[min_idx], arr[i]
		# print(min_idx,arr)
	return arr

arr = [1,2,5,3,4]
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
re = selectsort(arr)
print(re)