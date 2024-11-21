p=[0.1,0.2,0.4,0.3]
lst=[]

for x in range(5):
    row=[]
    for y in range(5):
        row.append('none')
    lst.append(row)

for i in range(5):
    lst[i][i]=0


len=4
j=1
while len>=1:
    for i in range(len):
        tem = []
        for x in range(1, j+1):
            tem.append(lst[i][i+j-x]+lst[i+j-x+1][i+j]+sum(p[i:i+j]))

        lst[i][i + j] = min(tem)
    len-=1
    j+=1



for r in lst:
    print(r)

