import random
list=[]
for x in range(10):
    x=random.randint(-100,100)
    list.append(x)
list=sorted(list)
print(list)
def mindis(first,last,list,n,min=200):   #从1开始数
    if n==2:
        return list[last-1]-list[first-1]
    else:
        leftmin=mindis(first,(first+last-1)//2+1,list,n//2+1,min)
        rightmin=mindis((first+last-1)//2+1,last,list,n-n//2,min)
        if leftmin<rightmin:
            min=leftmin
        else:
            min=rightmin
    return min
a=mindis(1,10,list,10)
print(a)
