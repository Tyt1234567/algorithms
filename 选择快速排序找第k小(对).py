import random
k=int(input(""))
list=[]
for a in range(1000):
    a=random.randint(-1000,1000)
    list.append(a)
print(list)
print(f"正确答案：{sorted(list)[k-1]}")


def findk(list,start,end,m): #start,end从1开始数

    i = start - 1
    j = end - 1

    while i < j:
        while i < j and list[i] < list[j]:
            j -= 1
        if i < j:
            list[i], list[j] = list[j], list[i]
            i += 1

        while i < j and list[i] < list[j]:
            i += 1
        if i < j:
            list[i], list[j] = list[j], list[i]
            j -= 1
    loc=i+1
    if loc==m :
        r=list[m-1]
        return r
    if loc<m: #在后面找
        return findk(list,loc+1,end,m)
    if loc>m: #在前面找
        return findk(list,start,loc-1,m)
a=findk(list,1,1000,k)
print(a)

a=findk(list,1,1000,k)
print(a)
print(f"正确答案：{sorted(list)[k-1]}")
