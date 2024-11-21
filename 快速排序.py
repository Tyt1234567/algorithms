import random
randomlist = []
for x in range(1000):
    x = random.randint(-1000, 1000)
    randomlist.append(x)

def quicksort(list,start,end): #start,end从1开始数
    if end-start>0:
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

        quicksort(list, start, i)
        quicksort(list, i + 2, end)
    return list

list1=quicksort(randomlist,1,1000)
print(list1)




