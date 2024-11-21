lst=[10,9,10,10,10,9,11,2,3]
#创建初始表格
num=[]

for x in range(len(lst)):
    row=1
    num.append(row)
#依次存储至某点的最大递增个数,并记录
for i in range(1,len(lst)):
    tem = []
    for j in range(i):

        if lst[i]>lst[j]:
            tem.append(num[j])
    print(tem)
    if tem!=[]:
        num[i]=max(tem)+1
print(num)

#下面开始找递增数列
addinglst=[]
#先找到最大数的位置，再向前找比他小且最靠近的数
loc=num.index(max(num))
addinglst.insert(0,lst[loc])
currentmax=lst[loc]
currentnum=num[loc]
while True:
    if num[loc] == 1 and lst[loc]<currentmax:
        addinglst.insert(0, lst[loc])
        break
    if num[loc]==currentnum-1 and lst[loc]<currentmax:
        addinglst.insert(0, lst[loc])
        currentmax=lst[loc]
        loc-=1
        currentnum -= 1
    else:
        loc-=1
print(addinglst)