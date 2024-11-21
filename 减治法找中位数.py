import random
k=10
list1=[]
list2=[]
for a in range(21):
    a=random.randint(-100,100)
    list1.append(a)
list1=sorted(list1)

for b in range(13):
    b=random.randint(-100,100)
    list2.append(b)
list2=sorted(list2)
print(list1)
print(list2)

list=[]
for i in list1:
    list.append(i)
for j in list2:
    list.append(j)
list=sorted(list)
print(list)

def findmedium(list1,list2):
    s1=0
    e1=len(list)-1
    s2=0
    e2=len(list2)-1
    while s1<e1 and s2<e2:
        mid1=(s1+e1)//2
        mid2=(s2+e2)//2
        if list1[mid1]==list2[mid2]:
            return list1[mid1]
        if list1[mid1]<list2[mid2]:
            if (s1+e1)%2==0:  #总数奇数
                s1=mid1
            else: #总数为偶数
                s1=mid1+1
            e2=mid2
        else:
            if (s1+e1)%2==0:
                s2=mid2
            else:
                s2=mid2+1
            e1=mid1
        print(s1)
        print(e1)
        print(list1[s1:e1+1])
        print(s2)
        print(e2)
        print(list2[s2:e2+1])
        print("\n")
    if list1[s1]<list2[s2]:
        return list1[s1]
    else:
        return list2[s2]
medium=findmedium(list1,list2)
print(medium)




