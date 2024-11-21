import random
randomlist = []
for x in range(10000):
    x = random.randint(-10000, 10000)
    randomlist.append(x)

def exchange(list,i,j):
    list[i],list[j]=list[j],list[i]
def siftdown(list,i,upper):  #i is node, upper is the length of list
    while True:
        l,r=i*2+1,i*2+2
        if max(l,r)<upper:  #the node have two children
            if list[i] >= max(list[l],list[r]):
                break
            elif list[l]>list[r]:
                exchange(list,i,l)
                i=l
            else:
                exchange(list,i,r)
                i=r
        elif l<upper:  #the node have only one child (must on the left)
            if list[l]>list[i]:
                exchange(list,i,l)
                i=l
            else:
                break
        else:  #the node have no children
            break
def heapsort(list):
    for j in range((len(list)-2)//2,-1,-1):
        siftdown(list,j,len(list))
    for end in range(len(list)-1,0,-1):  #after every circles one number is sorted, so the length minus 1
        exchange(list,0,end)
        siftdown(list,0,end)
    return list
list=heapsort(randomlist)
print(list)