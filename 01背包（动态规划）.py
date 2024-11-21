weight=[2,2,6,5,4]
value=[6,3,5,4,6]
size=10
tab=[]

for x in range(len(weight)+1):
    row=[]
    for y in range(size+1):
        row.append(0)
    tab.append(row)

for x in range(1,len(weight)+1):
   for y in range(1,size+1):
       # 没有资格放入，填入上一格数据
       if y<weight[x-1]:
           tab[x][y]=tab[x-1][y]
       # 有资格放入，在不放入他（上面一格）和放入他（上面一行重量减去该物品重量列+该物品价值）之间比较，填入大的
       else:
           tab[x][y] = max(tab[x - 1][y],tab[x-1][y-weight[x-1]]+value[x-1])

for row in tab:
    print(row)

#下面开始找放入了哪些物品（即倒过来找）
i=len(weight)
j=size
path=[]
while i>0 and j>0:
    if tab[i][j]==tab[i-1][j]:
        i-=1
    else:
        if tab[i][j]==tab[i-1][j-weight[i-1]]+value[i-1]:
            j=j-weight[i-1]
            path.append(i-1)
            i -= 1
        else:
            i-=1

path=sorted(path)
print(path)
