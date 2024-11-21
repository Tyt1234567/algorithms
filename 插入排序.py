list=[1,2,3,4,5,6,5,8,7,6,5,4,3,2,1]

for i in range(1,len(list)):

    while i>0:
        if list[i]<list[i-1]:#往前面排序好的数组中插
            list[i-1],list[i]=list[i],list[i-1]
            i-=1

        else:
            break
print(list)