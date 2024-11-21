import time
import random

n = int(input('输入最大值:'))
randomlist = []
for x in range(10000):
    a=[]
    x = random.randint(0, n)
    a.append(x)
    randomlist.append(a)
# 随机生成10000个数(范围为0至n)

def merge(list1,list2):
    list=[]
    i=0
    j=0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            list.append(list1[i])
            i += 1
        else:
            list.append(list2[j])
            j += 1
    if i == len(list1):
        for x in list2:
            if x>list1[-1]:
                list.append(x)
    if j == len(list2):
        for x in list1:
            if x>list2[-1]:
                list.append(x)
    return list

def mergesort(list,start,end):
    if start==end:
        return [list[start - 1]]
    else:
        list1=mergesort(list,start,(start+end)//2)
        list2=mergesort(list,(start+end)//2+1,end)
        sortlist=merge(list1,list2)
    return sortlist
a=mergesort(randomlist,1,10000)
for i in a:
    print(i,end=" ")

